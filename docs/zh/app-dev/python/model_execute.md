# 模型执行

## 基本原理

开发应用时，如果涉及整网模型推理，则应用程序中必须包含模型执行的代码逻辑，关于模型执行的接口调用流程。请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。

本节描述的是**整网模型执行**的接口调用流程，对于算子模型加载与执行的详细说明请参见[单算子调用](single_operator_invoke.md)。

- **在模型加载之后，模型执行之前**，需要准备输入、输出数据结构，将输入数据传输到模型输入数据结构的对应内存中。
- **模型执行结束后**，若无需使用输入数据、aclmdlDesc类型、aclmdlDataset类型、aclDataBuffer类型等相关资源，需及时释放内存、销毁对应的数据类型，防止内存异常。

    模型可能存在多个输入、多个输出，每个输入/输出的内存地址、内存大小用aclDataBuffer类型的数据来描述，针对每个输入/输出，需调用`acl.rt.free`接口释放内存中的数据，并调用`acl.destroy_data_buffer`接口销毁相应的aclDataBuffer类型。

## 接口调用流程

**图 1**  基本的模型推理流程
![](figures/basic_model_inference_process.png "基本的模型推理流程")

关键接口的说明如下：

1. 调用`acl.mdl.create_desc`接口**创建描述模型基本信息**的数据类型。
2. 调用`acl.mdl.get_desc`接口根据[模型加载](model_load.md)中返回的模型ID**获取模型基本信息**。
3. **准备模型执行的输入、输出数据结构**，具体流程请参见[准备模型执行的输入/输出数据结构](#准备模型执行的输入输出数据结构)。

    如果模型的输入涉及动态Batch、动态分辨率、动态AIPP、动态维度（ND格式）等特性，请参见[模型动态Shape输入推理](dynamic_shape_model_inference.md)、[模型动态AIPP推理](dynamic_AIPP_inference.md)。

4. **执行模型推理**。

    对于固定的多Batch场景，需要满足Batch数后，才能将输入数据发送给模型进行推理。不满足Batch数时，用户需根据自己的实际场景处理。

    当前系统支持模型的同步推理和异步推理：

    - 同步推理时调用`acl.mdl.execute`接口。
    - 异步推理时调用`acl.mdl.execute_async`接口。

        对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞应用程序运行，直到指定Stream中的所有任务都完成。

        异步推理的详细介绍，请参见[模型异步推理](model_asynchronous_inference.md)。

5. **获取模型推理的结果**，用于后续处理。

    对于同步推理，直接获取模型推理的输出数据即可。

    对于异步推理，在实现Callback功能时，在回调函数内获取模型推理的结果，供后续使用。

6. **释放内存**。

    调用`acl.rt.free`接口释放Device上的内存。

7. **释放相关数据类型的数据**。

    在模型推理结束后，需及时依次调用`acl.destroy_data_buffer`接口和`acl.mdl.destroy_dataset`接口释放描述模型输入的数据。**如果存在多个输入、输出**，需多次调用`acl.destroy_data_buffer`接口。

## 准备模型执行的输入/输出数据结构

pyacl提供了以下数据类型来描述模型、模型输入、模型输出以及存放数据的内存，在模型执行前，需要构造好这些数据类型，作为模型执行的输入：

- 使用**aclmdlDesc**类型的数据描述模型基本信息（例如输入/输出的个数、名称、数据类型、Format、维度信息等）。

    模型加载成功后，用户可根据模型的ID，调用`acl.mdl.get_desc`接口获取该模型的描述信息，进而从模型的描述信息中获取模型输入/输出的个数、内存大小、维度信息、Format、数据类型等信息，可参见`aclmdlDesc`类型下的操作接口。

- 使用**aclmdlDataset**类型的数据描述模型的输入/输出数据，模型可能存在多个输入、多个输出。

    调用`aclmdlDataset`类型下的操作接口添加aclDataBuffer类型的数据、获取aclDataBuffer的个数等。

- 每个输入/输出的内存地址、内存大小用**aclDataBuffer**类型的数据来描述。

    调用`aclDataBuffer`类型下的操作接口获取内存地址、内存大小等。

**图 2**  aclmdlDataset类型与aclDataBuffer类型的关系
![](figures/relationship_between_aclmdlDataset_and_aclDataBuffer.png "aclmdlDataset类型与aclDataBuffer类型的关系")

了解相关的数据类型后，可以使用这些数据类型的操作接口准备模型的输入、输出数据结构，如下图所示。

**图 3**  模型执行的输入/输出数据结构的准备流程
![](figures/prepare_model_input_output.png "模型执行的输入-输出数据结构的准备流程")

关键说明如下：

- 模型存在多个输入、输出时，用户可调用`acl.mdl.get_num_inputs`、`acl.mdl.get_num_outputs`接口获取输入、输出的个数。
- 模型每个输入、输出所需的内存大小，用户可调用`acl.mdl.get_input_size_by_index`、`acl.mdl.get_output_size_by_index`接口获取。

    如果模型的输入涉及动态Batch、动态分辨率、动态维度（ND格式）等特性，输入Tensor数据的Shape支持多种档位，在模型执行前才能确定，因此该输入所需的内存大小建议用户调用`acl.mdl.get_input_size_by_index`接口获取，该接口获取的是最大档位的内存，确保内存够用。

- 模型存在多个输入、输出时，用户在向aclmdlDataset中添加aclDataBuffer时，为避免顺序出错，可以先调用`acl.mdl.get_input_name_by_index`、`acl.mdl.get_output_name_by_index`接口获取输入、输出的名称，根据输入、输出名称所对应的index的顺序添加。

## 示例代码（准备模型的输入和输出数据结构）
<!-- npu="950,A3,910b,910,310p,310b" id1 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id1 -->

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
# 初始化变量。
ACL_MEM_MALLOC_HUGE_FIRST = 0

# 1.根据模型的ID，获取该模型的描述信息。
# self.model_desc为aclmdlDesc类型。
self.model_desc = acl.mdl.create_desc()
ret = acl.mdl.get_desc(self.model_desc, self.model_id)

# 2.准备模型推理的输入数据集。
# 创建aclmdlDataset类型的数据，描述模型推理的输入。
self.load_input_dataset = acl.mdl.create_dataset()
# 获取模型输入的数量。
input_size = acl.mdl.get_num_inputs(self.model_desc)
self.input_data = []
# 循环为每个输入申请内存，并将每个输入添加到aclmdlDataset类型的数据中。
for i in range(input_size):
    buffer_size = acl.mdl.get_input_size_by_index(self.model_desc, i)
    # 申请输入内存。
    buffer, ret = acl.rt.malloc(buffer_size, ACL_MEM_MALLOC_HUGE_FIRST)
    data = acl.create_data_buffer(buffer, buffer_size)
    _, ret = acl.mdl.add_dataset_buffer(self.load_input_dataset, data)
    self.input_data.append({"buffer": buffer, "size": buffer_size})

# 3.准备模型推理的输出数据集。
# 创建aclmdlDataset类型的数据，描述模型推理的输出。
self.load_output_dataset = acl.mdl.create_dataset()
# 获取模型输出的数量。
output_size = acl.mdl.get_num_outputs(self.model_desc)
self.output_data = []
# 循环为每个输出申请内存，并将每个输出添加到aclmdlDataset类型的数据中。
for i in range(output_size):
    buffer_size = acl.mdl.get_output_size_by_index(self.model_desc, i)
    # 申请输出内存。
    buffer, ret = acl.rt.malloc(buffer_size, ACL_MEM_MALLOC_HUGE_FIRST)
    data = acl.create_data_buffer(buffer, buffer_size)
    _, ret = acl.mdl.add_dataset_buffer(self.load_output_dataset, data)
    self.output_data.append({"buffer": buffer, "size": buffer_size})

# ......
```

## 示例代码（执行模型）
<!-- npu="950,A3,910b,910,310p,310b" id2 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id2 -->
调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
ACL_MEMCPY_HOST_TO_DEVICE = 1
ACL_MEMCPY_DEVICE_TO_HOST = 2
NPY_BYTE = 1
images_list = ["./data/dog1_1024_683.jpg", "./data/dog2_1024_683.jpg"]

for image in images_list:
    # 1.自定义函数transfer_pic，使用Python库读取图片文件，并对图片进行缩放、剪裁等操作。
    # transfer_pic函数的实现请参考样例中源代码。
    img = transfer_pic(image)

    # 2.准备模型推理的输入数据，运行模式默认为运行模式为ACL_HOST，当前实例代码中模型只有一个输入。
    if "bytes_to_ptr" in dir(acl.util):
        bytes_data = img.tobytes()
        ptr = acl.util.bytes_to_ptr(bytes_data)
    else:
        ptr = acl.util.numpy_to_ptr(img)
    # 将图片数据从Host传输到Device。
    ret = acl.rt.memcpy(self.input_data[0]["buffer"], self.input_data[0]["size"], ptr,
                         self.input_data[0]["size"], ACL_MEMCPY_HOST_TO_DEVICE)

    # 3.执行模型推理。
    # self.model_id表示模型ID，在模型加载成功后，会返回标识模型的ID。
    ret = acl.mdl.execute(self.model_id, self.load_input_dataset, self.load_output_dataset)

# ......
```

## 示例代码（处理推理结果：直接处理内存中的数据）
<!-- npu="950,A3,910b,910,310p,310b" id3 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id3 -->

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

以图片分类网络为例，模型执行结束后，需处理每一张图片的模型推理结果，直接输出top5置信度的类别编号。

```python
# 处理模型推理的输出数据，输出top5置信度的类别编号。
inference_result = []
for i, item in enumerate(self.output_data):
    buffer_host, ret = acl.rt.malloc_host(self.output_data[i]["size"])
    # 将推理输出数据从Device传输到Host。
    ret = acl.rt.memcpy(buffer_host, self.output_data[i]["size"], self.output_data[i]["buffer"],
                         self.output_data[i]["size"], ACL_MEMCPY_DEVICE_TO_HOST)

    bytes_out = acl.util.ptr_to_bytes(buffer_host, self.output_data[i]["size"])
    data = np.frombuffer(bytes_out, dtype=np.byte)

    inference_result.append(data)
    tuple_st = struct.unpack("1000f", bytearray(inference_result[0]))
    vals = np.array(tuple_st).flatten()
    top_k = vals.argsort()[-1:-6:-1]
    print("======== top5 inference results: =============")
    for j in top_k:
        print("[%d]: %f" % (j, vals[j]))

# ......
```

## 示例代码（处理推理结果：调用单算子处理推理结果）
<!-- npu="950,A3,910b,910,310p,310b" id4 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_imagenet_classification)中获取完整的同步推理样例代码。
<!-- end id4 -->

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

以图片分类网络为例，模型执行结束后，需处理每一张图片的模型推理结果，直接输出最大置信度的类别编号。
<!-- npu="910b,910,310p,310b" id5 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vpc_resnet50_imagenet_classification)中获取完整的图片解码+缩放+同步推理样例代码。
<!-- end id5 -->

当前示例中，使用Cast算子（将推理结果的数据类型从float32转成float16）和ArgMaxD算子（从推理结果中查找最大置信度的类别标识）实现数据后处理。单算子调用的流程请参见[接口调用流程](single_operator_interface_calling_process.md)。

- Cast算子被封装成pyacl接口，因此在使用时，将算子的输入输出Tensor描述、算子输入输出数据的内存等信息作为`acl.op.cast`的入参，直接调用`acl.op.cast`接口加载并执行算子。
- ArgMaxD算子没有被封装成pyacl接口，因此在使用时，必须自行构造算子描述信息（输入输出Tensor描述、算子属性等）、申请存放算子输入输出数据的内存、明确算子类型名称、调用`acl.op.execute_v2`接口加载并执行算子。

```python
ACL_MEMCPY_DEVICE_TO_HOST = 2

# 提前将Cast和ArgMaxD两个单算子的定义文件*.json编译成适配昇腾AI处理器的离线模型（*.om文件），用于验证单算子的运行。
# 设置单算子模型文件所在的目录，加载单算子模型。
ret = acl.op.set_model_dir("./op_models")
# ......

# 以下步骤需针对每一张图片的模型推理结果进行处理。
# 1.在数据后处理前，先获取模型推理的输出，dataset_ptr表示模型推理的输出。
self.input_buffer = acl.mdl.get_dataset_buffer(dataset_ptr, 0)

# 2.自定义函数_forward_op_cast，构造Cast算子的输入输出Tensor描述、申请存放算子输出数据的内存dev_buffer_cast、调用acl.op.cast接口加载并执行算子。
self._forward_op_cast()

# 3.自定义函数_forward_op_arg_max_d，构造ArgMaxD算子的输入输出Tensor、输入输出Tensor描述、算子属性、申请存放算子输出数据的内存dev_buffer_arg_max_d、调用acl.op.execute_v2接口加载并执行算子。
self._forward_op_arg_max_d()

# 4.将ArgMaxD算子的输出数据回传到Host。
# 4.1 根据ArgMaxD算子输出数据的大小，申请Host上的内存。
host_buffer, ret = acl.rt.malloc_host(self.tensor_size_arg_max_d)

# 4.2 将ArgMaxD算子的输出数据从Device复制到Host。
ret = acl.rt.memcpy(host_buffer,
                     self.tensor_size_arg_max_d,
                     self.dev_buffer_arg_max_d,
                     self.tensor_size_arg_max_d,
                     ACL_MEMCPY_DEVICE_TO_HOST)

# 4.3 在终端窗口显示最大置信度的类别编号。
bytes_out = acl.util.ptr_to_bytes(buffer_host, self.output_shape)
data = np.frombuffer(bytes_out, dtype=np.int32).reshape((self.output_shape,))
print("[SingleOP][ArgMaxOp] label of classification result is:{}"
      .format(data[0]))

# 5.释放资源。
# 5.1 释放Host的内存。
ret = acl.rt.free_host(host_buffer)

# 5.2 释放Device上存放算子输出数据的内存。
ret = acl.rt.free(self.dev_buffer_cast)
ret = acl.rt.free(self.dev_buffer_arg_max_d)

# 5.3 释放aclDataBuffer类型数据（用于描述算子输出数据）。
ret = acl.destroy_data_buffer(self.output_buffer_cast)
ret = acl.destroy_data_buffer(self.output_buffer_arg_max_d)

# ......
```

## 示例代码（释放模型的输入、输出资源）
<!-- npu="950,A3,910b,910,310p,310b" id6 -->
您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id6 -->

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
# 释放模型推理的输入、输出资源。
# 释放输入资源，包括数据结构和内存。
while self.input_data:
    item = self.input_data.pop()
    ret = acl.rt.free(item["buffer"])
input_number = acl.mdl.get_dataset_num_buffers(self.load_input_dataset)
for i in range(input_number):
    data_buf = acl.mdl.get_dataset_buffer(self.load_input_dataset, i)
    if data_buf:
        ret = acl.destroy_data_buffer(data_buf)
ret = acl.mdl.destroy_dataset(self.load_input_dataset)

# 释放输出资源，包括数据结构和内存。
while self.output_data:
    item = self.output_data.pop()
    ret = acl.rt.free(item["buffer"])
output_number = acl.mdl.get_dataset_num_buffers(self.load_output_dataset)
for i in range(output_number):
    data_buf = acl.mdl.get_dataset_buffer(self.load_output_dataset, i)
    if data_buf:
        ret = acl.destroy_data_buffer(data_buf)
ret = acl.mdl.destroy_dataset(self.load_output_dataset)
```
