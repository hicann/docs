# An Error of Unsupported Image Format Is Reported During Video Decoding When the Output Image Description Type Is Reused

## Symptom

When  **aclvdecSendFrame**  is repeatedly called to decode each frame of a stream in the video and if an exception occurs on a frame, an error will be reported when decoding the next frame, and the application process exits.

According to logs on the host and device,  **the out format 0 is not supported**. The log segment is as follows:

- Device logs

```text
[ERROR] KERNEL(2234,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [klogd.c:246][652145.056916] [HiDvpp][A618] [Vdec]:vdec_check_resize_param [Line]:6768 pid 23973 usr chn 0 device 0 chn 0 the out format 0 is not supported.
```

- Host log

```text
[ERROR] RUNTIME(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:721]17184 rtStreamSynchronize:[DVPP][DEFAULT]ErrCode=507018, desc=[aicpu exception], InnerCode=0x715002a
[ERROR] RUNTIME(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]17184 FuncErrorReason:[DVPP][DEFAULT]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]17184 FuncErrorReason:[DVPP][DEFAULT]rtStreamSynchronize execute failed, reason=[aicpu exception]
[INFO] GE(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:252]17184 ReportInterErrMessage:report error_message, error_code:EE8888, work_stream_id:1717417184
[ERROR] ASCENDCL(17174,AIMCDemo):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [video_processor_v200.cpp:1089]17184 aclvdecSendFrame: [DVPP][DEFAULT][Sync][Stream]vdec fail to synchronize sendFrameStream, runtime errorCode = 507018, channelId = 0.
```

## Possible Cause

Check the application code. It is found that when each frame of a video stream is decoded repeatedly, the output image description type  **acldvppPicDesc**  of the  **aclvdecSendFrame**  API is reused. However, the  **format**,  **width**,  **height**,  **widthStride**, and  **heightStride**  of the output image are not reset before the next decoding. In this case, if the previous frame fails to be decoded, the  **format**,  **width**,  **height**,  **widthStride**, and  **heightStride**  of  **acldvppPicDesc**  will change to the default value  **0**, and the VDEC decodes and outputs the actual image width and height. However,  **format**  0 indicates the YUV400 format, which is not supported by VDEC. As a result, the parameters of the next frame are invalid and the decoding fails.

## Solution

The application code logic is optimized. When the output image description type  **acldvppPicDesc**  is reused,  **format**,  **width**,  **height**,  **widthStride**, and  **heightStride**  of the output image need to be reset before the next decoding.

**Compliant code snippet:**

```c
aclError ret;
int restLen = 10;
uint32_t inBufferSize = 0;
void *g_picOutBufferDev;
void *inBufferDev = nullptr;
acldvppPicDesc *picOutputDesc;
size_t dataSize = (INPUT_WIDTH * INPUT_HEIGHT * 3) / 2;

// Apply for a picOutputDesc, which is used by each frame.
picOutputDesc = acldvppCreatePicDesc();
// read file to device memory
ReadFileToDeviceMem(filePath.c_str(), inBufferDev, inBufferSize);
while (restLen > 0) {
        // Wait until the previous frame decoding ends, call picOutputDesc again, and reset format, width, height, widthStride, and heightStride for this frame.
        ret = acldvppSetPicDescFormat(picOutputDesc, static_cast<acldvppPixelFormat>(1)); // 1: YUV420 semi-planner(nv12)
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

**Non-compliant code snippet:**

```c
aclError ret;
int restLen = 10;
uint32_t inBufferSize = 0;
void *g_picOutBufferDev;
void *inBufferDev = nullptr;
acldvppPicDesc *picOutputDesc;
size_t dataSize = (INPUT_WIDTH * INPUT_HEIGHT * 3) / 2;

// Apply for a picOutputDesc, which is used by each frame, but the format, width, height, widthStride, and heightStride are not changed for each frame.
picOutputDesc = acldvppCreatePicDesc();
ret = acldvppSetPicDescFormat(picOutputDesc, static_cast<acldvppPixelFormat>(1)); // 1: YUV420 semi-planner(nv12)
ret = acldvppSetPicDescWidth(picOutputDesc, 1920);
ret = acldvppSetPicDescHeight(picOutputDesc, 1080);
ret = acldvppSetPicDescWidthStride(picOutputDesc, 1920);
ret = acldvppSetPicDescHeightStride(picOutputDesc, 1080);
// read file to device memory
ReadFileToDeviceMem(filePath.c_str(), inBufferDev, inBufferSize);
while (restLen > 0) {
        // Wait until the previous frame decoding ends, call picOutputDesc again, but the format, width, height, widthStride, and heightStride are not reset for this frame.
    // If the previous frame fails to be decoded, the values of format, width, height, widthStride, and heightStride of picOutputDesc_ are changed to the default value 0.
    // VDEC decodes and outputs the actual image width and height. However, format 0 indicates the YUV400 format, which is not supported by VDEC. As a result, the parameters of the next frame are invalid and the decoding fails.
        ret = acldvppMalloc(&g_picOutBufferDev, dataSize);
        ret = acldvppSetPicDescData(picOutputDesc, g_picOutBufferDev);
        ret = acldvppSetPicDescSize(picOutputDesc, dataSize);
        ret = aclvdecSendFrame(vdecChannelDesc, streamInputDesc, picOutputDesc, nullptr, nullptr);
        restLen = restLen - 1;
    }
```
