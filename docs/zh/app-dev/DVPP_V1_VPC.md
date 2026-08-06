# VPC图像处理典型功能

本节以抠图、缩放为例说明VPC图像处理时的接口调用流程，同时配合以下典型功能的示例代码辅助理解该接口调用流程。

VPC（Vision Preprocessing Core）负责图像处理功能，支持对图片做抠图、缩放、格式转换等操作。关于VPC功能的详细介绍以及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程（以抠图、缩放为例）

**图 1**  抠图缩放流程  
![](figures/抠图缩放流程.png "抠图缩放流程")

关键接口的说明如下（以抠图、缩放处理为例）：

1. 调用aclInit接口初始化系统。
2. 调用aclrtSetDevice接口指定计算设备。
3. 调用aclrtCreateStream接口创建Stream。
4. 调用acldvppCreateChannel接口**创建图片数据处理的通道**。

    创建图片数据处理的通道前，需先调用acldvppCreateChannelDesc接口创建通道描述信息。

5. 调用acldvppCreateRoiConfig接口、acldvppCreateResizeConfig接口分别**创建抠图区域位置的配置、缩放配置**，调用acldvppSetResizeConfigInterpolation接口指定缩放算法。
6. 实现抠图、缩放功能前，若需要**申请Device上的内存**存放输入或输出数据，需调用acldvppMalloc申请内存。
7. **执行抠图、缩放**。
    - 关于抠图：
        - 调用acldvppVpcCropAsync异步接口，按指定区域从输入图片中抠图，再将抠取的图片存放到输出内存中，作为输出图片。

            输出图片区域与抠图区域cropArea不一致时会对图片再做一次缩放操作。

        - 当前系统还提供了acldvppVpcCropAndPasteAsync异步接口，支持按指定区域从输入图片中抠图，再将抠的图片贴到目标图片的指定位置，作为输出图片。
            - 抠图区域cropArea的宽高与贴图区域pasteArea宽高不一致时会对图片再做一次缩放操作。
            - 如果用户需要将目标图片读入内存用于存放输出图片，将贴图区域叠加在目标图片上，则需要编写代码逻辑：在申请输出内存后，将目标图片读入输出内存。

    - 关于缩放
        - 调用acldvppVpcResizeAsync异步接口，将输入图片缩放到输出图片大小。
        - 缩放后输出图片内存根据YUV420SP格式计算，计算公式：对齐后的宽\*对齐后的高\*3/2

    - 对于异步接口，还需调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成。

8. 调用acldvppFree接口**释放输入、输出内存**。
9. 调用acldvppDestroyRoiConfig接口、acldvppDestroyResizeConfig接口分别**销毁抠图区域位置的配置、缩放配置**。
10. 调用acldvppDestroyChannel接口**销毁图片数据处理的通道**。

    销毁图片数据处理的通道后，再调用acldvppDestroyChannelDesc接口销毁通道描述信息。

11. 调用aclrtDestroyStream接口销毁Stream。
12. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
13. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 图片缩放示例代码

以下是图片缩放功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

您可以单击[vpc\_resnet50\_imagenet\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vpc_resnet50_imagenet_classification)获取样例。

```cpp
// 1. 创建图片缩放配置数据、指定缩放算法
// resizeConfig_是acldvppResizeConfig类型
acldvppResizeConfig *resizeConfig_ = acldvppCreateResizeConfig();
aclError ret = acldvppSetResizeConfigInterpolation(resizeConfig_, 0);

// 2. 创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型
dvppChannelDesc_ = acldvppCreateChannelDesc();

// 3. 创建图片数据处理的通道。
ret = acldvppCreateChannel(dvppChannelDesc_);

// 4. 申请输入内存（区分运行状态）
// 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);
// inputPicWidth、inputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t resizeInBufferSize = inputPicWidth * inputPicHeight * 3 / 2;
if(runMode == ACL_HOST){ 
    // 申请Host内存vpcInHostBuffer
    void* vpcInHostBuffer = nullptr;
    vpcInHostBuffer = malloc(resizeInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, vpcInHostBuffer, resizeInBufferSize);
    // 申请Device内存resizeInDevBuffer_
    ret = acldvppMalloc(&resizeInDevBuffer_, resizeInBufferSize);
    // 通过aclrtMemcpy接口将输入图片数据传输到Device
    ret = aclrtMemcpy(resizeInDevBuffer_, resizeInBufferSize, vpcInHostBuffer, resizeInBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);
    // 数据传输完成后，及时释放内存
    free(vpcInHostBuffer);
} else {
    // 申请Device输入内存resizeInDevBuffer_
    ret = acldvppMalloc(&resizeInDevBuffer_, resizeInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, resizeInDevBuffer_, resizeInBufferSize);
}

// 5. 申请缩放输出内存resizeOutBufferDev_，内存大小resizeOutBufferSize_根据计算公式得出
// outputPicWidth、outputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t resizeOutBufferSize_ = outputPicWidth * outputPicHeight * 3 / 2;
ret = acldvppMalloc(&resizeOutBufferDev_, resizeOutBufferSize_);

// 6. 创建缩放输入图片的描述信息，并设置各属性值
// resizeInputDesc_是acldvppPicDesc类型
resizeInputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(resizeInputDesc_, resizeInDevBuffer_);
acldvppSetPicDescFormat(resizeInputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
acldvppSetPicDescWidth(resizeInputDesc_, inputWidth_);
acldvppSetPicDescHeight(resizeInputDesc_, inputHeight_);
acldvppSetPicDescWidthStride(resizeInputDesc_, inputWidthStride);
acldvppSetPicDescHeightStride(resizeInputDesc_, inputHeightStride);
acldvppSetPicDescSize(resizeInputDesc_, resizeInBufferSize);

// 7. 创建缩放输出图片的描述信息，并设置各属性值
// 如果缩放的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致
// resizeOutputDesc_是acldvppPicDesc类型
resizeOutputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(resizeOutputDesc_, resizeOutBufferDev_);
acldvppSetPicDescFormat(resizeOutputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420); 
acldvppSetPicDescWidth(resizeOutputDesc_, resizeOutputWidth_);
acldvppSetPicDescHeight(resizeOutputDesc_, resizeOutputHeight_);
acldvppSetPicDescWidthStride(resizeOutputDesc_, resizeOutputWidthStride);
acldvppSetPicDescHeightStride(resizeOutputDesc_, resizeOutputHeightStride);
acldvppSetPicDescSize(resizeOutputDesc_, resizeOutBufferSize_);

// 8. 执行异步缩放，再调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成
ret = acldvppVpcResizeAsync(dvppChannelDesc_, resizeInputDesc_,
        resizeOutputDesc_, resizeConfig_, stream_);
ret = aclrtSynchronizeStream(stream_);

// 9. 缩放结束后，释放资源，包括缩放输入/输出图片的描述信息、缩放输入/输出内存
acldvppDestroyPicDesc(resizeInputDesc_);
acldvppDestroyPicDesc(resizeOutputDesc_);

if(runMode == ACL_HOST){ 
    // 该模式下，由于处理结果在Device侧，因此需要调用内存复制接口传输结果数据后，再释放Device侧内存
    // 申请Host内存vpcOutHostBuffer
    void* vpcOutHostBuffer = nullptr;
    vpcOutHostBuffer = malloc(resizeOutBufferSize_);
    // 通过aclrtMemcpy接口将Device的处理结果数据传输到Host
    ret = aclrtMemcpy(vpcOutHostBuffer, resizeOutBufferSize_, resizeOutBufferDev_, resizeOutBufferSize_, ACL_MEMCPY_DEVICE_TO_HOST);
    // 释放掉输入输出的device内存
    (void)acldvppFree(resizeInDevBuffer_);
    (void)acldvppFree(resizeOutBufferDev_);
    // 数据使用完成后，释放内存
    free(vpcOutHostBuffer);
} else { 
    // 此时运行在device侧，处理结果也在Device侧，可以根据需要操作处理结果后，释放Device侧内存
    (void)acldvppFree(resizeInDevBuffer_);
    (void)acldvppFree(resizeOutBufferDev_);
}
acldvppDestroyChannel(dvppChannelDesc_);
(void)acldvppDestroyChannelDesc(dvppChannelDesc_);
dvppChannelDesc_ = nullptr;

 ....
```

## 格式转换示例代码

格式转换支持以下两种实现方式：

- 在实现抠图、缩放等功能时，调用对应的接口（例如acldvppVpcCropAsync接口）时，通过将输入图片和输出图片的格式设置成不同的，达到转换图片格式的目的。
- 如果仅做图片格式转换，也可以直接调用acldvppVpcConvertColorAsync接口。

以下是格式转换功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 1. 创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型
dvppChannelDesc_ = acldvppCreateChannelDesc();

// 2. 创建图片数据处理的通道。
aclError ret = acldvppCreateChannel(dvppChannelDesc_);

// 3. 申请输入内存（区分运行状态）
// 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);
// inputPicWidth、inputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t inBufferSize = inputPicWidth * inputPicHeight * 3 / 2;
if(runMode == ACL_HOST){ 
    // 申请Host内存vpcInHostBuffer
    void* vpcInHostBuffer = nullptr;
    vpcInHostBuffer = malloc(inBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, vpcInHostBuffer, inBufferSize);
    // 申请Device内存inDevBuffer_
    ret = acldvppMalloc(&inDevBuffer_, inBufferSize);
    // 通过aclrtMemcpy接口将输入图片数据传输到Device
    ret = aclrtMemcpy(inDevBuffer_, inBufferSize, vpcInHostBuffer, inBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);
    // 数据传输完成后，及时释放内存
    free(vpcInHostBuffer);
} else {
    // 申请Device输入内存inDevBuffer_
    ret = acldvppMalloc(&inDevBuffer_, inBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, inDevBuffer_, inBufferSize);
}

// 4. 申请色域转换输出内存outBufferDev_，内存大小outBufferSize_根据计算公式得出
// outputPicWidth、outputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t outBufferSize_ = outputPicWidth * outputPicHeight * 3 / 2;
ret = acldvppMalloc(&outBufferDev_, outBufferSize_);

// 5. 创建色域转换输入图片的描述信息，并设置各属性值
// inputDesc_是acldvppPicDesc类型
inputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(inputDesc_, inDevBuffer_);
acldvppSetPicDescFormat(inputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
acldvppSetPicDescWidth(inputDesc_, inputWidth_);
acldvppSetPicDescHeight(inputDesc_, inputHeight_);
acldvppSetPicDescWidthStride(inputDesc_, inputWidthStride);
acldvppSetPicDescHeightStride(inputDesc_, inputHeightStride);
acldvppSetPicDescSize(inputDesc_, inBufferSize);

// 6. 创建色域转换的输出图片的描述信息，并设置各属性值, 输出的宽和高要求和输入一致
// 如果色域转换的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致
// outputDesc_是acldvppPicDesc类型
outputDesc_= acldvppCreatePicDesc();
acldvppSetPicDescData(outputDesc_, outBufferDev_);
acldvppSetPicDescFormat(outputDesc_, PIXEL_FORMAT_YUV_400); 
acldvppSetPicDescWidth(outputDesc_, outputWidth_);
acldvppSetPicDescHeight(outputDesc_, outputHeight_);
acldvppSetPicDescWidthStride(outputDesc_, outputWidthStride);
acldvppSetPicDescHeightStride(outputDesc_, outputHeightStride);
acldvppSetPicDescSize(outputDesc_, outBufferSize_);

// 7. 执行异步色域转换，再调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成
ret = acldvppVpcConvertColorAsync(dvppChannelDesc_, inputDesc_, outputDesc_, stream_);
ret = aclrtSynchronizeStream(stream_);

// 8. 色域转换结束后，释放资源，包括输入/输出图片的描述信息、输入/输出内存
acldvppDestroyPicDesc(inputDesc_);
acldvppDestroyPicDesc(outputDesc_);

if(runMode == ACL_HOST){ 
    // 该模式下，由于处理结果在Device侧，因此需要调用内存复制接口传输结果数据后，再释放Device侧内存
    // 申请Host内存vpcOutHostBuffer
    void* vpcOutHostBuffer = nullptr;
    vpcOutHostBuffer = malloc(outBufferSize_);
    // 通过aclrtMemcpy接口将Device的处理结果数据传输到Host
    ret = aclrtMemcpy(vpcOutHostBuffer, outBufferSize_, outBufferDev_, outBufferSize_, ACL_MEMCPY_DEVICE_TO_HOST);
    // 释放掉输入输出的device内存
    (void)acldvppFree(inDevBuffer_);
    (void)acldvppFree(outBufferDev_);
    // 数据使用完成后，释放内存
    free(vpcOutHostBuffer);
} else { 
    // 此时运行在device侧，处理结果也在Device侧，可以根据需要操作处理结果后，释放Device侧内存
    (void)acldvppFree(inDevBuffer_);
    (void)acldvppFree(outBufferDev_);
}
acldvppDestroyChannel(dvppChannelDesc_);
(void)acldvppDestroyChannelDesc(dvppChannelDesc_);
dvppChannelDesc_ = nullptr;

....
```

## 抠图缩放（一图一框）示例代码

调用acldvppVpcCropResizeAsync异步接口，按指定区域从输入图片中抠图，再将抠取的图片存放到输出内存中，作为输出图片，此外，还支持指定缩放算法。当输出图片区域与抠图区域cropArea不一致时会对图片再做一次缩放操作。

以下是抠图缩放功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

您可以单击[vpc\_jpeg\_resnet50\_imagenet\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)获取样例。

```cpp
// 1. 创建缩放配置数据，并指定抠图区域的位置
// resizeConfig_是acldvppResizeConfig类型
resizeConfig_ = acldvppCreateResizeConfig();
aclError ret = acldvppSetResizeConfigInterpolation(resizeConfig_, 0);
// cropArea_是acldvppRoiConfig类型
cropArea_ = acldvppCreateRoiConfig(550, 749, 480, 679);

// 2. 创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型
dvppChannelDesc_ = acldvppCreateChannelDesc();

// 3. 创建图片数据处理的通道。
ret = acldvppCreateChannel(dvppChannelDesc_);

// 4. 申请输入内存（区分运行状态）
// 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);
// inputPicWidth、inputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t cropInBufferSize = inputPicWidth * inputPicHeight * 3 / 2;
if(runMode == ACL_HOST){ 
    // 申请Host内存cropInHostBuffer
    void* cropInHostBuffer = nullptr;
    cropInHostBuffer = malloc(cropInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, cropInHostBuffer, cropInBufferSize);
    // 申请Device内存cropInDevBuffer_
    ret = acldvppMalloc(&cropInDevBuffer_, cropInBufferSize);
    // 通过aclrtMemcpy接口图片数据传输到Device
    ret = aclrtMemcpy(cropInDevBuffer_, cropInBufferSize, cropInHostBuffer, cropInBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);
    // 数据传输完成后，及时释放内存
    free(cropInHostBuffer);
} else { 
    // 申请Device输入内存cropInDevBuffer_
    ret = acldvppMalloc(&cropInDevBuffer_, cropInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, cropInDevBuffer_, cropInBufferSize);
}

// 5. 申请Device输出内存cropOutBufferDev_，内存大小cropOutBufferSize_根据计算公式得出
// outputPicWidth、outputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t cropOutBufferSize_ = outputPicWidth * outputPicHeight * 3 / 2;
ret = acldvppMalloc(&cropOutBufferDev_, cropOutBufferSize_);

// 6. 创建输入图片的描述信息，并设置各属性值，cropInputDesc_是acldvppPicDesc类型
cropInputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(cropInputDesc_, cropInDevBuffer_);
acldvppSetPicDescFormat(cropInputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
acldvppSetPicDescWidth(cropInputDesc_, inputWidth_);
acldvppSetPicDescHeight(cropInputDesc_, inputHeight_);
acldvppSetPicDescWidthStride(cropInputDesc_, inputWidthStride);
acldvppSetPicDescHeightStride(cropInputDesc_, inputHeightStride);
acldvppSetPicDescSize(cropInputDesc_, cropInBufferSize);

// 7. 创建输出图片的描述信息，并设置各属性值，cropOutputDesc_是acldvppPicDesc类型
// 如果抠图的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致
cropOutputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(cropOutputDesc_, cropOutBufferDev_);
acldvppSetPicDescFormat(cropOutputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420); 
acldvppSetPicDescWidth(cropOutputDesc_, OutputWidth_);
acldvppSetPicDescHeight(cropOutputDesc_, OutputHeight_);
acldvppSetPicDescWidthStride(cropOutputDesc_, OutputWidthStride);
acldvppSetPicDescHeightStride(cropOutputDesc_, OutputHeightStride);
acldvppSetPicDescSize(cropOutputDesc_, cropOutBufferSize_);

// 8. 执行异步抠图缩放，再调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成
ret = acldvppVpcCropResizeAsync(dvppChannelDesc_, cropInputDesc_,
        cropOutputDesc_, cropArea_, resizeConfig_, stream_);
ret = aclrtSynchronizeStream(stream_);

// 9. 抠图贴图结束后，释放资源，包括输入/输出图片的描述信息、输入/输出内存、通道描述信息、通道等
acldvppDestroyRoiConfig(cropArea_);
acldvppDestroyResizeConfig(resizeConfig_);
acldvppDestroyPicDesc(cropInputDesc_);
acldvppDestroyPicDesc(cropOutputDesc_);
if(runMode == ACL_HOST){ 
    // 该模式下，由于处理结果在Device侧，因此需要调用内存复制接口传输结果数据后，再释放Device侧内存
    // 申请Host内存cropOutHostBuffer
    void* cropOutHostBuffer = nullptr;
    cropOutHostBuffer = malloc(cropOutBufferSize_);
    // 通过aclrtMemcpy接口将Device的处理结果数据传输到Host
    ret = aclrtMemcpy(cropOutHostBuffer, cropOutBufferSize_, cropOutBufferDev_, cropOutBufferSize_, ACL_MEMCPY_DEVICE_TO_HOST);
    // 释放掉输入输出的device内存
    (void)acldvppFree(cropInDevBuffer_);
    (void)acldvppFree(cropOutBufferDev_);
    // 数据使用完成后，释放内存
    free(cropOutHostBuffer);
} else { 
    // 此时运行在device侧，处理结果也在Device侧，可以根据需要操作抠图结果后，释放Device侧内存
    (void)acldvppFree(cropInDevBuffer_);
    (void)acldvppFree(cropOutBufferDev_);
}
acldvppDestroyChannel(dvppChannelDesc_);
(void)acldvppDestroyChannelDesc(dvppChannelDesc_);
dvppChannelDesc_ = nullptr;

....
```

## 抠图贴图缩放（一图一框）示例代码

调用acldvppVpcCropResizePasteAsync异步接口，按指定区域从输入图片中抠图，再将抠的图片贴到目标图片的指定位置，作为输出图片，此外，还支持指定缩放算法。当抠图区域cropArea的宽高与贴图区域pasteArea宽高不一致时会对图片再做一次缩放操作。如果用户需要将目标图片读入内存用于存放输出图片，将贴图区域叠加在目标图片上，则需要编写代码逻辑：在申请输出内存后，将目标图片读入输出内存。

以下是抠图贴图缩放功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

您可以单击[vpc\_jpeg\_resnet50\_imagenet\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)获取样例。

```cpp
// 1.  创建缩放配置数据，并指定抠图区域的位置、指定贴图区域的位置
// resizeConfig_是acldvppResizeConfig类型
resizeConfig_ = acldvppCreateResizeConfig();
aclError ret = acldvppSetResizeConfigInterpolation(resizeConfig_, 0);
// cropArea_和pasteArea_是acldvppRoiConfig类型
cropArea_ = acldvppCreateRoiConfig(512, 711, 512, 711);
pasteArea_ = acldvppCreateRoiConfig(16, 215, 16, 215);

// 2. 创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型
dvppChannelDesc_ = acldvppCreateChannelDesc();

// 3. 创建图片数据处理的通道。
ret = acldvppCreateChannel(dvppChannelDesc_);

// 4. 申请输入内存（区分运行状态）
// 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);
// inputPicWidth、inputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t vpcInBufferSize = inputPicWidth * inputPicHeight * 3 / 2;
if(runMode == ACL_HOST){ 
    // 申请Host内存vpcInHostBuffer
    void* vpcInHostBuffer = nullptr;
    vpcInHostBuffer = malloc(vpcInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, vpcInHostBuffer, vpcInBufferSize);
    // 申请Device内存vpcInDevBuffer_
    ret = acldvppMalloc(&vpcInDevBuffer_, vpcInBufferSize);
    // 通过aclrtMemcpy接口将输入图片数据传输到Device
    ret = aclrtMemcpy(vpcInDevBuffer_, vpcInBufferSize, vpcInHostBuffer, vpcInBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);
    // 数据传输完成后，及时释放内存
    free(vpcInHostBuffer);
} else {
    // 申请Device输入内存vpcInDevBuffer_
    ret = acldvppMalloc(&vpcInDevBuffer_, vpcInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, vpcInDevBuffer_, vpcInBufferSize);
}

// 5. 申请输出内存vpcOutBufferDev_，内存大小vpcOutBufferSize_根据计算公式得出
// outputPicWidth、outputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t vpcOutBufferSize_ = outputPicWidth * outputPicHeight * 3 / 2;
ret = acldvppMalloc(&vpcOutBufferDev_, vpcOutBufferSize_);

// 6. 创建输入图片的描述信息，并设置各属性值
// 此处示例将解码的输出内存作为抠图贴图的输入，vpcInputDesc_是acldvppPicDesc类型
vpcInputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(vpcInputDesc_, decodeOutBufferDev_); 
acldvppSetPicDescFormat(vpcInputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
acldvppSetPicDescWidth(vpcInputDesc_, inputWidth_);
acldvppSetPicDescHeight(vpcInputDesc_, inputHeight_);
acldvppSetPicDescWidthStride(vpcInputDesc_, jpegOutWidthStride);
acldvppSetPicDescHeightStride(vpcInputDesc_, jpegOutHeightStride);
acldvppSetPicDescSize(vpcInputDesc_, jpegOutBufferSize);

// 7. 创建输出图片的描述信息，并设置各属性值
// 如果抠图贴图的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致
// vpcOutputDesc_是acldvppPicDesc类型
vpcOutputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(vpcOutputDesc_, vpcOutBufferDev_);
acldvppSetPicDescFormat(vpcOutputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
acldvppSetPicDescWidth(vpcOutputDesc_, dvppOutWidth);
acldvppSetPicDescHeight(vpcOutputDesc_, dvppOutHeight);
acldvppSetPicDescWidthStride(vpcOutputDesc_, dvppOutWidthStride);
acldvppSetPicDescHeightStride(vpcOutputDesc_, dvppOutHeightStride);
acldvppSetPicDescSize(vpcOutputDesc_, vpcOutBufferSize_);

// 8. 执行异步抠图贴图缩放，再调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成
ret = acldvppVpcCropResizePasteAsync(dvppChannelDesc_, vpcInputDesc_,
        vpcOutputDesc_, cropArea_, pasteArea_, resizeConfig_, stream_);
ret = aclrtSynchronizeStream(stream_);

// 9. 抠图贴图结束后，释放资源，包括输入/输出图片的描述信息、输入/输出内存、通道描述信息、通道等
acldvppDestroyRoiConfig(cropArea_);
acldvppDestroyRoiConfig(pasteArea_);
acldvppDestroyResizeConfig(resizeConfig_);
acldvppDestroyPicDesc(vpcInputDesc_);
acldvppDestroyPicDesc(vpcOutputDesc_);

if(runMode == ACL_HOST){ 
    // 该模式下，由于处理结果在Device侧，因此需要调用内存复制接口传输结果数据后，再释放Device侧内存
    // 申请Host内存vpcOutHostBuffer
    void* vpcOutHostBuffer = nullptr;
    vpcOutHostBuffer = malloc(vpcOutBufferSize_);
    // 通过aclrtMemcpy接口将Device的处理结果数据传输到Host
    ret = aclrtMemcpy(vpcOutHostBuffer, vpcOutBufferSize_, vpcOutBufferDev_, vpcOutBufferSize_, ACL_MEMCPY_DEVICE_TO_HOST);
    // 释放掉输入输出的device内存
    (void)acldvppFree(vpcInDevBuffer_);
    (void)acldvppFree(vpcOutBufferDev_);
    // 数据使用完成后，释放内存
    free(vpcOutHostBuffer);
} else { 
    // 此时运行在device侧，处理结果也在Device侧，可以根据需要操作处理结果后，释放Device侧内存
    (void)acldvppFree(vpcInDevBuffer_);
    (void)acldvppFree(vpcOutBufferDev_);
}

acldvppDestroyChannel(dvppChannelDesc_);
(void)acldvppDestroyChannelDesc(dvppChannelDesc_);
dvppChannelDesc_ = nullptr;

....
```

## 抠图贴图（一图多框）示例代码

调用acldvppVpcBatchCropAndPasteAsync异步接口，按指定区域从输入图片中抠图，再将抠的图片贴到目标图片的指定位置，作为输出图片。当抠图区域cropArea的宽高与贴图区域pasteArea宽高不一致时会对图片再做一次缩放操作。如果用户需要将目标图片读入内存用于存放输出图片，将贴图区域叠加在目标图片上，则需要编写代码逻辑：在申请输出内存后，将目标图片读入输出内存。

以下是抠图贴图功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 1. 指定批量抠图区域的位置、指定批量贴图区域的位置,cropAreas_和pasteAreas_是acldvppRoiConfig类型
acldvppRoiConfig *cropAreas_[2], pasteAreas_[2];
cropAreas_[0] = acldvppCreateRoiConfig(512, 711, 512, 711);
cropAreas_[1] = acldvppCreateRoiConfig(512, 711, 512, 711);
pasteAreas_[0] = acldvppCreateRoiConfig(16, 215, 16, 215);
pasteAreas_[1] = acldvppCreateRoiConfig(16, 215, 16, 215);

// 2. 创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型
dvppChannelDesc_ = acldvppCreateChannelDesc();

// 3. 创建图片数据处理的通道。
aclError ret = acldvppCreateChannel(dvppChannelDesc_);

// 4. 申请输入内存（区分运行状态）
// 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);
// inputPicWidth、inputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t vpcInBufferSize = inputPicWidth * inputPicHeight * 3 / 2;
if(runMode == ACL_HOST){ 
    // 申请Host内存vpcInHostBuffer
    void* vpcInHostBuffer = nullptr;
    vpcInHostBuffer = malloc(vpcInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, vpcInHostBuffer, vpcInBufferSize);
    // 申请Device内存vpcInDevBuffer_
    ret = acldvppMalloc(&vpcInDevBuffer_, vpcInBufferSize);
    // 通过aclrtMemcpy接口将Host的图片数据传输到Device
    ret = aclrtMemcpy(vpcInDevBuffer_, vpcInBufferSize, vpcInHostBuffer, vpcInBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);
    // 数据传输完成后，及时释放内存
    free(vpcInHostBuffer);
} else {
    // 申请Device输入内存vpcInDevBuffer_
    ret = acldvppMalloc(&vpcInDevBuffer_, vpcInBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, vpcInDevBuffer_, vpcInBufferSize);
}

// 5. 申请输出内存vpcOutBufferDev_，内存大小vpcOutBufferSize_根据计算公式得出
// outputPicWidth、outputPicHeight分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例
uint32_t vpcOutBufferSize_ = outputPicWidth * outputPicHeight * 3 / 2;
ret = acldvppMalloc(&vpcOutBufferDev_, vpcOutBufferSize_);

// 6. 创建输入图片的描述信息，并设置各属性值
// 此处示例将解码的输出内存作为抠图贴图的输入，vpcInputDesc_是acldvppPicDesc类型
vpcInputBatchDesc_ = acldvppCreateBatchPicDesc(1);
vpcInputDesc_ = acldvppGetPicDesc(vpcInputBatchDesc_, 0);
acldvppSetPicDescData(vpcInputDesc_, decodeOutBufferDev_); 
acldvppSetPicDescFormat(vpcInputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
acldvppSetPicDescWidth(vpcInputDesc_, inputWidth_);
acldvppSetPicDescHeight(vpcInputDesc_, inputHeight_);
acldvppSetPicDescWidthStride(vpcInputDesc_, jpegOutWidthStride);
acldvppSetPicDescHeightStride(vpcInputDesc_, jpegOutHeightStride);
acldvppSetPicDescSize(vpcInputDesc_, jpegOutBufferSize);

// 7. 创建批量输出图片的描述信息，并设置各属性值
// 如果抠图贴图的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致
// vpcOutputDesc_是acldvppPicDesc类型
vpcOutputBatchDesc_ = acldvppCreateBatchPicDesc(2);
for (uint32_t index=0; index<2; ++index){
     vecOutPtr_.push_back(vpcOutBufferDev_);
     vpcOutputDesc_ = acldvppGetPicDesc(vpcInputBatchDesc_, index);
    acldvppSetPicDescData(vpcOutputDesc_, vpcOutBufferDev_);
    acldvppSetPicDescFormat(vpcOutputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420);
    acldvppSetPicDescWidth(vpcOutputDesc_, dvppOutWidth);
    acldvppSetPicDescHeight(vpcOutputDesc_, dvppOutHeight);
    acldvppSetPicDescWidthStride(vpcOutputDesc_, dvppOutWidthStride);
    acldvppSetPicDescHeightStride(vpcOutputDesc_, dvppOutHeightStride);
    acldvppSetPicDescSize(vpcOutputDesc_, vpcOutBufferSize_);
}

// 8. 创建roiNums,每张图对应需要抠图和贴图的数量

uint32_t totalNum = 0;
std::unique_ptr<uint32_t[]> roiNums(new (std::nothrow) uint32_t[1]);
roiNums[0]=2;
// 11. 执行异步抠图贴图，再调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成
ret = acldvppVpcBatchCropAndPasteAsync(dvppChannelDesc_, vpcInputBatchDesc_, roiNums.get(), 1,
        vpcOutputBatchDesc_, cropAreas_, pasteAreas_, stream_);
ret = aclrtSynchronizeStream(stream_);

// 9. 抠图贴图结束后，释放资源，包括输入/输出图片的描述信息、输入/输出内存、通道描述信息、通道等
acldvppDestroyRoiConfig(cropAreas_[0]);
acldvppDestroyRoiConfig(cropAreas_[1]);
acldvppDestroyRoiConfig(pasteAreas_[0]);
acldvppDestroyRoiConfig(pasteAreas_[1]);
(void)acldvppFree(vpcInDevBuffer_);
for(uint32_t index=0; index<2; ++index){
if(runMode == ACL_HOST){ 
    // 该模式下，由于处理结果在Device侧，因此需要调用内存复制接口传输结果数据后，再释放Device侧内存
    // 申请Host内存vpcOutHostBuffer
    void* vpcOutHostBuffer = nullptr;
    vpcOutHostBuffer = malloc(vpcOutBufferSize_);
    // 通过aclrtMemcpy接口将Device的处理结果数据传输到Host
    ret = aclrtMemcpy(vpcOutHostBuffer, vpcOutBufferSize_, vpcOutBufferDev_, vpcOutBufferSize_, ACL_MEMCPY_DEVICE_TO_HOST);
    // 释放掉输入输出的device内存
    (void)acldvppFree(vpcOutBufferDev_);
    // 数据使用完成后，释放内存
    free(vpcOutHostBuffer);
} else { 
    // 此时运行在device侧，处理结果也在Device侧，可以根据需要操作处理结果后，释放Device侧内存
    
    (void)acldvppFree(vpcOutBufferDev_);
}
}
acldvppDestroyBatchPicDesc(vpcInputDesc_);
acldvppDestroyBatchPicDesc(vpcOutputDesc_);
acldvppDestroyChannel(dvppChannelDesc_);
(void)acldvppDestroyChannelDesc(dvppChannelDesc_);
dvppChannelDesc_ = nullptr;

....
```
