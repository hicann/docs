# 动态AIPP（多个动态AIPP输入）

本节介绍在执行模型推理时，多个动态AIPP输入的模型所涉及的关键接口、示例代码。

## 接口调用流程

模型有多个动态AIPP输入时的推理基本流程与单个动态AIPP输入类似，请参见[动态AIPP（单个动态AIPP输入）](single_dynamic_AIPP_input.md)。

多个动态AIPP输入与单个动态AIPP输入的不同点如下：

- 需调用aclmdlGetAippType接口查询指定模型的指定输入是否有关联的动态AIPP输入，若有，则输出标识动态AIPP输入的index，该参数值可作为aclmdlSetAIPPByInputIndex接口的入参之一，来设置对应输入上的动态AIPP参数值。
- 为避免在错误的输入上设置动态AIPP参数，用户可调用aclmdlGetInputNameByIndex接口先获取指定输入index的输入名称，根据输入名称所对应的index设置动态AIPP参数。

## 示例代码

以下是关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 1. 模型加载，加载成功后，再设置动态AIPP参数值
// ......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_
// ......

// 3. 自定义函数，设置动态AIPP参数值
int  ModelSetDynamicAIPP()
{
    // 3.1 获取标识动态AIPP输入的index
    std::vector<size_t> dataNeedDynamicAipp;
    for (size_t index = 0; index < aclmdlGetNumInputs(modelDesc_); ++index) {
        aclmdlInputAippType aippType;
        size_t dynamicAttachedDataIndex;
        aclError ret = aclmdlGetAippType(modelId_, index, &aippType, &dynamicAttachedDataIndex);
        if (aippType == ACL_DATA_WITH_DYNAMIC_AIPP) {
            dataNeedDynamicAipp.push_back(index);
        }
    }

    // 3.2 当前示例中以2个动态AIPP输入为例，用户可根据实际情况修改
    if (dataNeedDynamicAipp.size() != 2) {
        return -1;
    }
    // 创建第一个动态aipp配置参数
    uint64_t batchNumber1 = 1;
    aclmdlAIPP *aippDynamicSet1 = aclmdlCreateAIPP(batchNumber1);
    ret = aclmdlSetAIPPSrcImageSize(aippDynamicSet1, 256, 224);
    ret = aclmdlSetAIPPInputFormat(aippDynamicSet1, ACL_YUV420SP_U8);
    ret = aclmdlSetAIPPCscParams(aippDynamicSet1, 1, 256, 443, 0, 256, -86, -178, 256, 0, 350, 0, 0, 0, 0, 128, 128);
    ret = aclmdlSetAIPPRbuvSwapSwitch(aippDynamicSet1, 0);
    ret = aclmdlSetAIPPDtcPixelMean(aippDynamicSet1, 0, 0, 0, 0, 0);
    ret = aclmdlSetAIPPDtcPixelMin(aippDynamicSet1, 0, 0, 0, 0, 0);
    ret = aclmdlSetAIPPPixelVarReci(aippDynamicSet1, 1.0, 1.0, 1.0, 1.0, 0);
    ret = aclmdlSetAIPPCropParams(aippDynamicSet1, 1, 2, 2, 224, 224, 0);
    // 设置模型推理时的动态aipp参数值
    ret = aclmdlSetAIPPByInputIndex(modelId_, input_, dataNeedDynamicAipp[0], aippDynamicSet1);
    ret = aclmdlDestroyAIPP(aippDynamicSet1);

    // 创建第二个动态aipp配置参数
    uint64_t batchNumber2 = 1;
    aclmdlAIPP *aippDynamicSet2 = aclmdlCreateAIPP(batchNumber2);
    ret = aclmdlSetAIPPSrcImageSize(aippDynamicSet2, 224, 224);
    // 此处可以继续调用其它AIPP参数设置接口
    // 设置模型推理时的动态aipp参数值
    ret = aclmdlSetAIPPByInputIndex(modelId_, input_, dataNeedDynamicAipp[1], aippDynamicSet2);
    ret = aclmdlDestroyAIPP(aippDynamicSet2);
}

// 4. 自定义函数，执行模型
int ModelExecute(int index)
{
        aclError ret;
        // 4.1 调用自定义函数，设置动态AIPP参数值
    ret = ModelSetDynamicAIPP();
        // 4.2 执行模型，modelId_表示加载成功的模型的ID，input_和output_分别表示模型的输入和输出
        ret = aclmdlExecute(modelId_, input_, output_);
        // ......
}

// 5. 处理模型推理结果
// TODO
```
