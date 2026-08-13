# VENC视频编码

本节介绍VENC视频编码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

VENC（Video Encoder）将YUV420SP格式的图片编码成H264/H265格式的视频码流。关于VENC功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

在实现VENC视频编码功能时，可在创建通道时设置基本参数、或调用对应的set接口设置高级参数，优化视频编码质量，请参见[优化视频编码质量](#section8439152116227)。

## 接口调用流程

**图 1**  VENC视频编码功能调用流程  
![](figures/VENC_API_call_process_V2.png "VENC视频编码功能调用流程")

当前系统支持H264/H265格式的视频码流，关键接口的说明如下：

1. **资源初始化**：
    1. 调用aclInit接口初始化系统。
    2. 调用aclrtSetDevice接口指定计算设备。
    3. 用hi\_mpi\_sys\_init接口进行媒体数据处理系统初始化。
    4. 调用hi\_mpi\_venc\_create\_chn函数创建通道。

        成功创建通道之后，您可以根据实际需求设置编码的高级参数，例如场景模式、码流控制器的高级参数等，请参见hi\_mpi\_venc\_set\_jpeg\_param\~hi\_mpi\_venc\_compact\_jpeg\_tables章节中的接口说明。

    5. 调用hi\_mpi\_venc\_get\_fd将通道ID转换为一个文件句柄。

        <!-- npu="310p" id1 -->
        **说明：**Control CPU开放形态下，为了兼容旧版本，用户在等待编码完成时，旧版本的应用程序中调用Linux操作系统的select或者poll函数的方式仍然可用。建议使用上图中的接口调用流程，保证后续版本的演进。
        <!-- end id1 -->

    6. 调用hi\_mpi\_sys\_create\_epoll函数创建DVPP epoll实例，再调用hi\_mpi\_sys\_ctl\_epoll函数将编码通道的文件句柄添加到epoll实例中，由epoll实例处理。

        select或者poll方式，不需要执行该步骤。

2. **视频编码**：
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

<a id="section8439152116227"></a>

## 优化视频编码质量

在实现VENC视频编码功能时，可在创建通道时设置基本参数、或调用对应的set接口设置高级参数，优化视频编码质量，以下调整手段可以叠加使用，效果是叠加的，例如：

- H264视频数据获取场景，分辨率720P，gop = 60，帧率30fps，码率1M需要提升编码质量，可以使用如下优化手段组合：CBR模式、HI\_VENC\_SCENE\_0、stats\_time等于2、profile等于2、关闭宏块级码控。
- H265电影场景，分辨率1080P，gop=30，帧率25fps，码率2M需要提升编码质量，可以使用如下优化手段组合：CBR模式、HI\_VENC\_SCENE\_1、stats\_time等于1、关闭宏块级码控。

**当前支持以下方式优化视频编码质量**：

- **设置基本参数，优化视频编码质量**

    不同分辨率的视频，其编码质量与视频的帧率、GOP（Group of pictures）、码率有关，在调用hi\_mpi\_venc\_create\_chn接口创建通道时，可设置编码的等级、设置H.264/H.265协议编码场景下CBR/VBR/AVBR/CVBR/QVBR模式的帧率、GOP、码率等参数，来调整视频编码质量：

    - 编码等级，通过hi\_venc\_chn\_attr.venc\_attr结构内的profile参数来设置；
    - 帧率，通过hi\_venc\_chn\_attr.rc\_attr结构体内的src\_frame\_rate输入帧率参数、dst\_frame\_rate输出帧率参数来设置；
    - GOP，通过hi\_venc\_chn\_attr.rc\_attr结构体内的gop参数来设置；
    - 码率，通过hi\_venc\_chn\_attr.rc\_attr结构体内的bit\_rate或max\_bit\_rate或target\_bit\_rate参数来设置。

    **表 1**  典型场景下帧率、GOP、码率的取值

    | 画质/分辨率 | 帧率 | GOP | 码率（Mbps） |
    | --- | --- | --- | --- |
    | 4K<br>3840*2160/4096*2160 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H264/H265码流，码率取值8~12。<br>  - 秀场/主播/短视频场景H265码流，码率取值6~12。<br>H264码流，不涉及。<br>  - 游戏视频场景H264/H265码流，码率取值10~16。 |
    | 2K<br>2560*1440 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H264/H265码流，码率取值6~10。<br>  - 秀场/主播/短视频场景H265码流，码率取值4.8~8。<br>H264码流，不涉及。<br>  - 游戏视频场景H264/H265码流，码率取值6~10。 |
    | 1080P（蓝光）<br>1920*1080 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H265码流，码率取值1~4。<br>H264码流，码率取值2~6。<br>  - 秀场/主播/短视频场景H265码流，码率取值1.4~3.6。<br>H264码流，码率取值2~4.8。<br>  - 游戏视频场景H264/H265码流，码率取值3~6。 |
    | 720P（高清）<br>1280*720 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H265码流，码率取值0.8~2。<br>H264码流，码率取值1~3。<br>  - 秀场/主播/短视频场景H265码流，码率取值1~2。<br>H264码流，码率取值1~3。<br>  - 游戏视频场景H264/H265码流，码率取值2~4。 |
    | 480P/D1_N（标清）<br>854*480/720*480 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H265码流，码率取值0.3~0.7。<br>H264码流，码率取值0.6~1.4。<br>  - 秀场/主播/短视频场景H265码流，码率取值0.25~0.6。<br>H264码流，码率取值0.3~0.7。<br>  - 游戏视频场景不涉及。 |
    | 576P/D1（标清）<br>720*576 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H265码流，码率取值0.3~0.7。<br>H264码流，码率取值0.6~1.4。<br>  - 秀场/主播/短视频场景H265码流，码率取值0.25~0.6。<br>H264码流，码率取值0.3~0.7。<br>  - 游戏视频场景不涉及。 |
    | 270P（流畅）<br>480*270 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景不涉及。<br>  - 秀场/主播/短视频场景H265码流，码率取值0.2。<br>H264码流，码率取值0.3。<br>  - 游戏视频场景不涉及。 |
    | CIF P/N<br>352*288/320*240 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | - 视频数据获取场景H264/H265码流，码率取值0.25。<br>  - 秀场/主播/短视频场景不涉及。<br>  - 游戏视频场景不涉及。 |

- **设置高级参数，调整视频编码细节**

    您可以调用接口设置码控模式、宏块级码率控制参数、编码场景模式等，来调整视频编码的细节，进一步改善编码质量。

    **表 2**  高级配置项列表

    | 配置项 | 接口 | 参数名 | 说明 |
    | --- | --- | --- | --- |
    | 码控模式 | hi_mpi_venc_create_chn | hi_venc_chn_attr.rc_attr结构体内的rc_mode参数 | 追求码率平稳或追求PSNR大且码率符合目标值，配置为CBR；<br>追求节省码率，对主观编码质量有一定要求，配置为VBR；<br>追求节省码率，对主观编码质量有一定要求，且场景中有较多静止画面，配置为AVBR；<br>追求PSNR且对码率上浮没有严格要求，配置为QVBR；<br>追求节省码率，对主观编码质量有一定要求，且可以根据带宽、存储空间要求进行更多调整，配置为CVBR； |
    | 码率控制模型统计时间 | hi_mpi_venc_create_chn | hi_venc_chn_attr.rc_attr内各模式属性值结构体内的stats_time参数 | 关注长期码率稳定，短期波动不在意的可以设置大一些，例：DVR存盘。设大可以提高重编码判决的门槛，重编码次数会减少，但是码率波动会加大。 |
    | 宏块级码率控制参数 | hi_mpi_venc_set_rc_param | hi_venc_rc_param结构内的threshold_i、threshold_p、threshold_b、direction、row_qp_delta参数 | 如果图像内容复杂、细节较多或用户关注PSNR等客观指标时，需关闭宏块级码率控制。 |
    | 第一帧的起始Qp值 | hi_mpi_venc_create_chn | hi_venc_rc_param结构内的first_frame_start_qp参数 | 典型场景下，用户配置的码率小于表1中给的参考值，且编码后的视频第一帧明显模糊，则建议配置first_frame_start_qp参数，参数值取[min_i_qp, max_i_qp]的中间值，例如,[min_i_qp, max_i_qp]为[30, 40]，则first_frame_start_qp参数配置为35，同时将max_reencode_times参数配置为0，会获得较好的编码质量。 |
    | 编码场景模式 | hi_mpi_venc_set_scene_mode | hi_venc_scene_mode | 安防场景配置为HI_VENC_SCENE_0；辅助驾驶、直播、游戏、动画、电影配置为HI_VENC_SCENE_1。 |

## 示例代码

以下是VENC视频编码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id2 -->
您可以单击[venc\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/venc_sample)获取样例。
<!-- end id2 -->

```cpp
// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_venc_chn chn = 0;
hi_venc_chn_attr attr{};
attr.venc_attr.type = HI_PT_H265;
attr.venc_attr.profile = 0;
attr.venc_attr.max_pic_width = 128;
attr.venc_attr.max_pic_height = 128;
attr.venc_attr.pic_width = 128;
attr.venc_attr.pic_height = 128;
attr.venc_attr.buf_size = 2 * 1024 * 1024;
attr.venc_attr.is_by_frame = HI_TRUE;
attr.rc_attr.rc_mode = HI_VENC_RC_MODE_H265_VBR;
attr.rc_attr.h265_vbr.gop = 30;
attr.rc_attr.h265_vbr.stats_time = 1;
attr.rc_attr.h265_vbr.src_frame_rate = 30;
attr.rc_attr.h265_vbr.dst_frame_rate = 30;
attr.rc_attr.h265_vbr.max_bit_rate = 4000;
attr.gop_attr.gop_mode = HI_VENC_GOP_MODE_NORMAL_P;
attr.gop_attr.normal_p.ip_qp_delta = 3;
ret = hi_mpi_venc_create_chn(chn, &attr);

// 3.通知编码器启动接收输入数据
hi_venc_start_param recv_param{};
recv_param.recv_pic_num = -1;
ret = hi_mpi_venc_start_chn(chn, &recv_param);

// 4.发送输入数据
// 4.1 申请输入内存
uint8_t* inputAddr = nullptr;
int32_t inputSize = 128 * 128 * 3 / 2;
ret = hi_mpi_dvpp_malloc(0, &inputAddr, inputSize);

// 将输入数据读入Device内存中，该自定义函数VencReadYuvFile由用户实现
VencReadYuvFile(streamName, inputAddr, inputSize);

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
ret = hi_mpi_sys_wait_epoll(epollFd, events, 3, 1000, &eventCount);

// 5.2 获取编码结果
hi_venc_chn_status stat;
ret = hi_mpi_venc_query_status(chn, &stat);
hi_venc_stream stream;
stream.pack_cnt = stat.cur_packs;
stream.pack = new hi_venc_pack[stream.pack_cnt];
ret = hi_mpi_venc_get_stream(chn, &stream, 1000);

// 5.3 获取编码输出码流数据
// 可以直接使用编码输出码流数据，在stream.pack[0].addr指向的内存中
// TODO: 推理相关的代码逻辑

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
