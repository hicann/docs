# VENC视频编码

VENC（Video Encoder）将YUV420SP格式的图片编码成H.264/H.265格式的视频码流。关于VENC功能的详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍VENC视频编码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程

开发应用时，如果涉及视频编码，则应用程序中必须包含视频编码的代码逻辑，**关于视频编码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明**。

**图 1**  视频编码流程
![](figures/VENC_API_call_process_V1.png "视频编码流程")

实现视频的编码，关键接口的说明如下：

1. **调用`acl.media.venc_create_channel`接口创建视频编码处理的通道。**
    - 创建视频编码处理通道前，需先执行以下操作：
        1. 调用`acl.media.venc_create_channel_desc`接口创建通道描述信息。
        2. 调用`acl.media.venc_set_channel_desc_param`接口设置通道描述信息的属性，包括线程、回调函数、视频编码协议、输入图片格式等，其中：

            1. 回调函数需由用户提前创建，用于在视频编码后，获取编码数据，并及时释放相关资源，回调函数的原型请参见`acl.media.venc_set_channel_desc_callback`。

                视频编码结束后，建议用户在回调函数内及时释放输入图片内存、以及相应的图片描述信息。视频编码的输出内存由系统管理，不由用户管理，因此无需用户释放。

            2. 线程需由用户提前创建，并自定义线程函数，在线程函数内调用`acl.rt.process_report`接口，等待指定时间后，触发前一步中的回调函数。

            >[!NOTE] 说明
            >推荐使用`acl.media.venc_set_channel_desc_param`接口设置通道描述信息的属性，通过枚举值来选择通过该接口设置某一个属性的值。
            >但为兼容旧版本，也可以调用acl.media.venc.set_channel_desc系列接口设置通道描述信息的属性，每个属性的设置对应一个set接口。

    - `acl.media.venc_create_channel`接口内部封装了如下接口，无需用户单独调用：
        1. `acl.rt.create_stream`接口：显式创建Stream，VENC内部使用。
        2. `acl.rt.subscribe_report`接口：指定处理Stream上回调函数的线程，回调函数和线程是由用户调用`acl.media.venc_set_channel_desc_param`接口时指定的。

2. **调用`acl.media.venc_send_frame`接口将YUV420SP格式的图片编码成H.264/H.265格式的视频码流。**
    - **视频编码前**，需先执行以下操作：
        - 调用`acl.media.dvpp_create_pic_desc`接口创建输入图片描述信息，并调用acl.media.dvpp_set_pic_desc系列接口设置输入图片的内存地址、内存大小、图片格式等属性。
        - 调用`acl.media.venc_create_frame_config`接口创建单帧编码配置数据，并调用acl.media.venc_set_frame_config系列接口设置是否强制重新开始I帧间隔、是否结束帧。

    - **视频编码时**，`acl.media.venc_send_frame`接口内部封装了`acl.rt.launch_callback`接口，用于在Stream的任务队列中增加一个需要执行的回调函数。用户无需单独调用`acl.rt.launch_callback`接口。
    - **视频编码后**，视频编码的结果数据通过回调函数获取。

3. **调用`acl.media.venc_destroy_channel`接口销毁视频处理的通道。**
    - 系统会等待已发送帧编码完成且用户的回调函数处理完成后再销毁通道。
    - `acl.media.venc_destroy_channel`接口内部封装了如下接口，无需用户单独调用。
        - `acl.rt.unsubscribe_report`接口：取消线程注册（Stream上的回调函数不再由指定线程处理）。
        - `acl.rt.destroy_stream`接口：销毁Stream。

    - 销毁通道后，需调用`acl.media.venc_destroy_channel_desc`接口销毁通道描述信息。
    - 销毁通道描述信息后，用户才可以销毁第一步中创建的线程。

## 示例代码

您可以从[样例介绍](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/0_data_process/venc_image)中获取完整样例代码。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.资源初始化:  创建 AclVenc 对象进行初始化。
# 1.1 初始化。
ret = acl.init()
# 1.2 运行管理资源申请。
# 调用acl.rt.get_run_mode接口获取软件栈的运行模式，根据运行模式来判断后续的内存申请接口调用逻辑。
runMode, ret = acl.rt.get_run_mode()

# 2.创建执行回调函数的线程及线程函数。
def cb_thread_func(self, args_list):
    ctx = args_list[0]
    timeout = args_list[1]
    print("[info] thread args_list = ", self.ctx, timeout, self.g_callbackRunFlag, "\n")
    ret = acl.rt.set_context(ctx)
    assert ret == 0

    while self.g_callbackRunFlag is True:
        print("[info] thread g_callbackRunFlag = ", self.g_callbackRunFlag, "\n")
        ret = acl.rt.process_report(timeout)
        print("[info] acl.rt.process_report =", ret)

timeout = 1000
g_callbackRunFlag = True
self.cb_thread_id, ret = acl.util.start_thread(self.cb_thread_func, [self.ctx, timeout])

# 3.创建回调函数。
# 3.1 获取流数据输出。
def get_stream_data(self, stream_desc):
    stream_data = acl.media.dvpp_get_stream_desc_data(stream_desc)
    assert stream_data is not None
    stream_data_size = acl.media.dvpp_get_stream_desc_size(stream_desc)
    print("[info] stream_data size", stream_data_size)
    # stream memcpy d2h
    np_data = np.zeros(stream_data_size, dtype=np.byte)

    bytes_data = np_data.tobytes()
    np_data_ptr = acl.util.bytes_to_ptr(bytes_data)
    ret = acl.rt.memcpy(np_data_ptr, stream_data_size,
                         stream_data, stream_data_size,
                         memcpy_kind.get("ACL_MEMCPY_DEVICE_TO_HOST"))
    assert ret == 0
    return np_data
# 3.2 回调函数将视频流保存文件。
def callback_func(self, input_pic_desc, output_stream_desc, user_data):
    # 获取视频编码结果数据, 转换成numpy对象。
    output_numpy = self.get_stream_data(output_stream_desc)
    with open('./data/output.h265', 'ab') as f:
        f.write(output_numpy)
    print("[INFO] [callback_func] stream size =", acl.media.dvpp_get_stream_desc_size(output_stream_desc))

# 4.创建视频编码处理通道时的通道描述信息。
self.venc_channel_desc = acl.media.venc_create_channel_desc()

# 5.设置通道描述信息的属性，其中线程、callback回调函数需要用户提前创建。
# venc_channel_desc是aclvencChannelDesc类型。
venc_format = 1
venc_entype = 0
input_width = 1280
input_height = 720
ret = acl.media.venc_set_channel_desc_thread_id(self.venc_channel_desc, self.cb_thread_id)
ret = acl.media.venc_set_channel_desc_callback(self.venc_channel_desc, self.callback_func)
ret = acl.media.venc_set_channel_desc_entype(self.venc_channel_desc, venc_entype)
ret = acl.media.venc_set_channel_desc_pic_format(self.venc_channel_desc, venc_format)
ret = acl.media.venc_set_channel_desc_key_frame_interval(self.venc_channel_desc, 16)
ret = acl.media.venc_set_channel_desc_pic_height(self.venc_channel_desc, input_height)
ret = acl.media.venc_set_channel_desc_pic_width(self.venc_channel_desc, input_width )

# 6.创建视频码流处理的通道、单帧编码配置数据。
ret = acl.media.venc_create_channel(self.venc_channel_desc)
# vencFrameConfig_是aclvencFrameConfig类型。
frame_config = acl.media.venc_create_frame_config()

# 7.申请Device内存dataDev，存放视频编码的输入数据。
# 7.1 读入图片数据。
output_pic_size = (input_width * input_height * 3) // 2
print("[INFO] output_pic_size:", output_pic_size, " load vdec file:", venc_file_path)
file_context = np.fromfile(venc_file_path, dtype=np.byte)
file_size = file_context.size
bytes_data = file_context.tobytes()
file_mem = acl.util.bytes_to_ptr(bytes_data)
input_size = file_size
# 如果调用acl.rt.get_run_mode接口获取软件栈的运行模式为ACL_HOST，则需要通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时调用acl.rt.free_host接口释放Host内存。
# 如果调用acl.rt.get_run_mode接口获取软件栈的运行模式为ACL_DEVICE，则直接申请Device内存，存放输入图片数据。
# 此处是运行模式为 ACL_HOST。
input_mem, ret = acl.media.dvpp_malloc(input_size)
assert ret == 0
ret = acl.rt.memcpy(input_mem, input_size, file_mem,
                     file_size, memcpy_kind.get("ACL_MEMCPY_HOST_TO_DEVICE"))
assert ret == 0

# 8.执行视频编码。
def venc_set_frame_config(self, frame_config, eos, iframe):
    ret = acl.media.venc_set_frame_config_eos(frame_config, eos)
    assert ret == 0
    ret = acl.media.venc_set_frame_config_force_i_frame(frame_config, iframe)
    assert ret == 0

def venc_process(self, venc_channel_desc, input_mem, input_size, frame_config):
   # 设置为非结束帧。
    self.venc_set_frame_config(frame_config, 0, 0)
    print("[INFO] set frame config")
    self.test_get_frame_config(frame_config)

    # set picture description
    dvpp_pic_desc = acl.media.dvpp_create_pic_desc()
    assert dvpp_pic_desc is not None
    ret = acl.media.dvpp_set_pic_desc_data(dvpp_pic_desc, input_mem)
    assert ret == 0
    ret = acl.media.dvpp_set_pic_desc_size(dvpp_pic_desc, input_size)
    assert ret == 0
    print("[INFO] set pic desc")

    # 发送1张图片到编码器进行编码。
    venc_cnt = 16
    while venc_cnt:
        ret = acl.media.venc_send_frame(venc_channel_desc, dvpp_pic_desc, 0, frame_config, 0)
        assert ret == 0
        print("[INFO] venc send frame")
        venc_cnt -= 1
    # 结束视频编码时可以发送eos为1的空图片，表示当前编码结束。
    self.venc_set_frame_config(frame_config, 1, 0)
    ret = acl.media.venc_send_frame(venc_channel_desc, 0, 0, frame_config, 0)
    assert ret == 0

# 9.释放资源。
ret = acl.media.dvpp_free(input_mem)
ret = acl.media.venc_destroy_frame_config(frame_config)
assert ret == 0
print("[INFO] free resources")
g_callbackRunFlag = False
ret = acl.util.stop_thread(self.cb_thread_id)
print("[INFO] thread join")

# 10. 释放运行管理资源。
# 去初始化。
ret = acl.finalize()
# ....
```

如果调用`acl.media.venc_set_channel_desc_param`接口设置通道描述信息的属性，调用`acl.media.venc_get_channel_desc_param`接口获取通道描述信息中的属性值，示例代码如下：

```bash
ACL_VENC_THREAD_ID_UINT64 = 0          #回调线程ID。
ACL_VENC_CALLBACK_PTR = 1              #回调函数。
ACL_VENC_PIXEL_FORMAT_UINT32 = 2       #输入图像格式。
ACL_VENC_ENCODE_TYPE_UINT32 = 3        #视频编码协议。
ACL_VENC_PIC_WIDTH_UINT32 = 4          #输入图片宽度。
ACL_VENC_PIC_HEIGHT_UINT32 = 5         #输入图片高度。
ACL_VENC_KEY_FRAME_INTERVAL_UINT32 = 6 #关键帧间隔。
ACL_VENC_BUF_ADDR_PTR = 7              #编码输出缓存地址。
ACL_VENC_BUF_SIZE_UINT32 = 8           #编码输出缓存大小。
ACL_VENC_RC_MODE_UINT32 = 9            #码率控制模式。
ACL_VENC_SRC_RATE_UINT32 = 10          #输入码流帧率。
ACL_VENC_MAX_BITRATE_UINT32 = 11       #输出码率。
ACL_VENC_MAX_IP_PROP_UINT32 = 12       #一个GOP内单个I帧bit数和单个P帧bit数的比例。

# 设置回调函数。
ret = acl.media.venc_set_channel_desc_param(self.venc_channel_desc, ACL_VENC_CALLBACK_PTR, self.callback_func)
# 获取回调函数。
get_cb_func, ret = acl.media.venc_get_channel_desc_param(self.venc_channel_desc, ACL_VENC_CALLBACK_PTR)

PIXEL_FORMAT_YUV_SEMIPLANAR_420 = 1
# 设置输入图片格式。
ret = acl.media.venc_set_channel_desc_param(self.venc_channel_desc, ACL_VENC_PIXEL_FORMAT_UINT32, PIXEL_FORMAT_YUV_SEMIPLANAR_420)
# 获取输入图片格式。
get_pic_format, ret = acl.media.venc_get_channel_desc_param(self.venc_channel_desc, ACL_VENC_PIXEL_FORMAT_UINT32)

width = 128
# 设置图片宽度。
ret = acl.media.venc_set_channel_desc_param(self.venc_channel_desc, ACL_VENC_PIC_WIDTH_UINT32, width)
# 获取图片宽度。
get_width, ret = acl.media.venc_get_channel_desc_param(self.venc_channel_desc, ACL_VENC_PIC_WIDTH_UINT32)

height = 128
# 设置图片高度。
ret = acl.media.venc_set_channel_desc_param(self.venc_channel_desc, ACL_VENC_PIC_HEIGHT_UINT32, height)
# 获取图片高度。
get_height, ret = acl.media.venc_get_channel_desc_param(self.venc_channel_desc, ACL_VENC_PIC_HEIGHT_UINT32)
```
