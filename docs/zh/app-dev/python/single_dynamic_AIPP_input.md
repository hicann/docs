<!-- npu="950,A3,910b,910,310p,310b" id1 -->
# 动态AIPP（单个动态AIPP输入）
<!-- end id1 -->
## 接口调用流程

动态AIPP场景下模型推理与[模型管理](model_management.md)的流程类似，都涉及初始化与去初始化、运行时资源申请与释放、模型构建、模型加载、模型执行、模型卸载等。

本节中重点描述动态AIPP场景下模型推理与[模型管理](model_management.md)的不同之处：

- **模型构建时**，需配置动态AIPP相关参数：

    **在构建模型时**，需调用pyacl提供的接口设置模型推理时需使用的AIPP配置，模型支持的AIPP模式已提前在构建模型时配置（使用ATC工具的“insert_op_conf”参数）。ATC工具的参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。

    **构建模型成功后**，在生成的om模型中，会新增相应的输入（下文简称动态AIPP输入），在模型推理时通过该新增的输入提供具体的AIPP配置值。

    **例如**，a输入的AIPP配置是动态的，在om模型中，会有与a对应的b输入来描述a的AIPP配置信息。在模型执行时，准备a输入的数据结构请参见[准备模型执行的输入/输出数据结构](model_execute.md#准备模型执行的输入输出数据结构)，准备b输入的数据结构、设置b输入的数据请参见以下内容。

- **在执行模型推理前**：
    - 准备动态AIPP输入的数据结构：
        1. 申请动态AIPP输入对应的内存前，需要先调用`acl.mdl.get_input_index_by_name`接口根据输入名称（固定为“ascend_dynamic_aipp_data”）获取模型中标识该输入的index。
        2. 调用`acl.mdl.get_input_size_by_index`根据index获取输入内存大小。
        3. 调用`acl.rt.malloc`接口根据前一步中的大小申请内存。

            申请动态AIPP输入对应的内存后，无需用户设置该内存中的数据（否则可能会导致业务异常），用户调用前一步中的接口后，系统会自动向该内存中填入数据。

        4. 调用`acl.create_data_buffer`接口创建aclDataBuffer类型的数据，用于存放动态AIPP输入数据的内存地址、内存大小。
        5. 调用`acl.mdl.create_dataset`接口创建aclmdlDataset类型的数据，并调用`acl.mdl.add_dataset_buffer`接口向aclmdlDataset类型的数据中增加aclDataBuffer类型的数据。

    - 设置动态AIPP参数值：

        **图 1**  接口调用流程
        ![](figures/dynamic_AIPP_API_call_process.png "接口调用流程")

        1. 调用`acl.mdl.get_input_index_by_name`接口根据输入名称（固定为“ascend_dynamic_aipp_data”）获取模型中标识该输入的index。
        2. 设置动态AIPP参数值。
            1. 调用`acl.mdl.create_aipp`接口创建aclmdlAIPP类型。
            2. 根据实际需求，调用aclmdlAIPP数据类型下的操作接口设置动态AIPP参数值。
            3. 动态AIPP场景下，`acl.mdl.set_aipp_src_image_size`接口（设置原始图片的宽和高）必须调用。
            4. 调用`acl.mdl.set_input_aipp`接口设置模型推理时的动态AIPP数据。
            5. 及时调用`acl.mdl.destroy_aipp`接口销毁aclmdlAIPP类型。

## 示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

ACL_YUV420SP_U8 = 1

# 1.模型加载，加载成功后，再设置动态AIPP参数值。
# ......

# 2.创建aclmdlDataset类型的数据，用于描述模型的输入数据input_dataset和模型的输出数据output_dataset。
# ......

# 3.自定义函数，设置动态AIPP参数值。
def model_set_dynamic_aipp():
    # 3.1 获取标识动态AIPP输入的index。
    index, ret = acl.mdl.get_input_index_by_name(model_desc, "ascend_dynamic_aipp_data")

    # 3.2 设置动态AIPP参数值。
    batch_number = 1
    aipp_dynamic_set = acl.mdl.create_aipp(batch_number)
    ret = acl.mdl.set_aipp_src_image_size(aipp_dynamic_set, 256, 224)
    ret = acl.mdl.set_aipp_input_format(aipp_dynamic_set, ACL_YUV420SP_U8)
    ret = acl.mdl.set_aipp_csc_params(aipp_dynamic_set, 1, 256, 443, 0, 256, -86, -178, 256, 0, 350, 0, 0, 0, 0, 128, 128)
    ret = acl.mdl.set_aipp_rbuv_swap_switch(aipp_dynamic_set, 0)
    ret = acl.mdl.set_aipp_dtc_pixel_mean(aipp_dynamic_set, 0, 0, 0, 0, 0)
    ret = acl.mdl.set_aipp_dtc_pixel_min(aipp_dynamic_set, 0, 0, 0, 0, 0)
    ret = acl.mdl.set_aipp_pixel_var_reci(aipp_dynamic_set, 1, 1, 1, 1, 0)
    ret = acl.mdl.set_aipp_crop_params(aipp_dynamic_set, 1, 0, 0, 224, 224, 0)
    ret = acl.mdl.set_input_aipp(model_id, input_dataset, index, aipp_dynamic_set)
    ret = acl.mdl.destroy_aipp(aipp_dynamic_set)
    # ......

# 4.自定义函数，执行模型。
def model_execute(index):
    # 4.1 调用自定义函数，设置动态AIPP参数值。
    ret = model_set_dynamic_aipp()
    # 4.2 执行模型，modelId_表示加载成功的模型的ID，input_和output_分别表示模型的输入和输出。
    ret = acl.mdl.execute(model_id, input_dataset, output_dataset)
    # ......

# 5.处理模型推理结果。
# ......
```
