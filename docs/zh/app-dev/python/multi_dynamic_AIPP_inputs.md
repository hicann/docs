<!-- npu="910b,910,310p,310b" id1 -->
# 动态AIPP（多个动态AIPP输入）
<!-- end id1 -->
## 接口调用流程

模型有多个动态AIPP输入时的推理基本流程与单个动态AIPP输入类似，请参见[动态AIPP（单个动态AIPP输入）](single_dynamic_AIPP_input.md)。

多个动态AIPP输入与单个动态AIPP输入的不同点如下：

- 需调用`acl.mdl.get_aipp_type`接口查询指定模型的指定输入是否有关联的动态AIPP输入，若有，则输出标识动态AIPP输入的index，该参数值可作为`acl.mdl.set_aipp_by_input_index`接口的入参之一，来设置对应输入上的动态AIPP参数值。
- 为避免在错误的输入上设置动态AIPP参数，用户可调用`acl.mdl.get_input_name_by_index`接口先获取指定输入index的输入名称，根据输入名称所对应的index设置动态AIPP参数。

## 示例代码

调用接口后，需增加异常处理的分支，示例代码中不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

ACL_DATA_WITH_DYNAMIC_AIPP = 2
ACL_YUV420SP_U8 = 1

# 1.模型加载，加载成功后，再设置动态AIPP参数值。
# ......

# 2.准备模型描述信息model_desc，准备模型的输入数据input_dataset和模型的输出数据output_dataset。
# ......

# 3.自定义函数，设置动态AIPP参数值。
def model_set_dynamic_aipp():
    # 3.1 获取标识动态AIPP输入的index。
    need_dynamic_aipp = []
    input_num = acl.mdl.get_num_inputs(model_desc)
    for index in range(input_num):
        aipp_type, dynamic_attached_index, ret = acl.mdl.get_aipp_type(model_id, index)
        if aipp_type == ACL_DATA_WITH_DYNAMIC_AIPP:
            need_dynamic_aipp.append(index)

    # 3.2 当前示例中以2个动态AIPP输入为例，用户可根据实际情况修改。
    if len(need_dynamic_aipp) != 2:
        return 1
    # 创建第一个动态aipp配置参数。
    batch_number_first = 1
    aipp_dynamic_set_first = acl.mdl.create_aipp(batch_number_first)
    ret = acl.mdl.set_aipp_src_image_size(aipp_dynamic_set_first, 256, 224)
    ret = acl.mdl.set_aipp_input_format(aipp_dynamic_set_first, ACL_YUV420SP_U8)
    ret = acl.mdl.set_aipp_csc_params(aipp_dynamic_set_first, 1, 256, 443, 0, 256, -86,
                                         -178, 256, 0, 350, 0, 0, 0, 0, 128, 128)
    ret = acl.mdl.set_aipp_rbuv_swap_switch(aipp_dynamic_set_first, 0)
    ret = acl.mdl.set_aipp_dtc_pixel_mean(aipp_dynamic_set_first, 0, 0, 0, 0, 0)
    ret = acl.mdl.set_aipp_dtc_pixel_min(aipp_dynamic_set_first, 0, 0, 0, 0, 0)
    ret = acl.mdl.set_aipp_pixel_var_reci(aipp_dynamic_set_first, 1.0, 1.0, 1.0, 1.0, 0)
    ret = acl.mdl.set_aipp_crop_params(aipp_dynamic_set_first, 1, 2, 2, 224, 224, 0)
    # 设置模型推理时的动态aipp参数值。
    ret = acl.mdl.set_aipp_by_input_index(model_id, input_dataset, need_dynamic_aipp[0],
                                              aipp_dynamic_set_first)
    ret = acl.mdl.destroy_aipp(aipp_dynamic_set_first)
    # 创建第二个动态aipp配置参数。
    batch_number_second = 2
    aipp_dynamic_set_second = acl.mdl.create_aipp(batch_number_second)
    ret = acl.mdl.set_aipp_src_image_size(aipp_dynamic_set_second, 224, 224)
    # 此处可以继续调用其它AIPP参数设置接口。
    # 设置模型推理时的动态aipp参数值。
    ret = acl.mdl.set_aipp_by_input_index(model_id, input_dataset, need_dynamic_aipp[1],
                                              aipp_dynamic_set_second)
    ret = acl.mdl.destroy_aipp(aipp_dynamic_set_second)
    return ret

# 4.自定义函数，执行模型。
def model_execute(index):
    # 4.1 调用自定义函数，设置动态AIPP参数值。
    ret = model_set_dynamic_aipp()
    # 4.2 执行模型，modelId_表示加载成功的模型的ID，input_dataset和output_dataset分别表示模型的输入和输出。
    ret = acl.mdl.execute(model_id, input_dataset, output_dataset)
    # ......

# 5.处理模型推理结果。
# ......
```
