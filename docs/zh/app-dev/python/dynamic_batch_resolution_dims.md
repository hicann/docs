<!-- npu="950,A3,910b,910,310p,310b" id1 -->
# 动态Batch/动态分辨率/动态维度（设置多档维度值）
<!-- end id1 -->
## 接口调用流程

动态Shape输入场景下模型推理与[模型管理](model_management.md)的流程类似，都涉及初始化与去初始化、运行时资源申请与释放、模型构建、模型加载、模型执行、模型卸载等。

本节中重点描述动态Shape输入场景下模型推理与[模型管理](model_management.md)的不同之处：

1. **构建模型时**，需配置动态Batch、动态分辨率、动态维度（ND格式）相关的信息：

    **若模型推理时包含动态Batch特性**，在模型推理时，需调用pyacl提供的接口设置模型推理时需使用的“batch size”，模型支持的“batch size”已提前在构建模型时配置（使用ATC工具的“dynamic\_batch\_size”参数）。

    **若模型推理时包含动态分辨率特性**，在模型推理时，需调用pyacl提供的接口设置模型推理时需使用的分辨率，模型支持的分辨率已提前在构建模型时配置（使用ATC工具的“dynamic\_image\_size”参数）。

    **若模型推理时包含动态维度（ND格式）特性**，在模型推理时，需调用pyacl提供的接口设置模型推理时需使用的维度值，模型支持哪些维度值已提前在构建模型时配置（使用ATC工具的“dynamic\_dims”参数）。

    构建模型成功后，在生成的om模型中，会新增相应的输入（下文简称动态Batch/动态分辨率/动态维度输入），在模型推理时通过该新增的输入提供具体的Batch值/分辨率/维度值。

    **例如**，a输入的“batch size”是动态的，在om模型中，会新增与a对应的b输入来描述a的batch信息。

    - 在模型执行时，准备a输入的数据结构请参见[准备模型执行的输入/输出数据结构](model_execute.md#准备模型执行的输入输出数据结构)。

        由于输入tensor数据的Shape支持多种档位，在模型执行前才能确定，因此该输入和输出所需的内存大小建议用户调用`acl.mdl.get_input_size_by_index`、`acl.mdl.get_output_size_by_index`接口获取，该接口获取的是最大档位的内存，确保内存够用。模型执行完成后，可以调用`acl.mdl.get_output_dims`接口获取模型输出tensor的实际维度信息。

    - 准备b输入的数据结构、设置b输入的数据请参见第二步。

    ATC工具的参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

2. **在执行模型推理前**：
    - 需准备动态Batch/动态分辨率/动态维度输入的数据结构：
        1. 申请动态Batch/动态分辨率/动态维度输入对应的内存前，需要先调用`acl.mdl.get_input_index_by_name`接口根据输入名称（固定为“ascend_mbatch_shape_data”）获取模型中标识该输入的index。
        2. 调用`acl.mdl.get_input_size_by_index`根据index获取输入内存大小。
        3. 调用`acl.rt.malloc`接口根据上一步中的大小申请内存。

            申请动态Batch/动态分辨率/动态AIPP/动态维度输入对应的内存后，无需用户设置该内存中的数据（否则可能会导致业务异常），用户调用上一步中的接口后，系统会自动向该内存中填入数据。

        4. 调用`acl.create_data_buffer`接口创建aclDataBuffer类型的数据，用于存放动态Batch/动态分辨率/动态维度输入数据的内存地址、内存大小。
        5. 调用`acl.mdl.create_dataset`接口创建aclmdlDataset类型的数据，并调用`acl.mdl.add_dataset_buffer`接口向aclmdlDataset类型的数据中增加aclDataBuffer类型的数据。

    - 需设置动态Batch/动态分辨率/动态维度参数值：

        **图 1**  接口调用流程
        ![](figures/dynamic_shape_API_call_process.png "接口调用流程-3")

        1. 调用`acl.mdl.get_input_index_by_name`接口根据输入名称（固定为“ascend_mbatch_shape_data”）获取模型中标识该输入的index。
        2. 设置动态Batch/动态分辨率/动态维度参数值。
            - 调用`acl.mdl.set_dynamic_batch_size`接口设置动态Batch。

                此处设置的“batch size”只能是构建模型时设置的Batch档位中的某一个。

                也可以调用`acl.mdl.get_dynamic_batch`接口获取指定模型支持的Batch档位数以及每一档中的“batch size”。

            - 调用`acl.mdl.set_dynamic_hw_size`接口设置动态分辨率。

                此处设置的分辨率只能是构建模型时设置的分辨率档位中的某一个。

                也可以调用`acl.mdl.get_dynamic_hw`接口获取指定模型支持的分辨率档位数以及每一档中的宽、高。

            - 调用`acl.mdl.set_input_dynamic_dims`接口设置动态维度的维度值。

                此处设置的动态维度的值只能是构建模型时设置的档位中的某一档。

                也可以调用`acl.mdl.get_input_dynamic_dims`接口获取指定模型支持的动态维度档位数以及每一档中的值。

## 动态Batch示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
# 1.模型加载，加载成功后，再设置动态Batch。
# ......

# 2.创建aclmdlDataset类型的数据，用于描述模型的输入数据input、输出数据output。
# ......

# 3.自定义函数，设置动态Batch。
def model_set_dynamic_info():
    # 3.1 获取动态Batch输入的index，标识动态Batch输入的输入名称固定为“ascend_mbatch_shape_data”。
    index, ret = acl.mdl.get_input_index_by_name(model_desc, "ascend_mbatch_shape_data")
    # 3.2 设置Batch，model_id表示加载成功的模型的ID，input表示aclmdlDataset类型的数据，index表示标识动态Batch输入的输入index。
    batch_size = 8
    ret = acl.mdl.set_dynamic_batch_size(model_id, input, index, batch_size)
    # ......

# 4.自定义函数，执行模型。
def model_execute(index):
    # 4.1 调用自定义函数，设置动态Batch。
    ret = model_set_dynamic_info()
    # 4.2 执行模型，model_id表示加载成功的模型的ID，input和output分别表示模型的输入和输出。
    ret = acl.mdl.execute(model_id, input, output)
    # ......

# 5.处理模型推理结果。
# ......
```

## 动态分辨率示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
# 1.模型加载，加载成功后，再设置动态分辨率。
# ......

# 2.创建aclmdlDataset类型的数据，用于描述模型的输入数据input、输出数据output。
# ......

# 3.自定义函数，设置动态分辨率。
def model_set_dynamic_info():
    # 3.1 获取动态分辨率输入的index，标识动态分辨率输入的输入名称固定为“ascend_mbatch_shape_data”。
    index, ret = acl.mdl.get_input_index_by_name(model_desc, "ascend_mbatch_shape_data")
    # 3.2 设置输入图片分辨率，model_id表示加载成功的模型的ID，input表示aclmdlDataset类型的数据，index表示标识动态分辨率输入的输入index。
    height = 224
    width = 224
    ret = acl.mdl.set_dynamic_hw_size(model_id, input, index, height, width)
    # ......

# 4.自定义函数，执行模型。
def model_execute(index):
    # 4.1 调用自定义函数，设置动态分辨率。
    ret = model_set_dynamic_info()
    # 4.2 执行模型，model_id表示加载成功的模型的ID，input和output分别表示模型的输入和输出。
    ret = acl.mdl.execute(model_id, input, output)
    # ......

# 5.处理模型推理结果。
# ......
```

## ND格式，动态维度示例代码

调用接口后，需增加异常处理的分支，示例代码中不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.模型加载，加载成功后，再设置动态维度。
# ......

# 2.准备模型描述信息model_desc，准备模型的输入数据input和模型的输出数据output。
# ......

# 3.自定义函数，设置动态维度。
def model_set_dynamic_info():
    # 3.1 获取动态维度输入的index，标识动态维度输入的输入名称固定为“ascend_mbatch_shape_data”。
    index, ret = acl.mdl.get_input_index_by_name(model_desc, "ascend_mbatch_shape_data")
    # 3.2 设置具体档位信息，包括维度数dimCount和各个维度的数值，model_id表示加载成功的模型的ID，input表示aclmdlDataset类型的数据，index表示标识动态维度输入的输入index。
    current_dims = {'name': '', 'dimCount': 4, 'dims': [8, 3, 224, 224]}
    ret = acl.mdl.set_input_dynamic_dims(model_id, input, index, current_dims)
    # ......

# 4.自定义函数，执行模型。
def model_execute(index):
    # 4.1 调用自定义函数，设置动态维度。
    ret = model_set_dynamic_info()
    # 4.2 执行模型，model_id表示加载成功的模型的ID，input和output分别表示模型的输入和输出。
    ret = acl.mdl.execute(model_id, input, output)
    # ......

# 5.处理模型推理结果。
# ......
```
