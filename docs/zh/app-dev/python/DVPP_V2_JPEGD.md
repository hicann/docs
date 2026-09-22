<!-- npu="910b,910,310p,310b" id1 -->
# JPEGD图片解码

JPEGD（JPEG Decoder）负责完成图像解码功能，将.jpg、.jpeg、.JPG、.JPEG图片解码成YUV格式图片。关于JPEGD功能的详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍JPEGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程

开发应用时，如果涉及对JPEG图片的解码，则应用程序中必须包含解码的代码逻辑，关于图片解码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。

**图 1**  接口调用的流程
![](figures/JPEGD_API_call_process_V2.png "接口调用的流程")

当前系统支持解码JPEG图片，关键接口的说明如下：

1. 调用`acl.himpi.sys_init`接口进行媒体数据处理系统初始化。
2. 调用`acl.himpi.vdec_create_chn`接口创建通道。
3. 调用`acl.himpi.dvpp_malloc`接口申请Device上的内存，存放输入或输出数据。
    <!-- npu="910b,310b" id2 -->
    接口申请的内存为媒体数据处理的专用内存，但专用内存的地址空间有限，若关注内存规划或内存资源有限时，建议调用`acl.rt.malloc`接口申请内存。
    <!-- end id2 -->
4. 解码前，需调用`acl.himpi.vdec_start_recv_stream`接口通知解码器启动接收码流，再调用`acl.himpi.vdec_send_stream`接口发送解码码流，`acl.himpi.vdec_send_stream`接口是异步接口，调用该接口仅表示任务下发成功，还需要调用`acl.himpi.vdec_get_frame`接口获取解码结果数据，成功获取解码数据后，可以调用`acl.himpi.vdec_release_frame`接口释放帧相关的资源。

    解码结束后，需调用`acl.himpi.vdec_stop_recv_stream`接口通知解码器停止接收码流。

5. 调用`acl.himpi.dvpp_free`接口释放输入、输出内存。
    <!-- npu="310b" id3 -->
    Atlas 200I/500 A2推理产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id3 -->
    <!-- npu="910b" id4 -->
    Atlas A2系列产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id4 -->

6. 调用`acl.himpi.vdec_destroy_chn`接口销毁通道。
7. 调用`acl.himpi.sys_exit`接口进行媒体数据处理系统去初始化。

## 示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
# 1.获取软件栈的运行模式，不同运行模式影响后续的接口调用流程（例如是否进行数据传输等）。
run_mode, ret = acl.rt.get_run_mode()

# 2.初始化。
ret = acl.init()

# 3.运行时资源申请。
# 4.初始化媒体数据处理系统。
ret = acl.himpi.sys_init()

# 5.创建通道。
channel_id = 0
attr = {'type': HI_PT_JPEG, 'mode': HI_VDEC_SEND_MODE_FRAME,
        'pic_width': 1920, 'pic_height': 1080,
        'stream_buf_size': 1920 * 1080, 'frame_buf_size': 0,
        'frame_buf_cnt': 9}

ret = acl.himpi.vdec_create_chn(channel_id, attr)
# 6.设置通道属性。
jpegd_param_dict, ret = acl.himpi.vdec_get_chn_param(channel_id)
jpegd_param_dict["pic_param"]["pixel_format"] = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420
jpegd_param_dict["pic_param"]["alpha"] = 255
jpegd_param_dict["display_frame_num"] = 0
ret = acl.himpi.vdec_set_chn_param(channel_id, jpegd_param_dict)

# 7.解码器启动接收码流。
ret = acl.himpi.vdec_start_recv_stream(channel_id)

# 8.发送码流。
# 8.1 申请输入内存。
# input_size表示输入图片占用的内存大小，此处以1024 Byte为例，用户需根据实际情况计算内存大小。
input_size = 1024
input_addr, ret = acl.himpi.dvpp_malloc(0, input_size)

#如果运行模式为ACL_HOST，则需要申请Host内存，将输入图片数据读入Host内存，再通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时释放Host内存；否则直接将输入图片数据读入Device内存。
#直接将输入图片数据读入Device内存。
if run_mode == ACL_HOST:
    # 申请Host内存。
    input_buffer, ret= acl.rt.malloc_host(input_size)
    # 将输入图片读入内存中。
    vdec_file = np.fromfile(vdec_file_path, dtype=np.byte)
    vdec_file_size = vdec_file.itemsize * vdec_file.size

    bytes_data = vdec_file.tobytes()
    vdec_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, vdec_file_ptr, vdec_file_size, ACL_MEMCPY_HOST_TO_DEVICE)
else:
    # 将输入图片读入内存中。
    vdec_file = np.fromfile(vdec_file_path, dtype=np.byte)
    vdec_file_size = vdec_file.itemsize * vdec_file.size

    bytes_data = vdec_file.tobytes()
    vdec_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, vdec_file_ptr, vdec_file_size, ACL_MEMCPY_DEVICE_TO_DEVICE)

# 8.2 构造存放输入图片信息的字典。
stream = {'end_of_frame': HI_TRUE, 'end_of_stream': HI_FALSE,
          'need_display': HI_TRUE, 'pts': 0,
          'len': input_size, 'addr': vdec_file_ptr}
img_info, ret = acl.himpi.dvpp_get_image_info(HI_PT_JPEG, stream)
if run_mode == ACL_HOST:
    # 如果不使用Host上的数据，需及时释放。
    ret = acl.rt.free_host(input_buffer)

stream['addr'] =  input_addr

# 8.3 构造存放输出图片信息的字典，并申请输出内存。
out_pic_info = {"width": img_info['width'],
                "height": img_info['height'],
                "width_stride": img_info['width_stride'],
                "height_stride": img_info['height_stride'],
                "pixel_format": HI_PIXEL_FORMAT_UNKNOWN,
                "buffer_size": img_info['img_buf_size']}
out_buffer, ret = acl.himpi.dvpp_malloc(0, out_pic_info['buffer_size'])
out_pic_info['vir_addr'] = out_buffer

# 8.4 发送需解码的输入图片。
ret = acl.himpi.vdec_send_stream(channel_id, stream, out_pic_info, 0)

# 9.接收解码结果。
# 9.1 获取解码结果。
frame_info, supplement, stream, ret = acl.himpi.vdec_get_frame(channel_id, 0)
if ret == 0:
    dec_result = frame_info['v_frame']['frame_flag']
    if dec_result == 0: #  0: Decode success
        print("Chn %u GetFrame Success, Decode Success \n"%channel_id)
    else: # Decode fail
        print("Chn %u GetFrame Success, Decode Fail \n"%channel_id)

# 9.2 如果运行模式为ACL_HOST，且Host上需要展示JPEGD输出的图片数据，则需要申请Host内存，通过aclrtMemcpy接口将Device的输出图片数据传输到Host。
# 获取JPEGD的输出图片数据。

if run_mode == ACL_HOST:
    # 申请Host内存。
    output_buffer, ret= acl.rt.malloc_host(out_pic_info['buffer_size'])
    # 数据传输。
    ret = acl.rt.memcpy(output_buffer, out_pic_info['buffer_size'], frame_info['v_frame']['virt_addr'][0], out_pic_info['buffer_size'], ACL_MEMCPY_DEVICE_TO_HOST)

    # ......
    # 数据使用完成后，及时释放不使用的内存。
    ret = acl.rt.free_host(output_buffer)
else:
    # 可以直接使用JPEGD的输出图片数据，在outputPic.picture_address指向的内存中。
    # ......

# 9.3 释放输入、输出内存。
ret = acl.himpi.dvpp_free(frame_info['v_frame']['virt_addr'][0])
ret = acl.himpi.dvpp_free(stream['addr'])

# 9.4 释放资源。
ret = acl.himpi.vdec_release_frame(channel_id, frame_info)

# 10.解码器停止接收码流。
ret = acl.himpi.vdec_stop_recv_stream(channel_id)

# 11.销毁通道。
ret = acl.himpi.vdec_destroy_chn(channel_id)

# 12.媒体数据处理系统去初始化。
ret = acl.himpi.sys_exit()

# 13.释放运行时资源。
# 14.去初始化。
ret = acl.finalize()
```
<!-- end id1 -->
