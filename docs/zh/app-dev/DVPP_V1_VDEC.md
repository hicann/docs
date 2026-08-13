# VDEC视频解码

本节介绍VDEC视频解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

VDEC（Video Decoder）负责将H264/H265格式的视频码流解码为YUV/RGB格式的图片。关于VDEC功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

**图 1**  视频解码流程  
![](figures/VDEC_API_call_process_V1.png "视频解码流程")

实现视频的解码，关键接口的说明如下：

1. **调用aclvdecCreateChannel接口创建视频解码处理的通道。**
    - 创建视频解码处理通道前，需先执行以下操作：
        1. 调用aclvdecCreateChannelDesc接口**创建通道描述信息**。
        2. 调用aclvdecSetChannelDesc系列接口**设置通道描述信息的属性**，包括**解码通道号、线程、回调函数、视频编码协议**等，其中：

            1. 回调函数需由用户提前创建，用于在视频解码后，获取解码数据，并及时释放相关资源，回调函数的原型请参见aclvdecCallback。

                在回调函数内，用户需调用acldvppGetPicDescRetCode接口获取retCode返回码判断是否解码成功，retCode为0表示解码成功，为1表示解码失败。如果解码失败，需要根据日志中的返回码判断具体的问题，返回码请参见[返回码说明](#section197765691414)。

                解码结束后，建议用户在回调函数内及时释放VDEC的输入码流内存、输出图片内存以及相应的视频码流描述信息、图片描述信息。

            2. 线程需由用户提前创建，并自定义线程函数，在线程函数内调用aclrtProcessReport接口，等待指定时间后，触发前一步中的回调函数。

            >**说明：** 
            >如果不调用aclvdecSetChannelDescOutPicFormat接口设置输出格式，则默认使用YUV420SP NV12。

    - aclvdecCreateChannel接口内部封装了如下接口，无需用户单独调用：
        1. aclrtCreateStream接口：显式创建Stream，VDEC内部使用。
        2. aclrtSubscribeReport接口：指定处理Stream上回调函数的线程，回调函数和线程是由用户调用aclvdecSetChannelDesc系列接口时指定的。

2. **调用aclvdecSendFrame接口将视频码流解码成YUV420SP格式的图片。**
    - **视频解码前，**需先执行以下操作：
        - 调用acldvppCreateStreamDesc接口创建输入视频码流描述信息，并调用acldvppSetStreamDesc系列接口设置输入视频的内存地址、内存大小、码流格式等属性。
        - 调用acldvppCreatePicDesc接口创建输出图片描述信息，并调用acldvppSetPicDesc系列接口设置输出图片的内存地址、内存大小、图片格式等属性。

    - **视频解码时：**

        aclvdecSendFrame接口内部封装了aclrtLaunchCallback接口，用于在Stream的任务队列中增加一个需要执行的回调函数。用户无需单独调用aclrtLaunchCallback接口。

    - **视频解码后**，视频解码的结果数据通过回调函数获取：

        获取解码数据前，先获取retCode的值，判断解码是否成功，0表示解码成功，1表示解码失败。如果解码失败，需要根据日志中的返回码判断具体的问题，返回码请参见[返回码说明](#section197765691414)。

        如果用户需要获取解码的帧序号，则可以在aclvdecSendFrame接口的userData参数处定义，然后解码的帧序号可以通过userData参数传递给VDEC的回调函数，用于确定回调函数中处理的是第几帧数据。

        如果不想获取某一帧的解码结果，可以调用aclvdecSendSkippedFrame接口，将待解码的码流（输入内存）传到解码器进行解码，此时，解码结果最终不会输出，解码完成的回调函数中返回的output为nullptr。

3. **调用aclvdecDestroyChannel接口销毁视频处理的通道。**
    - 系统会等待已发送帧解码完成且用户的回调函数处理完成后再销毁通道。
    - aclvdecDestroyChannel接口内部封装了如下接口，无需用户单独调用：
        - aclrtUnSubscribeReport接口：取消线程注册（Stream上的回调函数不再由指定线程处理）。
        - aclrtDestroyStream接口：销毁Stream。

    - 销毁通道后，需调用aclvdecDestroyChannelDesc接口销毁通道描述信息。
    - 销毁通道描述信息后，用户才可以销毁第1步中创建的线程。

## 示例代码

以下是VDEC视频解码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

您可以单击[vdec\_resnet50\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vdec_resnet50_classification)获取样例。

```cpp
// 1. 创建回调函数
void callback(acldvppStreamDesc *input, acldvppPicDesc *output, void *userdata)
{
    static int count = 1;
    if (output != nullptr) {
        // 获取VDEC解码的输出内存，调用自定义函数WriteToFile将输出内存中的数据写入文件后，再调用acldvppFree接口释放输出内存
        void *vdecOutBufferDev = acldvppGetPicDescData(output);
        if (vdecOutBufferDev != nullptr) {
            // 0: vdec success; others, vdec failed
            // retCode为0表示解码成功，为1表示解码失败
            int retCode = acldvppGetPicDescRetCode(output);
            if (retCode == 0) {
                // process task: write file
                uint32_t size = acldvppGetPicDescSize(output);
                std::string fileNameSave = "outdir/image" + std::to_string(count);
                // vdec输出结果在device侧，在WriteToFile方法中进行下述处理
                if (!Utils::WriteToFile(fileNameSave.c_str(), vdecOutBufferDev, size)) {
                    ERROR_LOG("write file failed.");
                }
            } else {
                ERROR_LOG("vdec decode frame failed.");
            }

            // free output vdecOutBufferDev
            aclError ret = acldvppFree(vdecOutBufferDev);
        }
        // 释放acldvppPicDesc类型的数据，表示解码后输出图片描述数据
        aclError ret = acldvppDestroyPicDesc(output);
    }

    // free input vdecInBufferDev and destroy stream desc
    if (input != nullptr) {
        void *vdecInBufferDev = acldvppGetStreamDescData(input);
        if (vdecInBufferDev != nullptr) {
            aclError ret = acldvppFree(vdecInBufferDev);
        }
        // 释放acldvppStreamDesc类型的数据，表示解码的输入码流描述数据
        aclError ret = acldvppDestroyStreamDesc(input);
    }

    INFO_LOG("callback success %d.", count);
    count++;
}

// 2. 创建视频码流处理通道时的通道描述信息，设置视频处理通道描述信息的属性，其中线程（threadId表示线程ID）、callback回调函数需要用户提前创建。
// vdecChannelDesc是aclvdecChannelDesc类型
vdecChannelDesc = aclvdecCreateChannelDesc();
aclError ret = aclvdecSetChannelDescChannelId(vdecChannelDesc, 10);
ret = aclvdecSetChannelDescThreadId(vdecChannelDesc, threadId);
ret = aclvdecSetChannelDescCallback(vdecChannelDesc, callback);
// 示例中使用的是H265_MAIN_LEVEL视频编码协议
ret = aclvdecSetChannelDescEnType(vdecChannelDesc, static_cast<acldvppStreamFormat>(H265_MAIN_LEVEL));
// 示例中使用的是PIXEL_FORMAT_YVU_SEMIPLANAR_420
ret = aclvdecSetChannelDescOutPicFormat(vdecChannelDesc, static_cast<acldvppPixelFormat>(PIXEL_FORMAT_YUV_SEMIPLANAR_420));

// 3. 创建视频码流处理的通道
ret = aclvdecCreateChannel(vdecChannelDesc);


// 4. 调用aclrtGetRunMode接口获取软件栈的运行模式，如果调用aclrtGetRunMode接口获取软件栈的运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将输入图片数据传输到Device，数据传输完成后，需及时释放内存；否则直接申请并使用Device的内存
aclrtRunMode runMode;
ret = aclrtGetRunMode(&runMode);

// 5. 按帧发送码流，并解码
count = 0;
while (count < 10) { // 假设码流有10帧数据，需要发送10次
    //  5.1 申请输入码流内存（区分运行状态），并读取一帧码流数据，inBufferSize为实际要读取的一帧码流的大小，需要用户按每一帧的实际码流大小进行赋值
    if (runMode == ACL_HOST){ 
        // 申请Host内存inputHostBuff
        void* inputHostBuff= nullptr;
        // inBufferSize为输入码流大小
        inputHostBuff= malloc(inBufferSize);
        // 将输入一帧码流读入内存中，该自定义函数ReadStreamFile由用户实现
        ReadStreamFile(picName, inputHostBuff, inBufferSize);
        // 申请Device内存inBufferDev
        ret = acldvppMalloc(&inBufferDev, inBufferSize);
        // 通过aclrtMemcpy接口将输入图片数据传输到Device
        ret = aclrtMemcpy(inBufferDev, inBufferSize, inputHostBuff, inBufferSize, ACL_MEMCPY_HOST_TO_DEVICE);
        // 数据传输完成后，及时释放Host内存
        free(inputHostBuff);
    } else {
        // 申请Device输入内存dataDev，inBufferSize为每帧输入码流大小
        ret = acldvppMalloc(&inBufferDev, inBufferSize);
        // 将输入一帧码流读入内存中，该自定义函数ReadStreamFile由用户实现
        ReadStreamFile(picName, inBufferDev, inBufferSize);
    }

    // 5.2 创建输入视频码流描述信息，设置码流信息的属性
    streamInputDesc = acldvppCreateStreamDesc(); 
    // inBufferDev表示Device存放输入视频数据的内存，inBufferSize表示内存大小  
    ret = acldvppSetStreamDescData(streamInputDesc, inBufferDev);
    ret = acldvppSetStreamDescSize(streamInputDesc, inBufferSize);

    // 5.3 申请Device内存picOutBufferDev，用于存放VDEC解码后的输出数据，size为解码后的图片大小，需根据图片格式以及对齐后的图片宽高计算出size大小，再赋值
    ret = acldvppMalloc(&picOutBufferDev, size);

    // 5.4 创建输出图片描述信息，设置图片描述信息的属性
    // picOutputDesc是acldvppPicDesc类型
    picOutputDesc = acldvppCreatePicDesc();
    ret = acldvppSetPicDescData(picOutputDesc, picOutBufferDev);
    ret = acldvppSetPicDescSize(picOutputDesc, size);
    ret = acldvppSetPicDescFormat(picOutputDesc, static_cast<acldvppPixelFormat>(PIXEL_FORMAT_YUV_SEMIPLANAR_420));

    // 5.5 执行视频码流解码，解码每帧数据后，系统自动调用callback回调函数将解码后的数据写入文件，再及时释放相关资源
    ret = aclvdecSendFrame(vdecChannelDesc, streamInputDesc, picOutputDesc, nullptr, nullptr);
    // ......
    count++;
    // 注意，aclvdecSendFrame为异步接口，输入内存(inBufferDev)，输出内存(picOutBufferDev),输入描述符(streamInputDesc),输出描述符(picOutputDesc)不能提前释放，都需要在回调函数中释放
}

// 6. 释放图片处理通道、图片描述信息
ret = aclvdecDestroyChannel(vdecChannelDesc);
aclvdecDestroyChannelDesc(vdecChannelDesc);

......
```

<a id="section197765691414"></a>

## 返回码说明

**表 1**  返回码列表

| 返回码 | 含义 | 可能原因及解决方法 |
| --- | --- | --- |
| AICPU_DVPP_KERNEL_STATE_SUCCESS = 0 | 解码成功。 | - |
| AICPU_DVPP_KERNEL_STATE_FAILED = 1 | 其它错误。 | - |
| AICPU_DVPP_KERNEL_STATE_DVPP_ERROR = 2 | 接口内部调用其它模块的接口失败。 | - |
| AICPU_DVPP_KERNEL_STATE_PARAM_INVALID = 3 | 参数校验失败。 | 请检查接口的参数是否符合接口要求。 |
| AICPU_DVPP_KERNEL_STATE_OUTPUT_SIZE_INVALID = 4 | 输出内存大小校验失败。 | 请检查输出内存大小是否符合接口要求。 |
| AICPU_DVPP_KERNEL_STATE_INTERNAL_ERROR = 5 | 系统内部错误。 | - |
| AICPU_DVPP_KERNEL_STATE_QUEUE_FULL = 6 | 系统内部队列满。 | - |
| AICPU_DVPP_KERNEL_STATE_QUEUE_EMPTY = 7 | 系统内部队列空。 | - |
| AICPU_DVPP_KERNEL_STATE_QUEUE_NOT_EXIST = 8 | 系统内部队列不存在。 | - |
| AICPU_DVPP_KERNEL_STATE_GET_CONTEXT_FAILED = 9 | 获取系统内部上下文失败。 | - |
| AICPU_DVPP_KERNEL_STATE_SUBMIT_EVENT_FAILED = 10 | 提交系统内部事件失败。 | - |
| AICPU_DVPP_KERNEL_STATE_MEMORY_FAILED = 11 | 系统内部申请内存失败。 | 请检查系统是否有可用内存。 |
| AICPU_DVPP_KERNEL_STATE_SEND_NOTIFY_FAILED = 12 | 发送系统内部通知失败。 | - |
| AICPU_DVPP_KERNEL_STATE_VPC_OPERATE_FAILED = 13 | 系统内部接口处理失败。 | - |
| AICPU_DVPP_KERNEL_STATE_CHANNEL_ABNORMAL = 14 | 当前通道异常。 | - |
| ERR_INVALID_STATE = 0x10001 | VDEC解码器状态异常错误。 | - |
| ERR_HARDWARE = 0x10002 | 硬件错误，包含解码器启动、执行、停止等异常。 | - |
| ERR_SCD_CUT_FAIL = 0x10003 | 将视频码流分解成多帧图片异常。 | 请检查输入的视频流数据是否正确。 |
| ERR_VDM_DECODE_FAIL = 0x10004 | 解码某一帧异常。 | 请检查输入的视频流数据是否正确。 |
| ERR_ALLOC_MEM_FAIL = 0x10005 | 内部申请内存失败。 | 请检查系统是否有可用内存，若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出。 |
| ERR_ALLOC_DYNAMIC_MEM_FAIL = 0x10006 | 包括输入视频分辨率超范围、内部动态申请内存失败等异常。 | 请检查输入视频流的分辨率、系统是否有可用内存，若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出。 |
| ERR_ALLOC_IN_OR_OUT_PORT_MEM_FAIL = 0x10007 | 系统内部申请VDEC的输入、输出buffer异常。 | 请检查系统是否有可用内存，若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出。 |
| ERR_BITSTREAM = 0x10008 | 码流错误（如语法解析失败、重发eos或首帧即发送eos）。 | 请检查输入的视频流数据是否正确。 |
| ERR_VIDEO_FORMAT = 0x10009 | 输入视频格式错误。 | 请检查输入视频的格式是否为H264或H265。 |
| ERR_IMAGE_FORMAT = 0x1000a | 输出格式配置错误。 | 请检查输出图像的格式是否为nv12或nv21。 |
| ERR_CALLBACK = 0x1000b | 回调函数为空。 | 请检查配置的回调函数是否为空。 |
| ERR_INPUT_BUFFER = 0x1000c | 输入内存为空。 | 请检查输入内存是否为空。 |
| ERR_INBUF_SIZE = 0x1000d | 输入内存大小<=0。 | 请检查输入内存大小是否小于等于0。 |
| ERR_THREAD_CREATE_FBD_FAIL = 0x1000e | 系统内部将解码结果通过回调函数返回给用户的线程异常。 | 请检查系统中资源（例如：线程、内存等）是否可用。 |
| ERR_CREATE_INSTANCE_FAIL = 0x1000f | 创建解码实例失败。 | - |
| ERR_INIT_DECODER_FAIL = 0x10010 | 初始化解码器失败，例如解码实例个数超出范围（最大16）。 | - |
| ERR_GET_CHANNEL_HANDLE_FAIL = 0x10011 | 系统内部获取某路视频流的解码句柄失败。 | - |
| ERR_COMPONENT_SET_FAIL = 0x10012 | 系统内部设置解码实例异常。 | 请检查解码的入参值是否正确，例如输入视频格式video_format、输出帧格式image_format等。 |
| ERR_COMPARE_NAME_FAIL = 0x10013 | 系统内部设置解码实例名称异常。 | 请检查解码的入参值是否正确，例如输入视频格式video_format、输出帧格式image_format等。 |
| ERR_OTHER = 0x10014 | 其它错误。 | - |
| ERR_DECODE_NOPIC = 0x20000 | 隔行码流场景下使用，隔行码流每帧发送两场，解码时其中一块无图像输出，属于正常现象，会返回该错误码；隔行码流的解码输出数据都在奇数场对应的输出buffer中。 | - |
| 0x20001 | 参考帧个数设置错误。 | 请检查码流实际参考帧个数与用户设置的参考帧个数是否一致。Atlas 推理系列产品，默认参考帧个数为8。 |
| 0x20002 | VDEC解码帧存大小设置错误。 | 请检查输入码流实际宽、高与用户设置的宽、高是否一致。 |
| 0xA0058001 | 无效的Device ID。 | 请检查Device ID。 |
| 0xA0058002 | 无效的channel ID。 | 请检查传入接口的通道号是否正确，或者检查通道总数是否达到上限。 |
| 0xA0058003 | 参数不合法，例如不合法的枚举值。 | 请根据日志检查出错的参数。 |
| 0xA0058004 | 资源已存在。 | 请检查是否重复创建通道。 |
| 0xA0058005 | 通道资源不存在。 | 请检查是否使用了不存在的通道号或通道句柄。 |
| 0xA0058006 | 函数参数中有空指针。 | 请根据日志检查接口的入参。 |
| 0xA0058007 | 启用系统、Device或通道前未配置对应的参数。 | 请根据日志检查接口的入参。 |
| 0xA0058008 | 不支持的参数或者功能。 | 请根据日志检查接口的入参。 |
| 0xA0058009 | 该操作不允许，如试图修改静态配置参数。 | - |
| 0xA005800C | 分配内存失败，如系统内存不足。 | 请检查系统是否有可用内存，若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出。 |
| 0xA005800D | 分配缓存失败，如申请的数据缓冲区太大。 | - |
| 0xA005800E | 缓冲区中无数据。 | 系统未完成解码，缓冲区中无解码结果数据，需等待缓冲区中有数据后，再尝试获取数据。 |
| 0xA005800F | 缓冲区中数据满。 | 用户发送输入码流数据的速度太快，导致输入缓冲区数据满，请尝试降低发送输入码流数据的速度，或者在创建通道时将缓冲区大小设置为较大值。 |
| 0xA0058010 | 系统没有初始化或者相关依赖的模块没有加载。 | 请检查是否调用系统初始化接口。 |
| 0xA0058011 | 地址错误。 | - |
| 0xA0058012 | 系统忙。 | 请检查VDEC解码总路数是否达到上限。 |
| 0xA0058013 | 缓存小于实际需要的大小。 | - |
| 0xA0058014 | 硬件或软件处理超时。 | - |
| 0xA0058015 | 内部系统错误。 | - |
| 0xA005803F | 最大的返回码，该模块的错误码必须小于该值。 | - |
