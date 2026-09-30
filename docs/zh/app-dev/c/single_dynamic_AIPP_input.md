# 动态AIPP（单个动态AIPP输入）

本节介绍在执行模型推理时，单个动态AIPP输入的模型所涉及的关键接口、示例代码。

## 接口调用流程

动态AIPP场景下模型推理与[静态Shape输入模型推理](static_shape_model_inference.md)的流程类似，都涉及初始化与去初始化、运行时资源申请与释放、模型构建、模型加载、模型执行、模型卸载等。

本节中重点描述动态AIPP场景下模型推理与[静态Shape输入模型推理](static_shape_model_inference.md)的不同之处：

- **模型构建时**，需配置动态AIPP相关参数：

    **构建模型时**，需通过ATC工具的insert\_op\_conf参数配置动态AIPP模式。ATC工具的参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 高级功能参数 \> 功能配置选项 \> --insert\_op\_conf”。

    **构建模型成功后**，在生成的om模型中，会新增相应的输入（下文简称动态AIPP输入），在模型推理时通过该新增的输入提供具体的AIPP配置值。

    **例如**，a输入的AIPP配置是动态的，在om模型中，会有与a对应的b输入来描述a的AIPP配置信息。在模型执行时，准备a输入的数据结构请参见[准备模型执行的输入/输出数据结构](model_execute.md#section1620016465510)，准备b输入的数据结构、设置b输入的数据请参见以下内容。

- **在执行模型推理前**：
    - 准备动态AIPP输入的数据结构：
        1. 申请动态AIPP输入对应的内存前，需要先调用aclmdlGetAippDataSize接口获取内存大小。

            同时，旧版本中调用aclmdlGetInputSizeByIndex接口获取内存大小的方式依然支持，但该方式在batch size不固定的场景下获取到的内存大小可能为0，此时用户需自行预估内存大小。若调用aclmdlGetInputSizeByIndex接口获取内存大小，还需提前调用aclmdlGetInputIndexByName接口根据输入名称（固定为ACL\_DYNAMIC\_AIPP\_NAME宏，表示ascend\_dynamic\_aipp\_data）获取模型中标识该输入的index。

        2. 调用aclrtMalloc接口根据前一步中获取的大小申请内存。

            申请动态AIPP输入对应的内存后，无需用户设置该内存中的数据（否则可能会导致业务异常），用户调用设置动态AIPP参数值的接口后，系统会自动向该内存中填入数据。

        3. 调用aclCreateDataBuffer接口创建aclDataBuffer类型的数据，用于存放动态AIPP输入数据的内存地址、内存大小。
        4. 调用aclmdlCreateDataset接口创建aclmdlDataset类型的数据，并调用aclmdlAddDatasetBuffer接口向aclmdlDataset类型的数据中增加aclDataBuffer类型的数据。

    - 设置动态AIPP参数值：

        **图 1**  接口调用流程  
        ![](figures/dynamic_AIPP_API_call_process.png "接口调用流程")

        1. 调用aclmdlGetInputIndexByName接口根据输入名称（固定为ACL\_DYNAMIC\_AIPP\_NAME）获取模型中标识该输入的index。
        2. 设置动态AIPP参数值。
            1. 调用aclmdlCreateAIPP接口创建aclmdlAIPP类型。
            2. 根据实际需求，调用aclmdlAIPP数据类型下的操作接口设置动态AIPP参数值。
            3. 动态AIPP场景下，aclmdlSetAIPPSrcImageSize接口（设置原始图片的宽和高）必须调用。
            4. 调用aclmdlSetInputAIPP接口设置模型推理时的动态AIPP数据。
            5. 及时调用aclmdlDestroyAIPP接口销毁aclmdlAIPP类型。

## 示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
......

// 1. 模型加载，加载成功后，再设置动态AIPP参数值
// ......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_

// 3. 自定义函数，设置动态AIPP参数值
int  ModelSetDynamicAIPP()
{
    // 3.1 获取标识动态AIPP输入的index
    size_t index;
    // modelDesc_为aclmdlCreateDesc表示模型描述信息，根据1中加载成功的模型的ID，获取该模型的描述信息
    aclError ret = aclmdlGetInputIndexByName(modelDesc_, ACL_DYNAMIC_AIPP_NAME, &index);

    // 3.2 设置动态AIPP参数值
    uint64_t batchNumber = 1;
    aclmdlAIPP *aippDynamicSet = aclmdlCreateAIPP(batchNumber);
    ret = aclmdlSetAIPPSrcImageSize(aippDynamicSet, 256, 224);
    ret = aclmdlSetAIPPInputFormat(aippDynamicSet, ACL_YUV420SP_U8);
    ret = aclmdlSetAIPPCscParams(aippDynamicSet, 1, 256, 443, 0, 256, -86, -178, 256, 0, 350, 0, 0, 0, 0, 128, 128);
    ret = aclmdlSetAIPPRbuvSwapSwitch(aippDynamicSet, 0);
    ret = aclmdlSetAIPPDtcPixelMean(aippDynamicSet, 0, 0, 0, 0, 0);
    ret = aclmdlSetAIPPDtcPixelMin(aippDynamicSet, 0, 0, 0, 0, 0);
    ret = aclmdlSetAIPPPixelVarReci(aippDynamicSet, 1.0, 1.0, 1.0, 1.0, 0);
    ret = aclmdlSetAIPPCropParams(aippDynamicSet, 1, 2, 2, 224, 224, 0);
    ret = aclmdlSetInputAIPP(modelId_, input_, index, aippDynamicSet);
    ret = aclmdlDestroyAIPP(aippDynamicSet);
        
    // ......
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
......
```
