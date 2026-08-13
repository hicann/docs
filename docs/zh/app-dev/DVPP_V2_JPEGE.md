# JPEGE图片编码

本节介绍JPEGE图片编码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

JPEGE（JPEG Encoder）负责完成图像编码功能，将YUV格式图片编码成.jpg图片。关于JPEGE功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

**图 1**  JPEGE图片编码功能调用流程  
![](figures/JPEGE_API_call_process_V2.png "JPEGE图片编码功能调用流程")

当前系统支持将YUV格式图片编码成JPEG压缩格式的图片文件，关键接口的说明如下：

1. **资源初始化**：
    1. 调用aclInit接口初始化系统。
    2. 调用aclrtSetDevice接口指定计算设备。
    3. 调用hi\_mpi\_sys\_init接口进行媒体数据处理系统初始化。
    4. 调用hi\_mpi\_venc\_create\_chn函数创建通道。

        成功创建通道之后，您可以根据实际需求设置编码的高级参数，例如场景模式、码流控制器的高级参数等，请参见hi\_mpi\_venc\_set\_jpeg\_param\~hi\_mpi\_venc\_compact\_jpeg\_tables章节中的接口说明。

    5. 调用hi\_mpi\_venc\_get\_fd将通道ID转换为一个文件句柄。
    6. 调用hi\_mpi\_sys\_create\_epoll函数创建DVPP epoll实例。

        **说明：**Control CPU开放形态下，为了兼容旧版本，用户在等待编码完成时，旧版本的应用程序中调用Linux操作系统的select或者poll函数的方式仍然可用。建议使用上图中的接口调用流程，保证后续版本的演进。

    7. 调用hi\_mpi\_sys\_ctl\_epoll函数将编码通道的文件句柄添加到epoll实例中，由epoll实例处理。

        select或者poll方式，不需要执行该步骤。

2. **图片编码**：
    1. 调用hi\_mpi\_venc\_start\_chn函数通知通道准备开始编码。
    2. 调用hi\_mpi\_dvpp\_malloc接口申请存放Device上输入数据的内存。
    3. 启动一个用户态线程，调用hi\_mpi\_sys\_wait\_epoll函数等待编码完成。
    4. 之后用户就可以调用hi\_mpi\_venc\_send\_frame函数发送待编码的码流。
    5. 一旦编码完成，hi\_mpi\_sys\_wait\_epoll函数或select函数或poll函数就会返回，用户就可以调用hi\_mpi\_venc\_query\_status接口查询编码状态，再调用hi\_mpi\_venc\_get\_stream函数获取编码结果。
    6. 用户需要注意的是，编码结果数据使用完成之后，需要及时调用hi\_mpi\_venc\_release\_stream函数释放buffer。否则会因编码buffer用完导致后续编码无法进行。
    7. 调用hi\_mpi\_dvpp\_free接口释放输入内存。
    8. 当用户不需发送图像到目的通道继续编码时，需要调用hi\_mpi\_venc\_stop\_chn函数通知该通道不再接收新的输入图片。

3. **资源释放**：
    1. 调用hi\_mpi\_sys\_ctl\_epoll函数从epoll实例中删除编码通道的文件句柄。
    2. 当用户完成所有编码之后，需要调用hi\_mpi\_venc\_destroy\_chn释放编码通道以及内部内存资源。
    3. 调用hi\_mpi\_sys\_close\_epoll函数销毁DVPP epoll实例。
    4. 调用hi\_mpi\_sys\_exit接口进行媒体数据处理系统去初始化。
    5. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
    6. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 示例代码

以下是JPEGE图片编码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id1 -->
您可以单击[jpege\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/jpege_sample)获取样例。
<!-- end id1 -->

```cpp
// ....

// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_venc_chn chn = 0;
hi_venc_chn_attr attr{};
attr.venc_attr.type = HI_PT_JPEG;
attr.venc_attr.profile = 0;
attr.venc_attr.max_pic_width = 128;
attr.venc_attr.max_pic_height = 128;
attr.venc_attr.pic_width = 128;
attr.venc_attr.pic_height = 128;
attr.venc_attr.buf_size = 2 * 1024 * 1024;
attr.venc_attr.is_by_frame = HI_TRUE;
attr.venc_attr.jpeg_attr.dcf_en = HI_FALSE;
attr.venc_attr.jpeg_attr.recv_mode = HI_VENC_PIC_RECV_SINGLE;
attr.venc_attr.jpeg_attr.mpf_cfg.large_thumbnail_num = 0;
ret = hi_mpi_venc_create_chn(chn, &attr);

// 3.通知编码器开始接收输入数据
hi_venc_start_param recv_param{};
recv_param.recv_pic_num = -1;
ret = hi_mpi_venc_start_chn(chn, &recv_param);

// 4.发送输入数据
// 4.1 申请输入内存
uint8_t* inputAddr = nullptr;
int32_t inputSize = 128 * 128 * 3 / 2;
ret = hi_mpi_dvpp_malloc(0, &inputAddr, inputSize);
// 将输入数据读入内存中，该自定义函数JpegeReadYuvFile由用户实现
JpegeReadYuvFile(streamName, inputAddr, inputSize);

// 4.2 发送输入数据，开始编码
hi_video_frame_info frame{};
frame.mod_id = HI_ID_VENC;
frame.v_frame.width = 128;
frame.v_frame.height = 128;
frame.v_frame.field = HI_VIDEO_FIELD_FRAME;
frame.v_frame.pixel_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
frame.v_frame.video_format = HI_VIDEO_FORMAT_LINEAR;
frame.v_frame.compress_mode = HI_COMPRESS_MODE_NONE;
frame.v_frame.dynamic_range = HI_DYNAMIC_RANGE_SDR8;
frame.v_frame.color_gamut = HI_COLOR_GAMUT_BT709;
frame.v_frame.width_stride[0] = 128;
frame.v_frame.width_stride[1] = 128;
frame.v_frame.width_stride[2] = 128;
frame.v_frame.virt_addr[0] = inputAddr;
frame.v_frame.virt_addr[1] = (hi_void *)((uintptr_t)frame.v_frame.virt_addr[0] + 128 * 128);
frame.v_frame.frame_flag = 0;
frame.v_frame.time_ref = 0;
frame.v_frame.pts = 0;
ret = hi_mpi_venc_send_frame(chn, &frame, 0);

// 5.获取编码结果
// 5.1 创建EPOLL实例
int32_t epollFd = 0;
int32_t fd = hi_mpi_venc_get_fd(chn);
ret = hi_mpi_sys_create_epoll(10, &epollFd);

hi_dvpp_epoll_event event;
event.events = HI_DVPP_EPOLL_IN;
event.data = (void*)(unsigned long)(fd);
ret = hi_mpi_sys_ctl_epoll(epollFd, HI_DVPP_EPOLL_CTL_ADD, fd, &event);

int32_t eventCount = 0;
// 编码完成前，会超时阻塞在这里，一旦完成，才会往下执行
ret = hi_mpi_sys_wait_epoll(epollFd, event, 3, 1000, &eventCount);

// 5.2 获取编码结果
hi_venc_chn_status stat;
ret = hi_mpi_venc_query_status(chn, &stat);
hi_venc_stream stream;
stream.pack_cnt = stat.cur_packs;
stream.pack = new hi_venc_pack[stream.pack_cnt];
ret = hi_mpi_venc_get_stream(chn, &stream, 1000);

// 5.3 获取编码输出码流数据，在stream.pack[0].addr指向的内存中
......

// 6.释放输入内存和输出码流
ret = hi_mpi_dvpp_free(inputAddr);
ret = hi_mpi_venc_release_stream(chn, &stream);
delete[] stream.pack;

// 7.通知编码器停止接收输入数据
ret = hi_mpi_venc_stop_chn(chn);
ret = hi_mpi_sys_ctl_epoll(epollFd, HI_DVPP_EPOLL_CTL_DEL, fd, NULL);
ret = hi_mpi_sys_close_epoll(epollFd);

// 8.销毁通道
ret = hi_mpi_venc_destroy_chn(chn);

// 9.媒体数据处理系统去初始化
ret = hi_mpi_sys_exit();

// ....
```
