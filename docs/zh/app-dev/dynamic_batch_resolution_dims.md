# 动态Batch/动态分辨率/动态维度（设置多档维度值）

本节介绍动态Batch/动态分辨率/动态维度功能涉及的关键接口、接口调用流程及示例代码。

## 接口调用流程

动态Shape输入场景下模型推理与[静态Shape输入模型推理](static_shape_model_inference.md)的流程类似，都涉及初始化与去初始化、运行时资源申请与释放、模型构建、模型加载、模型执行、模型卸载等。

本节中重点描述动态Shape输入场景下模型推理与[静态Shape输入模型推理](static_shape_model_inference.md)的不同之处：

1. **构建模型时**，需配置动态Batch、动态分辨率、动态维度（ND格式）相关的信息：

    **若模型推理时包含动态Batch特性**，在模型推理时，需调用acl接口设置模型推理时需使用的batch size，模型支持的batch size已提前在构建模型时配置，例如构建模型时使用ATC工具的dynamic\_batch\_size参数，详细参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 基础功能参数 \> 输入选项 \> --dynamic\_batch\_size”。

    **若模型推理时包含动态分辨率特性**，在模型推理时，需调用acl接口设置模型推理时需使用的分辨率，模型支持的分辨率已提前在构建模型时配置，例如构建模型时使用ATC工具的dynamic\_image\_size参数，详细参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 基础功能参数 \> 输入选项 \> --dynamic\_image\_size”。

    **若模型推理时包含动态维度（ND格式）特性**，在模型推理时，需调用acl接口设置模型推理时需使用的维度值，模型支持哪些维度值已提前在构建模型时配置，例如构建模型时使用ATC工具的dynamic\_dims参数，详细参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 基础功能参数 \> 输入选项 \> --dynamic\_dims”。

    构建模型成功后，在生成的om模型中，会新增相应的输入（下文简称动态Batch输入/动态分辨率输入/动态维度输入），在模型推理时通过该新增的输入提供具体的Batch值/分辨率/维度值。

    **例如**，a输入的batch size是动态的，在om模型中，会新增与a对应的b输入来描述a的batch信息。

    - 在模型执行时，准备a输入的数据结构请参见[准备模型执行的输入/输出数据结构](model_execute.md#section1620016465510)。

        由于输入tensor数据的Shape支持多种档位，在模型执行前才能确定，因此该输入和输出所需的内存大小建议用户调用aclmdlGetInputSizeByIndex、aclmdlGetOutputSizeByIndex接口获取，该接口获取的是最大档位的内存，确保内存够用。模型执行完成后，可以调用aclmdlGetCurOutputDims接口获取模型输出tensor的实际维度信息。

    - 准备b输入的数据结构、设置b输入的数据请参见第2步。

2. **在执行模型推理前**：
    - 需准备动态Batch/动态分辨率/动态维度输入的数据结构：
        1. 申请动态Batch/动态分辨率/动态维度输入对应的内存前，需要先调用aclmdlGetInputIndexByName接口根据输入名称（固定为ACL\_DYNAMIC\_TENSOR\_NAME）获取模型中标识该输入的index。

            >**说明：** 
            >ACL\_DYNAMIC\_TENSOR\_NAME是一个宏，宏的定义如下：
>
            >```
            >#define ACL_DYNAMIC_TENSOR_NAME "ascend_mbatch_shape_data"
            >```

        2. 调用aclmdlGetInputSizeByIndex根据index获取输入内存大小。
        3. 调用aclrtMalloc接口根据[2.b](#zh-cn_topic_0000001086879105_li899693033013)中的大小申请内存。

            申请动态Batch/动态分辨率/动态AIPP/动态维度输入对应的内存后，无需用户设置该内存中的数据（否则可能会导致业务异常），用户调用[2.b](#li1767343825610)中的接口后，系统会自动向该内存中填入数据。

        4. 调用aclCreateDataBuffer接口创建aclDataBuffer类型的数据，用于存放动态Batch/动态分辨率/动态维度输入数据的内存地址、内存大小。
        5. 调用aclmdlCreateDataset接口创建aclmdlDataset类型的数据，并调用aclmdlAddDatasetBuffer接口向aclmdlDataset类型的数据中增加aclDataBuffer类型的数据。

    - 需设置动态Batch/动态分辨率/动态维度参数值：

        **图 1**  接口调用流程  
        ![](figures/dynamic_shape_API_call_process.png "接口调用流程")

        1. 调用aclmdlGetInputIndexByName接口根据输入名称（固定为ACL\_DYNAMIC\_TENSOR\_NAME）获取模型中标识该输入的index。
        2. 设置动态Batch/动态分辨率/动态维度参数值。
            - 调用aclmdlSetDynamicBatchSize接口设置动态Batch。

                此处设置的batch size只能是构建模型时设置的Batch档位中的某一个。

                也可以调用aclmdlGetDynamicBatch接口获取指定模型支持的Batch档位数以及每一档中的batch size。

            - 调用aclmdlSetDynamicHWSize接口设置动态分辨率。

                此处设置的分辨率只能是构建模型时设置的分辨率档位中的某一个。

                也可以调用aclmdlGetDynamicHW接口获取指定模型支持的分辨率档位数以及每一档中的宽、高。

            - 调用aclmdlSetInputDynamicDims接口设置动态维度的维度值。

                此处设置的动态维度的值只能是构建模型时设置的档位中的某一档。

                也可以调用aclmdlGetInputDynamicDims接口获取指定模型支持的动态维度档位数以及每一档中的值。

## 动态Batch示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="910,310p,310b" id1 -->
您可以单击[YOLOV3\_dynamic\_batch\_detection\_picture](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/2_object_detection/YOLOV3_dynamic_batch_detection_picture)获取样例。
<!-- end id1 -->

```cpp
......

// 1. 模型加载，加载成功后，再设置动态Batch
......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_
// ......

// 3. 自定义函数，设置动态Batch
int  ModelSetDynamicInfo()
{
        size_t index;
        // 3.1 获取动态Batch输入的index，标识动态Batch输入的输入名称固定为ACL_DYNAMIC_TENSOR_NAME
        aclError ret = aclmdlGetInputIndexByName(modelDesc_, ACL_DYNAMIC_TENSOR_NAME, &index);
        // 3.2 设置Batch
        // modelId_表示加载成功的模型的ID，input_表示aclmdlDataset类型的数据，index表示标识动态Batch输入的输入index，batchSize表示Batch数（此处以8为例）
        uint64_t batchSize = 8;
        ret = aclmdlSetDynamicBatchSize(modelId_, input_, index, batchSize);
        // ......
}

// 4. 自定义函数，执行模型
int ModelExecute(int index)
{
        aclError ret;
        // 4.1 调用自定义函数，设置动态Batch
    ret = ModelSetDynamicInfo();
        // 4.2 执行模型，modelId_表示加载成功的模型的ID，input_和output_分别表示模型的输入和输出
        ret = aclmdlExecute(modelId_, input_, output_);
        // ......
}
// 5. 处理模型推理结果
......
```

## 动态分辨率示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="910,310p,310b" id2 -->
您可以单击[YOLOV3\_dynamic\_batch\_detection\_picture](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/2_object_detection/YOLOV3_dynamic_batch_detection_picture)获取样例。
<!-- end id2 -->

```cpp
......

// 1. 模型加载，加载成功后，再设置动态分辨率
......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_
......

// 3. 自定义函数，设置动态分辨率
int  ModelSetDynamicInfo()
{
        size_t index;
                // 3.1 获取动态分辨率输入的index，标识动态分辨率输入的输入名称固定为ACL_DYNAMIC_TENSOR_NAME
        aclError ret = aclmdlGetInputIndexByName(modelDesc_, ACL_DYNAMIC_TENSOR_NAME, &index);
                // 3.2 设置输入图片分辨率，modelId_表示加载成功的模型的ID，input_表示aclmdlDataset类型的数据，index表示标识动态分辨率输入的输入index
                uint64_t height = 224;
        uint64_t width = 224;
        ret = aclmdlSetDynamicHWSize(modelId_, input_, index, height, width);
                // ......
}

// 4. 自定义函数，执行模型
int ModelExecute(int index)
{
        aclError ret;
        // 4.1 调用自定义函数，设置动态分辨率
    ret = ModelSetDynamicInfo();
        // 4.2 执行模型，modelId_表示加载成功的模型的ID，input_和output_分别表示模型的输入和输出
        ret = aclmdlExecute(modelId_, input_, output_);
        // ......
}

// 5. 处理模型推理结果
......
```

## ND格式，动态维度示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
......

// 1. 模型加载，加载成功后，再设置动态维度
......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_
......

// 3. 自定义函数，设置动态维度
int  ModelSetDynamicInfo()
{
        size_t index;
        // 3.1 获取动态维度输入的index，动态维度输入的输入名称固定为ACL_DYNAMIC_TENSOR_NAME
        aclError ret = aclmdlGetInputIndexByName(modelDesc_, ACL_DYNAMIC_TENSOR_NAME, &index);
        // 3.2 设置具体档位信息，包括维度数dimCount和各个维度的数值，modelId_表示加载成功的模型的ID，input_表示aclmdlDataset类型的数据，index表示标识动态维度输入的输入index
        aclmdlIODims currentDims;
        currentDims.dimCount = 4;
        currentDims.dims[0] = 8;
        currentDims.dims[1] = 3;
        currentDims.dims[2] = 224;
        currentDims.dims[3] = 224;
        ret = aclmdlSetInputDynamicDims(modelId_, input_, index, &currentDims);
        // ......
}

// 4. 自定义函数，执行模型
int ModelExecute(int index)
{
        aclError ret;
        // 4.1 调用自定义函数，设置动态维度
    ret = ModelSetDynamicInfo();
        // 4.2 执行模型，modelId_表示加载成功的模型的ID，input_和output_分别表示模型的输入和输出
        ret = aclmdlExecute(modelId_, input_, output_);
        // ......
}
// 5. 处理模型推理结果
......
```
