# 复用输出图片描述类型，VDEC视频解码报错，提示有不支持的图片格式

## 问题现象描述

循环调用aclvdecSendFrame接口解码视频中的每一帧码流时，在遇到异常帧之后，解码下一帧就会报错，退出应用进程。

分别查看Host日志、Device日志，发现Device日志中提示**the out format 0 is not supported**，日志片段如下：

- Device日志：

```bash
[ERROR] KERNEL(2234,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [klogd.c:246][652145.056916] [HiDvpp][A618] [Vdec]:vdec_check_resize_param [Line]:6768 pid 23973 usr chn 0 device 0 chn 0 the out format 0 is not supported. 
```

- Host日志：

```bash
[ERROR] RUNTIME(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:721]17184 rtStreamSynchronize:[DVPP][DEFAULT]ErrCode=507018, desc=[aicpu exception], InnerCode=0x715002a
[ERROR] RUNTIME(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]17184 FuncErrorReason:[DVPP][DEFAULT]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]17184 FuncErrorReason:[DVPP][DEFAULT]rtStreamSynchronize execute failed, reason=[aicpu exception]
[INFO] GE(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:252]17184 ReportInterErrMessage:report error_message, error_code:EE8888, work_stream_id:1717417184
[ERROR] ASCENDCL(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [video_processor_v200.cpp:1089]17184 aclvdecSendFrame: [DVPP][DEFAULT][Sync][Stream]vdec fail to synchronize sendFrameStream, runtime errorCode = 507018, channelId = 0.
```

## 原因分析

检查应用代码，发现循环解码视频中的每一帧码流时，复用aclvdecSendFrame接口的输出图片描述类型acldvppPicDesc，但在下一次解码前没有重新设置输出图片format、width、height、widthStride、heightStride，这时，如果前一帧解码失败，acldvppPicDesc的参数format、width、height、widthStride、heightStride变成默认值0，width、height、widthStride、heightStride为0时，vdec会以实际图片宽高解码输出，但format为0，表示YUV400格式，vdec不支持解码输出该格式，会导致下一帧参数不合法解码失败。

## 解决方法

优化应用代码逻辑，复用输出图片描述类型acldvppPicDesc时，在下一次解码前需重新设置输出图片format、width、height、widthStride、heightStride。

**正例代码片段：**

```c
aclError ret;
int restLen = 10;
uint32_t inBufferSize = 0;
void *g_picOutBufferDev;
void *inBufferDev = nullptr;
acldvppPicDesc *picOutputDesc;
size_t dataSize = (INPUT_WIDTH * INPUT_HEIGHT * 3) / 2;

// 申请一个picOutputDesc,每帧复用
picOutputDesc = acldvppCreatePicDesc();
// read file to device memory
ReadFileToDeviceMem(filePath.c_str(), inBufferDev, inBufferSize);
while (restLen > 0) {
        // 等待前一个使用picOutputDesc解码帧结束，重新复用picOutputDesc,并针对这一帧重新设置Format、width、height、widthStride、heightStride参数值
        ret = acldvppSetPicDescFormat(picOutputDesc, static_cast<acldvppPixelFormat>(1)); // 1：YUV420 semi-planner（nv12）
        ret = acldvppSetPicDescWidth(picOutputDesc, 1920);
        ret = acldvppSetPicDescHeight(picOutputDesc, 1080);
        ret = acldvppSetPicDescWidthStride(picOutputDesc, 1920);
        ret = acldvppSetPicDescHeightStride(picOutputDesc, 1080);
        ret = acldvppMalloc(&g_picOutBufferDev, dataSize);
        ret = acldvppSetPicDescData(picOutputDesc, g_picOutBufferDev);
        ret = acldvppSetPicDescSize(picOutputDesc, dataSize);
        ret = aclvdecSendFrame(vdecChannelDesc, streamInputDesc, picOutputDesc, nullptr, nullptr);
        restLen = restLen - 1;
}
```

**反例代码片段：**

```c
aclError ret;
int restLen = 10;
uint32_t inBufferSize = 0;
void *g_picOutBufferDev;
void *inBufferDev = nullptr;
acldvppPicDesc *picOutputDesc;
size_t dataSize = (INPUT_WIDTH * INPUT_HEIGHT * 3) / 2;

// 申请一个picOutputDesc，每帧复用，且对Format、width、height、widthStride、heightStride参数值只设置了一次
picOutputDesc = acldvppCreatePicDesc();
ret = acldvppSetPicDescFormat(picOutputDesc, static_cast<acldvppPixelFormat>(1)); // 1：YUV420 semi-planner（nv12）
ret = acldvppSetPicDescWidth(picOutputDesc, 1920);
ret = acldvppSetPicDescHeight(picOutputDesc, 1080);
ret = acldvppSetPicDescWidthStride(picOutputDesc, 1920);
ret = acldvppSetPicDescHeightStride(picOutputDesc, 1080);
// read file to device memory
ReadFileToDeviceMem(filePath.c_str(), inBufferDev, inBufferSize);
while (restLen > 0) {
        // 等待前一个使用picOutputDesc解码帧结束，重新复用picOutputDesc,但没有重新设置Format、width、height、widthStride、heightStride参数值
    // 如果前一帧解码失败，picOutputDesc_的参数Format、width、height、widthStride、heightStride变成默认值0，
    // width、height、widthStride、heightStride为0时，vdec会以实际图片宽高解码输出，但Format为0，表示YUV400格式，vdec不支持解码输出该格式，会导致本帧参数不合法解码失败
        ret = acldvppMalloc(&g_picOutBufferDev, dataSize);
        ret = acldvppSetPicDescData(picOutputDesc, g_picOutBufferDev);
        ret = acldvppSetPicDescSize(picOutputDesc, dataSize);
        ret = aclvdecSendFrame(vdecChannelDesc, streamInputDesc, picOutputDesc, nullptr, nullptr);
        restLen = restLen - 1;
    }
```
