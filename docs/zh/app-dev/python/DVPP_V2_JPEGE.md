<!-- npu="910b,910,310p,310b" id1 -->
# JPEGE图片编码

JPEGE（JPEG Encoder）负责完成图像编码功能，将YUV格式图片编码成.jpg图片。关于JPEGE功能的详细介绍请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍JPEGE图片编码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程

开发应用时，如果涉及将YUV格式图片编码成JPEG压缩格式的图片文件，则应用程序中必须包含编码的代码逻辑，关于编码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。

**图 1**  接口调用流程
![](figures/JPEGE_API_call_process_V2.png "接口调用流程-5")

当前系统支持将YUV格式图片编码成JPEG压缩格式的图片文件，关键接口的说明如下：

1. 调用`acl.himpi.sys_init`接口进行媒体数据处理系统初始化。
2. 调用`acl.himpi.venc_create_chn`函数创建完通道。

    成功创建通道之后，您可以根据实际需求设置编码的高级参数，例如场景模式、码流控制器的高级参数等，请参见`acl.himpi.venc_set_jpeg_param`\~`acl.himpi.venc_compact_jpeg_tables`章节中的接口说明。

3. 调用`acl.himpi.venc_get_fd`将通道ID转换为一个文件句柄。
4. 调用`acl.himpi.sys_create_epoll`函数创建DVPP epoll实例。
5. 调用`acl.himpi.sys_ctl_epoll`函数将编码通道的文件句柄添加到epoll实例中，由epoll实例处理。select或者poll方式，不需要执行该步骤。
6. 调用`acl.himpi.venc_start_chn`函数通知通道准备开始编码。
7. 调用`acl.himpi.dvpp_malloc`接口申请存放Device上输入数据的内存。
    <!-- npu="910b,310b" id2 -->
    对于Atlas 200I/500 A2推理产品与Atlas A2系列产品，调用`acl.himpi.dvpp_malloc`接口申请的内存为媒体数据处理的专用内存，但专用内存的地址空间有限，若关注内存规划或内存资源有限时，建议调用`acl.rt.malloc`接口申请内存。
    <!-- end id2 -->
8. 启动一个用户态线程，调用`acl.himpi.sys_wait_epoll`函数等待编码完成。
9. 之后用户就可以调用`acl.himpi.venc_send_frame`函数发送待编码的码流。
10. 一旦编码完成，`acl.himpi.sys_wait_epoll`函数或select函数或poll函数就会返回，用户就可以调用`acl.himpi.venc_query_status`接口查询编码状态，再调用`acl.himpi.venc_get_stream`函数获取编码结果。
11. 用户需要注意的是，编码结果数据使用完成之后，需要及时调用`acl.himpi.venc_release_stream`函数释放Buffer。否则会因编码Buffer用完导致后续编码无法进行。
12. 调用`acl.himpi.dvpp_free`接口释放输入内存。
    <!-- npu="310b" id3 -->
    Atlas 200I/500 A2推理产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id3 -->
    <!-- npu="910b" id4 -->
    Atlas A2系列产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id4 -->
13. 当用户不需发送图像到目标通道继续编码时，需要调用`acl.himpi.venc_stop_chn`函数通知该通道不再接收新的输入图片。
14. 调用`acl.himpi.sys_ctl_epoll`函数从epoll实例中删除编码通道的文件句柄。
15. 当用户完成所有编码之后，需要调用`acl.himpi.venc_destroy_chn`释放编码通道以及内部内存资源。
16. 调用`acl.himpi.sys_close_epoll`函数销毁DVPP epoll实例。
17. 调用`acl.himpi.sys_exit`接口进行媒体数据处理系统去初始化。

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
venc_attr = {'type': HI_PT_JPEG, 'profile': 0,
             'max_pic_width': 128, 'pic_width': 128,
             'max_pic_height': 128, 'pic_height': 128,
             'buf_size': 1024 * 1024 * 2, 'is_by_frame': 1}
jpeg_attr = {'recv_mode':HI_VENC_PIC_RECV_SINGLE,
            'mpf_cfg':{'large_thumbnail_num': 0}}
attr = {'venc_attr':venc_attr, 'jpeg_attr':jpeg_attr}
ret = acl.himpi.venc_create_chn(channel_id, attr)

# 6.设置JPEGE参数。
param, ret = acl.himpi.venc_get_jpeg_param(channel_id)
param['qfactor'] = 100
ret = acl.himpi.venc_set_jpeg_param(channel_id, param)

# 7.通知编码器开始接收输入数据。
recv_param = {'recv_pic_num': -1}
ret = acl.himpi.venc_start_chn(channel_id, recv_param)

# 8.发送输入数据。
# 8.1 申请输入内存。
input_size = 128 * 128 * 3 // 2
input_addr, ret = acl.himpi.dvpp_malloc(0, input_size)

# 如果运行模式为ACL_HOST，则需要申请Host内存，将输入图片数据读入Host内存，再通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时释放Host内存；否则直接将输入图片数据读入Device内存。
# 直接将输入图片数据读入Device内存。
if run_mode == ACL_HOST:
    # 将输入图片读入内存中。
    jpege_file = np.fromfile(jpege_file_path, dtype=np.byte)
    jpege_file_size = jpege_file.itemsize * jpege_file.size

    bytes_data = jpege_file.tobytes()
    jpege_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, jpege_file_ptr, jpege_file_size, ACL_MEMCPY_HOST_TO_DEVICE)
else:
    # 将输入图片读入内存中。
    jpege_file = np.fromfile(jpege_file_path, dtype=np.byte)
    jpege_file_size = jpege_file.itemsize * jpege_file.size

    bytes_data = jpege_file.tobytes()
    jpege_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, jpege_file_ptr, jpege_file_size, ACL_MEMCPY_DEVICE_TO_DEVICE)

# 8.2 发送输入数据，开始编码。
v_frame = {'width': 128,
           'height': 128,
           'field': HI_VIDEO_FIELD_FRAME,
           'pixel_format': HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420,
           'video_format': HI_VIDEO_FORMAT_LINEAR,
           'compress_mode': HI_COMPRESS_MODE_NONE,
           'dynamic_range': HI_DYNAMIC_RANGE_SDR8,
           'color_gamut': HI_COLOR_GAMUT_BT709,
           'header_stride': [0, 0, 0],
           'width_stride': [128, 0, 0],
           'height_stride': [0, 0, 0],
           'header_phys_addr': [0, 0, 0],
           'phys_addr': [0, 0, 0],
           'header_virt_addr': [0, 0, 0],
           'virt_addr': [input_addr, 0, 0],
           'time_ref': 0, 'pts': cur_time}
frame = {'v_frame':v_frame, 'pool_id':0, 'mod_id':HI_ID_VGS}
ret = acl.himpi.venc_send_frame(channel_id, frame, 0)

# 9.获取编码结果。
# 9.1 通过EPOLL处理编码完成事件。
fd = acl.himpi.venc_get_fd(channel_id)
epoll_fd, ret = acl.himpi.sys_create_epoll(10)

event['data'] = fd
event['events'] = HI_DVPP_EPOLL_IN
ret = acl.himpi.sys_ctl_epoll(epoll_fd, HI_DVPP_EPOLL_CTL_ADD, fd, event)

# 编码完成前，会超时阻塞在这里，一旦完成，才会往下执行。
events, eventCount, ret = acl.himpi.sys_wait_epoll(epoll_fd, 3, 1000)

# 9.2 获取编码结果。
status, ret = acl.himpi.venc_query_status(channel_id)
stream = {'pack_cnt': status['cur_packs']}
stream, ret = acl.himpi.venc_get_stream(channel_id, stream, 1000)
# 9.3 如果运行模式为ACL_HOST，且Host上需要使用编码输出的码流，则需要申请Host内存，通过acl.rt.memcpy接口将Device的输出码流传输到Host；否则直接使用编码输出码流数据。
# 获取编码输出码流数据。
if run_mode == ACL_HOST:
    # 申请Host内存。
    output_buffer, ret= acl.rt.malloc_host(output_size)
    # 数据传输。
    ret = acl.rt.memcpy(output_buffer, output_size, stream['pack'][0]['addr'], output_size, ACL_MEMCPY_DEVICE_TO_HOST)
    # ......
    # 数据使用完成后，及时释放不使用的内存。
    ret = acl.rt.free_host(output_buffer)
else:
    # 可以直接使用编码输出码流数据，在stream['pack'][0]['addr']指向的内存中。
    # ......

# 10.释放输入内存和输出码流。
ret = acl.himpi.dvpp_free(input_addr)
ret = acl.himpi.venc_release_stream(channel_id, stream)

# 11.通知编码器停止接收输入数据。
ret = acl.himpi.venc_stop_chn(channel_id)
ret = acl.himpi.sys_ctl_epoll(epoll_fd, HI_DVPP_EPOLL_CTL_DEL, fd, event)
ret = acl.himpi.sys_close_epoll(epoll_fd)

# 12.销毁通道。
ret = acl.himpi.venc_destroy_chn(channel_id)

# 13.媒体数据处理系统去初始化。
ret = acl.himpi.sys_exit()

# 14.释放运行时资源。
# 15.去初始化。
ret = acl.finalize()
```
<!-- end id1 -->
