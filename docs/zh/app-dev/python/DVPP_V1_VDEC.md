# VDEC视频解码

VDEC（Video Decoder）负责将H.264/H.265格式的视频码流解码为YUV/RGB格式的图片。关于VDEC功能的详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍VDEC视频解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程

开发应用时，如果涉及视频解码，则应用程序中必须包含视频解码的代码逻辑，**关于视频解码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明**。

**图 1**  视频解码流程
![](figures/VDEC_API_call_process_V1.png "视频解码流程")

实现视频的解码，关键接口的说明如下：

1. **调用`acl.media.vdec_create_channel`接口创建视频解码处理的通道。**
    - 创建视频解码处理通道前，需先执行以下操作：
        1. 调用`acl.media.vdec_create_channel_desc`接口**创建通道描述信息**。
        2. 调用acl.media.vdec_set_channel_desc系列接口**设置通道描述信息的属性，包括解码通道号、线程、回调函数、视频编码协议**等，其中：

            1. 回调函数需由用户提前创建，用于在视频解码后，获取解码数据，并及时释放相关资源，回调函数的原型请参见`acl.media.vdec_set_channel_desc_callback`。

                在回调函数内，用户需调用`acl.media.dvpp_get_pic_desc_ret_code`接口获取“ret_code”返回码判断是否解码成功，“ret_code”为“0”表示解码成功，为“1”表示解码失败。如果解码失败，需要根据日志中的返回码判断具体的问题，返回码请参见[返回码说明](#返回码说明)。

                解码结束后，建议用户在回调函数内及时释放VDEC的输入码流内存、输出图片内存以及相应的视频码流描述信息、图片描述信息。

            2. 线程需由用户提前创建，并自定义线程函数，在线程函数内调用`acl.rt.process_report`接口，等待指定时间后，触发前一步中的回调函数。

            >[!NOTE] 说明
            >如果不调用`acl.media.vdec_set_channel_desc_out_pic_format`接口设置输出格式，则默认使用“YUV420SP NV12”。

    - `acl.media.vdec_create_channel`接口内部封装了如下接口，无需用户单独调用：
        1. `acl.rt.create_stream`接口：显式创建Stream，VDEC内部使用。
        2. `acl.rt.subscribe_report`接口：指定处理Stream上回调函数的线程，回调函数和线程是由用户调用acl.media.vdec_set_channel_desc系列接口时指定的。

2. **调用`acl.media.vdec_send_frame`接口将视频码流解码成YUV420SP格式的图片。**
    - **视频解码前**，需先执行以下操作：
        - 调用`acl.media.dvpp_create_stream_desc`接口创建输入视频码流描述信息，并调用acl.media.dvpp_set_stream_desc系列接口设置输入视频的内存地址、内存大小、码流格式等属性。
        - 调用`acl.media.dvpp_create_pic_desc`接口创建输出图片描述信息，并调用acl.media.dvpp_set_pic_desc系列接口设置输出图片的内存地址、内存大小、图片格式等属性。

    - **视频解码时：**

        `acl.media.vdec_send_frame`接口内部封装了`acl.rt.launch_callback`接口，用于在Stream的任务队列中增加一个需要执行的回调函数。用户无需单独调用acl.rt.launch_callback接口。

    - **视频解码后**，视频解码的结果数据通过回调函数获取：

        获取解码数据前，先获取“ret_code”的值，判断解码是否成功，0表示解码成功，1表示解码失败。如果解码失败，需要根据日志中的返回码判断具体的问题，返回码请参见[返回码说明](#返回码说明)。

        如果用户需要获取解码的帧序号，则可以在`acl.media.vdec_send_frame`接口的“user_data”参数处定义，然后解码的帧序号可以通过“user_data”参数传递给VDEC的回调函数，用于确定回调函数中处理的是第几帧数据。

        如果不想获取某一帧的解码结果，可以调用`acl.media.vdec_send_skipped_frame`接口，将待解码的码流（输入内存）传到解码器进行解码，此时，解码结果最终不会输出，解码完成的回调函数中返回的“dvpp_pic_desc”为0。

3. **调用`acl.media.vdec_destroy_channel`接口销毁视频处理的通道。**
    - 系统会等待已发送帧解码完成且用户的回调函数处理完成后再销毁通道。
    - `acl.media.vdec_destroy_channel`接口内部封装了如下接口，无需用户单独调用。
        - `acl.rt.unsubscribe_report`接口：取消线程注册（Stream上的回调函数不再由指定线程处理）。
        - `acl.rt.destroy_stream`接口：销毁Stream。

    - 销毁通道后，需调用`acl.media.vdec_destroy_channel_desc`接口销毁通道描述信息。
    - 销毁通道描述信息后，用户才可以销毁第一步中创建的线程。

## 示例代码

您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vdec_resnet50_classification)中获取完整样例代码。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行管理资源申请。
# 3.创建回调函数。
def _callback(self, input_stream_desc, output_pic_desc, user_data):
    # 输入码流描述。
    if input_stream_desc:
        ret = acl.media.dvpp_destroy_stream_desc(input_stream_desc)
        if ret != 0:
            print("acl.media.dvpp_destroy_stream_desc failed")
    # 输出图片描述。
    if output_pic_desc:
        vdec_out_buffer = acl.media.dvpp_get_pic_desc_data(output_pic_desc)
        ret_code = acl.media.dvpp_get_pic_desc_ret_code(output_pic_desc)
        data_size = acl.media.dvpp_get_pic_desc_size(output_pic_desc)
        self.images_buffer.append(dict({"buffer": vdec_out_buffer,
                                        "size": data_size}))
        ret = acl.media.dvpp_destroy_pic_desc(output_pic_desc)
        if ret != 0:
            print("acl.media.dvpp_destroy_pic_desc failed")
    self.output_count += 1
    print("[Vdec] [_callback] _callback exit success")
    # 在此样例中，释放vdec_out_buffer在vdec流程之后处理。

# 4.创建回调处理线程，并提交注册由此线程执行回调函数。
timeout = 100
cb_thread_id, ret = acl.util.start_thread(self._thread_func, [timeout])
acl.rt.subscribe_report(cb_thread_id, self.stream)

# 5.创建视频码流处理通道时的通道描述信息，设置视频处理通道描述信息的属性，其中线程、callback回调函数需要用户提前创建。
def init_resource(self, cb_thread_id):
    print("[Vdec] class Vdec init resource stage:")
    self.vdec_channel_desc = acl.media.vdec_create_channel_desc()
    acl.media.vdec_set_channel_desc_channel_id(self.vdec_channel_desc, self._channel_id)
    acl.media.vdec_set_channel_desc_thread_id(self.vdec_channel_desc, cb_thread_id)
    acl.media.vdec_set_channel_desc_callback(self.vdec_channel_desc, self._callback)
    acl.media.vdec_set_channel_desc_entype(self.vdec_channel_desc, self._en_type)
    acl.media.vdec_set_channel_desc_out_pic_format(self.vdec_channel_desc, self._format)
    print("[Vdec] class Vdec init resource stage success")

# 6.创建视频码流处理的通道。
ret = acl.media.vdec_create_channel(self.vdec_channel_desc)
# ......
# 7.申请Device内存dataDev，存放视频解码的输入视频数据。
# 将通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时调用acl.rt.free_host接口释放Host内存。
# 输出图片尺寸对齐方式设置。
output_pic_size = (self.input_width * self.input_height * 3) // 2
img = np.fromfile(img_path, dtype=self.dtype)
input_stream_size = img.size
bytes_data = img.tobytes()
img_ptr = acl.util.bytes_to_ptr(bytes_data)
self.input_stream_mem, ret = acl.media.dvpp_malloc(input_stream_size)
ret = acl.rt.memcpy(self.input_stream_mem,
                    input_stream_size,
                    img_ptr,
                    input_stream_size,
                    ACL_MEMCPY_HOST_TO_DEVICE)

# 8.循环10次执行视频解码，输出10张YUV420SP NV12格式的图片。
def forward(self, output_pic_size, input_stream_size):
    self.frame_config = acl.media.vdec_create_frame_config()
    for i in range(self.rest_len):
        print("[Vdec] forward index:{}".format(i))
        # 8.1 创建输入视频码流描述信息，设置码流信息的属性。
        self.dvpp_stream_desc = acl.media.dvpp_create_stream_desc()
        ret = acl.media.dvpp_set_stream_desc_data(self.dvpp_stream_desc, self.input_stream_mem)
        ret = acl.media.dvpp_set_stream_desc_size(self.dvpp_stream_desc, input_stream_size)
        # 8.2 创建输出图片描述信息，设置图片描述信息的属性。
        output_pic_mem, ret = acl.media.dvpp_malloc(output_pic_size)
        self.dvpp_pic_desc = acl.media.dvpp_create_pic_desc()
        acl.media.dvpp_set_pic_desc_data(self.dvpp_pic_desc, output_pic_mem)
        acl.media.dvpp_set_pic_desc_size(self.dvpp_pic_desc, output_pic_size)
        acl.media.dvpp_set_pic_desc_format(self.dvpp_pic_desc, PIXEL_FORMAT_YVU_SEMIPLANAR_420)
        # 8.3 执行视频码流解码，解码每帧数据后，系统自动调用callback回调函数将解码后的数据写入文件，再及时释放相关资源。
        ret = acl.media.vdec_send_frame(self.vdec_channel_desc,
                                        self.dvpp_stream_desc,
                                        self.dvpp_pic_desc,
                                        self.frame_config,
                                        None)
        check_ret("acl.media.vdec_send_frame", ret)
        print('[Vdec] vdec_send_frame stage success')

# 9.释放图片处理通道、图片描述信息。
ret = acl.media.vdec_destroy_channel(self.vdec_channel_desc)
acl.media.vdec_destroy_channel_desc(self.vdec_channel_desc)

# 10. 释放运行管理资源。
# 去初始化。
ret = acl.finalize()
# ....
```

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
| AICPU_DVPP_KERNEL_STATE_GET_CONTEX_FAILED = 9 | 获取系统内部上下文失败。 | - |
| AICPU_DVPP_KERNEL_STATE_SUBMIT_EVENT_FAILED = 10 | 提交系统内部事件失败。 | - |
| AICPU_DVPP_KERNEL_STATE_MEMORY_FAILED = 11 | 系统内部申请内存失败。 | 请检查系统是否有可用内存。 |
| AICPU_DVPP_KERNEL_STATE_SEND_NOTIFY_FAILED = 12 | 发送系统内部通知失败。 | - |
| AICPU_DVPP_KERNEL_STATE_VPC_OPERATE_FAILED = 13 | 系统内部接口处理失败。 | - |
| AICPU_DVPP_KERNEL_STATE_CHANNEL_ABNORMAL = 14 | 当前通道异常。 | - |
| ERR_INVALID_STATE = 0x10001 | VDEC解码器状态异常错误。 | - |
| ERR_HARDWARE = 0x10002 | 硬件错误，包含解码器启动、执行、停止等异常。 | - |
| ERR_SCD_CUT_FAIL = 0x10003 | 将视频码流分解成多帧图片异常。 | 请检查输入的视频流数据是否正确。 |
| ERR_VDM_DECODE_FAIL = 0x10004 | 解码某一帧异常。 | 请检查输入的视频流数据是否正确。 |
| ERR_ALLOC_MEM_FAIL = 0x10005 | 内部申请内存失败。 | 请检查系统是否有可用内存，**若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出**。 |
| ERR_ALLOC_DYNAMIC_MEM_FAIL = 0x10006 | 包括输入视频分辨率超范围、内部动态申请内存失败等异常。 | 请检查输入视频流的分辨率、系统是否有可用内存，**若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出**。 |
| ERR_ALLOC_IN_OR_OUT_PORT_MEM_FAIL = 0x10007 | 系统内部申请VDEC的输入、输出buffer异常。 | 请检查系统是否有可用内存，**若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出**。 |
| ERR_BITSTREAM = 0x10008 | 码流错误（如语法解析失败、重发eos或首帧即发送eos）。 | 请检查输入的视频流数据是否正确。 |
| ERR_VIDEO_FORMAT = 0x10009 | 输入视频格式错误。 | 请检查输入视频的格式是否为h264或h265。 |
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
| 0x20001 | 参考帧个数设置错误。 | 请检查码流实际参考帧个数与用户设置的参考帧个数是否一致。Atlas推理系列产品，默认参考帧个数为8。 |
| 0x20002 | VDEC解码帧存大小设置错误。 | 请检查输入码流实际宽、高与用户设置的宽、高是否一致。 |
| 0xA0058001 | 无效的Device ID。 | 请检查Device ID。 |
| 0xA0058002 | 无效的channel ID。 | 请检查传入接口的通道号是否正确，或者检查通道总数是否达到上限。 |
| 0xA0058003 | 参数不合法，例如不合法的枚举值。 | 请根据日志检查出错的参数。 |
| 0xA0058004 | 资源已存在。 | 请检查是否重复创建通道。 |
| 0xA0058005 | 通道资源不存在。 | 请检查是否使用了不存在的通道号或通道句柄。 |
| 0xA0058006 | 函数参数中有空指针。 | 请根据日志检查接口的入参。 |
| 0xA0058007 | 使能系统、Device或通道前未配置对应的参数。 | 请根据日志检查接口的入参。 |
| 0xA0058008 | 不支持的参数或者功能。 | 请根据日志检查接口的入参。 |
| 0xA0058009 | 该操作不允许，如试图修改静态配置参数。 | - |
| 0xA005800C | 分配内存失败，如系统内存不足。 | 请检查系统是否有可用内存，**若忽略错误，则可能导致用户持续送入码流却无任何解码结果输出**。 |
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
