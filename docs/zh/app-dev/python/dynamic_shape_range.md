<!-- npu="950,A3,910b,910,310p,310b" id1 -->
# 动态Shape输入（设置Shape范围）
<!-- end id1 -->
## 接口调用流程

如果模型输入Shape是动态的，在模型执行之前调`acl.mdl.set_dataset_tensor_desc`设置该输入的Tensor描述信息（主要是设置Shape信息），在模型执行之后，调用`acl.mdl.get_dataset_tensor_desc`接口获取模型动态输出的Tensor描述信息，再进一步调用aclTensorDesc数据类型的操作接口获取输出Tensor数据占用的内存大小、Tensor的Format信息、Tensor的维度信息等。

关键原理说明如下：

1. 构建模型。

    模型推理场景下，对于动态Shape的输入数据，使用ATC工具转换模型时，通过“input\_shape”参数设置输入Shape范围。

    ATC工具的参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

2. 加载模型。

    模型加载的详细流程，请参见[模型加载](model_load.md)，模型加载成功后，返回标识模型的ID。

3. 创建aclmdlDataset类型的数据，用于描述模型执行的输入、输出。

    详细调用流程请参见[准备模型执行的输入/输出数据结构](model_execute.md#准备模型执行的输入输出数据结构)。

    注意点如下：

    - 当调用`acl.mdl.get_input_size_by_index`获取到的size大小为0时，表示该**输入**的Shape是动态的，用户可根据实际情况预估一块较大的**输入**内存。
    - 当调用`acl.mdl.get_output_size_by_index`获取到的size大小为0时，表示该**输出**的Shape是动态的，用户可根据实际情况预估一块较大的**输出**内存，或者选择由系统内部自行申请对应index的输出内存。详细说明参见`acl.mdl.get_output_size_by_index`接口。

4. 在成功加载模型之后，执行模型之前，调用`acl.mdl.set_dataset_tensor_desc`接口设置动态Shape输入的Tensor描述信息（主要是设置Shape信息）。

    在调用`acl.create_tensor_desc`接口创建Tensor描述信息时，设置Shape信息，包括维度个数、维度大小，此处设置的维度个数、维度大小必须在模型构建时设置的输入Shape范围内，模型构建的详细说明请参见[模型构建](model_construction.md)。

5. （可选）创建Allocator描述符、注册Allocator。

    **注意**：当前仅支持在动态Shape模型推理场景使用外置Allocator管理内存，注册Allocator的接口需配合`acl.mdl.execute_async`接口一起使用，且需在`acl.mdl.execute_async`接口之前调用本接口。

    1. 先调用`acl.rt.allocator_create_desc`创建Allocator描述符 ；
    2. 再分别调用`acl.rt.allocator_set_obj_to_desc`、`acl.rt.allocator_set_alloc_func_to_desc`、`acl.rt.allocator_set_get_addr_from_block_func_to_desc`、`acl.rt.allocator_set_free_func_to_desc`设置Allocator对象及回调函数；
    3. 然后调用`acl.rt.allocator_register`注册Allocator，并将Allocator与stream绑定，模型执行时需使用相同的stream；
    4. 注册Allocator后，可调用`acl.rt.allocator_destroy_desc`接口销毁Allocator描述符。

6. 执行模型。
    - 支持同步推理场景，调用`acl.mdl.execute`接口。
    - 也支持异步推理场景，例如调用`acl.mdl.execute_async`接口，但异步场景下需调用流同步接口（例如`acl.rt.synchronize_stream`）确认异步任务执行完成。
        <!-- npu="910b,910,310p,310b" id3 -->
        异步推理场景下，当前仅`acl.mdl.execute_async`接口支持使用用户注册的Allocator，即第5步注册的Allocator。
        <!-- end id3 -->
7. 获取模型执行的结果数据。

    调用`acl.mdl.get_dataset_tensor_desc`接口获取动态Shape输出的Tensor描述信息，再利用aclTensorDesc数据类型的操作接口获取Tensor描述信息的属性，此处以获取size（表示Tensor数据占用的空间大小）为例，然后从内存中读取对应size的数据。

8. （可选）若在5步中注册Allocator，则此处需要取消注册、销毁已注册的Allocator。

    用户注册的Allocator和Stream绑定，如需主动释放、销毁Allocator，在释放Stream之前，应先调用`acl.rt.allocator_unregister`取消注册，然后释放流资源、销毁用户的Allocator。

## 同步推理场景示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。

```python
# 此例中假设模型的第一个输入为动态输入，其index为0；模型的第一个输出为动态输出，其index为0。
# 1.模型加载，加载成功后，再设置动态输入的Tensor描述信息，主要设置动态输入的Shape信息。
# ......

# 2.准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_。
# 此处需注意：
# 当利用acl.mdl.get_input_size_by_index获取到的size大小为0时，表示该输入的Shape是动态的，用户可根据实际情况预估一块较大的输入内存。
# 当利用acl.mdl.get_output_size_by_index获取到的size大小为0时，表示该输出的Shape是动态的，用户可根据实际情况预估一块较大的输出内存。
# ......

# 3.自定义函数，设置动态输入的Tensor描述信息。
def set_tensor_desc():
    # ......
    # 创建Tensor描述信息，其中dataType和format不需要设置，直接从模型中获取，此处使用的默认值。
    # shape需要和给定的输入数据的shape一致。
    shapes = [1, 3, 224, 224]
    inputDesc = acl.create_tensor_desc(0, shapes, 0)

    # 设置index为0的动态输入的Tensor描述信息。
    dataset, ret = acl.mdl.set_dataset_tensor_desc(input_, inputDesc, 0)
    # ......

# 4.自定义函数，执行模型，并获取动态输出的Tensor描述信息
def model_execute():
    # ......
    # 调用自定义接口，设置动态输入的Tensor描述信息。
    set_tensor_desc()

    # 执行模型。
    ret = acl.mdl.execute(modelId, input_, output_)

    # 获取index为0的动态输出的Tensor描述信息。
    outputDesc = acl.mdl.get_dataset_tensor_desc(output_, 0)

    # 利用aclTensorDesc数据类型的操作接口获取outputDesc的属性，此处需要获取size（表示Tensor数据占用的空间大小），然后从内存中读取对应size的数据。
    outputFileName = "./output"
    outputDesc_size = acl.get_tensor_desc_size(outputDesc)
    dataBuffer = acl.mdl.get_dataset_buffer(output_, 0)
    data = acl.get_data_buffer_addr(dataBuffer)
    outHostData = None

    # 调用acl.rt.get_run_mode接口获取软件栈的运行模式，并根据运行模式判断是否进行数据传输。
    runMode, ret = acl.rt.get_run_mode()
    if runMode == ACL_HOST:
        ret = acl.rt.malloc_host(outHostData, outputDesc_size)

        # 由于动态shape申请的内存比较大，而真实数据的大小是outputDesc_size，所以此处用真实数据大小去拷贝内存。
        ret = acl.rt.memcpy(outHostData, outputDesc_size, data, outputDesc_size, ACL_MEMCPY_DEVICE_TO_HOST)
        with open(outputFileName, "wb") as f:
            f.write(outHostData)
        ret = acl.rt.free_host(outHostData)
    else:
        with open(outputFileName, "wb") as f:
            f.write(data)
    # ......

# 5.处理模型推理结果
# TODO
```

## 异步推理场景示例代码

示例场景为用户注册Allocator，并调用异步接口acl.mdl.execute\_async执行推理。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。

```python
# 此例中假设模型的第一个输入为动态输入，其index为0；模型的第一个输出为动态输出，其index为0。
# 1.模型加载，加载成功后，再设置动态输入的Tensor描述信息，主要设置动态输入的Shape信息。
# ......

# 2.准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_。
# 此处需注意：
# 当利用acl.mdl.get_input_size_by_index获取到的size大小为0时，表示该输入的Shape是动态的，用户可根据实际情况预估一块较大的输入内存。
# 当利用acl.mdl.get_output_size_by_index获取到的size大小为0时，表示该输出的Shape是动态的，用户可根据实际情况预估一块较大的输出内存。
# ......

# 3.自定义函数，设置动态输入的Tensor描述信息。
def set_tensor_desc():
    # ......
    # 创建Tensor描述信息，其中dataType和format不需要设置，直接从模型中获取，此处使用的默认值。
    # shape需要和给定的输入数据的shape一致。
    shapes = [1, 3, 224, 224]
    inputDesc = acl.create_tensor_desc(0, shapes, 0)

    # 设置index为0的动态输入的Tensor描述信息。
    ret = acl.mdl.set_dataset_tensor_desc(input_, inputDesc, 0)
    # ......

# 4. 创建Allocator描述符、注册Allocator
# 假设allocator是用户想要注册的Allocator对象
def register_custom_allocator(allocator, stream):
    # 4.1 创建 AllocatorDesc
    allocatorDesc = acl.rt.allocator_create_desc()
    # 4.2 初始化AllocatorDesc，设置Allocator内存申请、释放相关的回调函数。
    acl.rt.allocator_set_obj_to_desc(allocatorDesc, allocator)
    acl.rt.allocator_set_alloc_func_to_desc(allocatorDesc, CustomMallocFunc)
    acl.rt.allocator_set_free_func_to_desc(allocatorDesc, CustomFreeFunc)
    acl.rt.allocator_set_alloc_advise_func_to_desc(allocatorDesc, CustomMallocAdviseFunc)
    acl.rt.allocator_set_get_addr_from_block_func_to_desc(allocatorDesc, CustomGetBlockAddrFunc)
    # 注册Allocator并和Stream绑定，接口会根据AllocatorDesc创建
    acl.rt.allocator_register(stream, allocatorDesc)
    # Allocator描述符使用完成后，可直接销毁
    acl.rt.allocator_destroy_desc(allocatorDesc)

def model_execute():
    # ......
    # 调用自定义接口，设置动态输入的Tensor描述信息。
    set_tensor_desc()

    # 执行模型。
    ret = acl.mdl.execute_async(modelId, input_, output_, stream)

    # 获取index为0的动态输出的Tensor描述信息。
    outputDesc = acl.mdl.get_dataset_tensor_desc(output_, 0)

    # 利用aclTensorDesc数据类型的操作接口获取outputDesc的属性，此处需要获取size（表示Tensor数据占用的空间大小），然后从内存中读取对应size的数据。
    outputFileName = "./output"
    outputDesc_size = acl.get_tensor_desc_size(outputDesc)
    dataBuffer = acl.mdl.get_dataset_buffer(output_, 0)
    data = acl.get_data_buffer_addr(dataBuffer)
    outHostData = None

    # 调用acl.rt.get_run_mode接口获取软件栈的运行模式，并根据运行模式判断是否进行数据传输。
    runMode, ret = acl.rt.get_run_mode()
    if runMode == ACL_HOST:
        ret = acl.rt.malloc_host(outHostData, outputDesc_size)

        # 由于动态shape申请的内存比较大，而真实数据的大小是outputDesc_size，所以此处用真实数据大小去拷贝内存。
        ret = acl.rt.memcpy(outHostData, outputDesc_size, data, outputDesc_size, ACL_MEMCPY_DEVICE_TO_HOST)
        with open(outputFileName, "wb") as f:
            f.write(outHostData)
        ret = acl.rt.free_host(outHostData)
    else:
        with open(outputFileName, "wb") as f:
            f.write(data)
    # ......

# 5.处理模型推理结果
# TODO
# 6. 取消注册、销毁已注册的 Allocator
def unregister_custom_allocator(stream):
   acl.rt.allocator_unregister(stream)# 由用户自行销毁自定义的Allocator
```
