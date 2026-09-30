# JPEGD图像解码

本节介绍JPEGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

JPEGD（JPEG Decoder）负责完成图像解码功能，将.jpg、.jpeg、.JPG、.JPEG图片解码成YUV格式图片。关于JPEGD功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

**图 1**  JPEG图片解码  
![](figures/JPEGD_API_call_process_V1.png "JPEG图片解码")

当前系统支持.jpg、.jpeg、.JPG、.JPEG图片的解码，针对不同的源图编码格式，输出不同编码格式的图片，关键接口的说明如下：

1. 调用aclInit接口初始化系统。
2. 调用aclrtSetDevice接口指定计算设备。
3. 调用aclrtCreateStream接口创建Stream。
4. 调用acldvppCreateChannel接口**创建图片数据处理的通道**。

    创建图片数据处理的通道前，需先调用acldvppCreateChannelDesc接口创建通道描述信息。

5. 实现JPEG图片解码功能前，若需要**申请Device上的内存**存放输入或输出数据，需调用acldvppMalloc申请内存。

    在申请输出内存前，可根据存放JPEG图片数据的内存，调用acldvppJpegPredictDecSize接口预估JPEG图片解码后所需的输出内存的大小。

    实际输出内存大小可能与调用acldvppJpegPredictDecSize接口预估的内存大小存在差异，如果用户需要获取解码后的实际输出内存大小，需调用acldvppPicDesc类型下的acldvppGetPicDescSize接口获取。

6. 调用acldvppJpegDecodeAsync异步接口进行**解码**。

    对于异步接口，还需调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成。

7. 在解码结束后，需及时调用acldvppFree接口**释放输入、输出内存**。
8. 调用acldvppDestroyChannel接口**销毁图片数据处理的通道**。

    销毁图片数据处理的通道后，再调用acldvppDestroyChannelDesc接口销毁通道描述信息。

9. 调用aclrtDestroyStream接口销毁Stream。
10. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
11. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 示例代码

以下是JPEGD图片解码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

您可以单击[vpc\_jpeg\_resnet50\_imagenet\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)获取样例。

```cpp
// 1.创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型
dvppChannelDesc_ = acldvppCreateChannelDesc();

// 2.创建图片数据处理的通道。
aclError ret = acldvppCreateChannel(dvppChannelDesc_);

// 3. 申请输入内存（区分运行状态）
// 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);
if(runMode == ACL_HOST){
    // 申请Host内存inputHostBuff，并将输入图片读入该地址，inDevBufferSize为读入图片大小
    void* inputHostBuff = nullptr;
    inputHostBuff = malloc(inDevBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, inputHostBuff, inDevBufferSize);
    // 申请Device内存inDevBuffer_
    ret = acldvppMalloc(&inDevBuffer_, inDevBufferSize);
    // 通过aclrtMemcpy接口将输入图片数据传输到Device
    ret = aclrtMemcpy(inDevBuffer_, inDevBufferSize, inputHostBuff, inDevBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);

} else {
    // 申请Device输入内存inDevBuffer_
    ret = acldvppMalloc(&inDevBuffer_, inBufferSize);
    // 将输入图片读入内存中，该自定义函数ReadPicFile由用户实现
    ReadPicFile(picName, inDevBuffer_, inBufferSize);
}

// 4. 申请解码输出内存decodeOutDevBuffer_
// 预估JPEGD处理结果所需的内存大小
uint32_t decodeOutBufferSize = 0;
ret = acldvppJpegPredictDecSize(inputHostBuff, inDevBufferSize, PIXEL_FORMAT_YVU_SEMIPLANAR_420, &decodeOutBufferSize);
ret = acldvppMalloc(&decodeOutDevBuffer_, decodeOutBufferSize);
// 及时释放内存
free(inputHostBuff);

// 5. 创建解码输出图片的描述信息，设置各属性值
// decodeOutputDesc是acldvppPicDesc类型
decodeOutputDesc_ = acldvppCreatePicDesc();
acldvppSetPicDescData(decodeOutputDesc_, decodeOutDevBuffer_);
acldvppSetPicDescFormat(decodeOutputDesc_, PIXEL_FORMAT_YUV_SEMIPLANAR_420); 
acldvppSetPicDescWidth(decodeOutputDesc_, inputWidth_);
acldvppSetPicDescHeight(decodeOutputDesc_, inputHeight_);
acldvppSetPicDescWidthStride(decodeOutputDesc_, decodeOutWidthStride);
acldvppSetPicDescHeightStride(decodeOutputDesc_, decodeOutHeightStride);
acldvppSetPicDescSize(decodeOutputDesc_, decodeOutBufferSize);

// 6. 执行异步解码，再调用aclrtSynchronizeStream接口阻塞程序运行，直到指定Stream中的所有任务都完成
ret = acldvppJpegDecodeAsync(dvppChannelDesc_, inDevBuffer_, inDevBufferSize, decodeOutputDesc_, stream_);
ret = aclrtSynchronizeStream(stream_);

// 7. 解码结束后，释放资源，包括解码输出图片的描述信息、解码输出内存、通道描述信息、通道等
acldvppDestroyPicDesc(decodeOutputDesc_);

if(runMode == ACL_HOST){ 
    // 该模式下，由于处理结果在Device侧，因此需要调用内存复制接口传输结果数据后，再释放Device侧内存
    // 申请Host内存vpcOutHostBuffer
    void* vpcOutHostBuffer = nullptr;
    vpcOutHostBuffer = malloc(decodeOutBufferSize);
    // 通过aclrtMemcpy接口将Device的处理结果数据传输到Host
    ret = aclrtMemcpy(vpcOutHostBuffer, decodeOutBufferSize, decodeOutDevBuffer_, decodeOutBufferSize, ACL_MEMCPY_DEVICE_TO_HOST);
    // 释放掉输入输出的device内存
    (void)acldvppFree(inDevBuffer_);
    (void)acldvppFree(decodeOutDevBuffer_);
    // 数据使用完成后，释放内存
    free(vpcOutHostBuffer);
} else { 
    // 此时运行在device侧，处理结果也在Device侧，可以根据需要操作处理结果后，释放Device侧内存
    (void)acldvppFree(inDevBuffer_);
    (void)acldvppFree(decodeOutDevBuffer_);
}
acldvppDestroyChannel(dvppChannelDesc_);
(void)acldvppDestroyChannelDesc(dvppChannelDesc_);
dvppChannelDesc_ = nullptr;

....
```
