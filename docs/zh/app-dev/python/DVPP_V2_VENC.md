<!-- npu="910b,910,310p,310b" id1 -->
# VENC视频编码

VENC（Video Encoder）将YUV420SP格式的图片编码成H.264/H.265格式的视频码流。关于VENC功能的详细介绍请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍VENC视频编码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程
<!-- npu="310p,310b" id2 -->
开发应用时，如果涉及视频编码，则应用程序中必须包含编码的代码逻辑，关于编码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。
<!-- end id2 -->
**图 1**  接口调用流程
![](figures/VENC_API_call_process_V2.png "接口调用流程-8")

当前系统支持H.264/H.265格式的视频码流，关键接口的说明如下：

1. 调用`acl.himpi.sys_init`接口进行媒体数据处理系统初始化。
2. 调用`acl.himpi.venc_create_chn`函数创建通道。

    成功创建通道之后，您可以根据实际需求设置编码的高级参数，例如场景模式、码流控制器的高级参数等，请参见`acl.himpi.venc_set_jpeg_param`\~`acl.himpi.venc_compact_jpeg_tables`章节中的接口说明。

3. 调用`acl.himpi.venc_get_fd`将通道ID转换为一个文件句柄。
4. 调用`acl.himpi.sys_create_epoll`函数创建DVPP epoll实例。

    Control CPU开放形态下，为了兼容旧版本，用户在等待编码完成时，旧版本的应用程序中调用Linux操作系统的select或者poll函数的方式仍然可用。建议使用上图中的接口调用流程，保证后续版本的演进。

5. 调用`acl.himpi.sys_ctl_epoll`函数将编码通道的文件句柄添加到epoll实例中，由epoll实例处理。

    select或者poll方式，不需要执行该步骤。

6. 调用`acl.himpi.venc_start_chn`函数通知通道准备开始编码。
7. 调用`acl.himpi.dvpp_malloc`接口申请存放Device上输入数据的内存。
    <!-- npu="310b" id3 -->
    对于Atlas 200I/500 A2推理产品，调用`acl.himpi.dvpp_malloc`接口申请的内存为媒体数据处理的专用内存，但专用内存的地址空间有限，若关注内存规划或内存资源有限时，建议调用`acl.rt.malloc`接口申请内存。
    <!-- end id3 -->
8. 启动一个用户态线程，调用`acl.himpi.sys_wait_epoll`函数等待编码完成。
9. 之后用户就可以调用`acl.himpi.venc_send_frame`函数发送待编码的码流。
10. 一旦编码完成，`acl.himpi.sys_wait_epoll`函数或select函数或poll函数就会返回，用户就可以调用`acl.himpi.venc_query_status`接口查询编码状态，再调用`acl.himpi.venc_get_stream`函数获取编码结果。
11. 用户需要注意的是，编码结果数据使用完成之后，需要及时调用`acl.himpi.venc_release_stream`函数释放Buffer。否则会因编码Buffer用完导致后续编码无法进行。
12. 调用`acl.himpi.dvpp_free`接口释放输入内存。
    <!-- npu="310b" id4 -->
    Atlas 200I/500 A2推理产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id4 -->
13. 当用户不需发送图像到目标通道继续编码时，需要调用`acl.himpi.venc_stop_chn`函数通知该通道不再接收新的输入图片。
14. 调用`acl.himpi.sys_ctl_epoll`函数从epoll实例中删除编码通道的文件句柄。
15. 当用户完成所有编码之后，需要调用`acl.himpi.venc_destroy_chn`释放编码通道以及内部内存资源。
16. 调用`acl.himpi.sys_close_epoll`函数销毁DVPP epoll实例。
17. 调用`acl.himpi.sys_exit`接口进行媒体数据处理系统去初始化。

## 优化视频编码质量

在实现VENC视频编码功能时，可在创建通道时设置基本参数、或调用对应的set接口设置高级参数，优化视频编码质量，以下调整手段可以叠加使用，效果是叠加的，例如：

- H.264视频数据获取场景，分辨率720P，gop = 60，帧率30fps，码率1M需要提升编码质量，可以使用如下优化手段组合：CBR模式、HI\_VENC\_SCENE\_0、stats\_time等于2、profile等于2、关闭宏块级码控。
- H.265电影场景，分辨率1080P，gop=30，帧率25fps，码率2M需要提升编码质量，可以使用如下优化手段组合：CBR模式、HI\_VENC\_SCENE\_1、stats\_time等于1、关闭宏块级码控。

**当前支持以下方式优化视频编码质量**：

- **设置基本参数，优化视频编码质量**

    不同分辨率的视频，其编码质量与视频的帧率、GOP（Group of pictures）、码率有关，在调用`acl.himpi.venc_create_chn`接口创建通道时，可设置编码的等级、设置H.264/H.265协议编码场景下CBR/VBR/AVBR/CVBR/QVBR模式的帧率、GOP、码率等参数，来调整视频编码质量：

    - 编码等级，通过`hi_venc_chn_attr`\["venc\_attr"\]字典内的“profile”属性来确定。
    - 帧率，通过`hi_venc_chn_attr`\["rc\_attr"\]字典内的“src\_frame\_rate”输入帧率参数、“dst\_frame\_rate”输出帧率属性来确定。
    - GOP，通过`hi_venc_chn_attr`\["rc\_attr"\]字典内的“gop”属性来确定。
    - 码率，通过`hi_venc_chn_attr`\["rc\_attr"\]字典内的`bit_rate`、`max_bit_rate`或`target_bit_rate`属性来确定。

    **表 1**  典型场景下帧率、GOP、码率的取值
    <!-- npu="310p,310b" id5 -->
    | 画质/分辨率 | 帧率 | GOP | 码率（mbps） |
    | --- | --- | --- | --- |
    | 4K<br>3840\*2160/4096\*2160 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H264/H265码流，码率取值8~12。<br>秀场/主播/短视频场景<br>H265码流，码率取值6~12。<br>H264码流，不涉及。<br>游戏视频场景<br>H264/H265码流，码率取值10~16。<br>MDC场景<br>H264/H265码流，码率取值16以上。 |
    | 2K<br>2560\*1440 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H264/H265码流，码率取值6~10。<br>秀场/主播/短视频场景<br>H265码流，码率取值4.8~8。<br>H264码流，不涉及。<br>游戏视频场景<br>H264/H265码流，码率取值6~10。<br>MDC场景<br>H264/H265码流，码率取值12以上。 |
    | 1080P（蓝光）<br>1920\*1080 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H265码流，码率取值1~4。<br>H264码流，码率取值2~6。<br>秀场/主播/短视频场景<br>H265码流，码率取值1.4~3.6。<br>H264码流，码率取值2~4.8。<br>游戏视频场景<br>H264/H265码流，码率取值3~6。<br>MDC场景<br>H264/H265码流，码率取值8以上。 |
    | 720P（高清）<br>1280\*720 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H265码流，码率取值0.8~2。<br>H264码流，码率取值1~3。<br>秀场/主播/短视频场景<br>H265码流，码率取值1~2。<br>H264码流，码率取值1~3。<br>游戏视频场景<br>H264/H265码流，码率取值2~4。<br>MDC场景<br>H264/H265码流，码率取值4以上。 |
    | 480P/D1_N（标清）<br>854\*480/720\*480 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H265码流，码率取值0.3~0.7。<br>H264码流，码率取值0.6~1.4。<br>秀场/主播/短视频场景<br>H265码流，码率取值0.25~0.6。<br>H264码流，码率取值0.3~0.7。<br>游戏视频场景<br>不涉及。<br>MDC场景<br>不涉及。 |
    | 576P/D1（标清）<br>720\*576 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H265码流，码率取值0.3~0.7。<br>H264码流，码率取值0.6~1.4。<br>秀场/主播/短视频场景<br>H265码流，码率取值0.25~0.6。<br>H264码流，码率取值0.3~0.7。<br>游戏视频场景<br>不涉及。<br>MDC场景<br>不涉及。 |
    | 270P（流畅）<br>480\*270 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>不涉及。<br>秀场/主播/短视频场景<br>H265码流，码率取值0.2。<br>H264码流，码率取值0.3。<br>游戏视频场景<br>不涉及。<br>MDC场景<br>不涉及。 |
    | CIF P/N<br>352\*288/320\*240 | 25或30 | 建议GOP为帧率的整数倍，例如帧率为25时，GOP建议25或50。 | 视频数据获取场景<br>H264/H265码流，码率取值0.25。<br>秀场/主播/短视频场景<br>不涉及。<br>游戏视频场景<br>不涉及。<br>MDC场景<br>不涉及。 |
    <!-- end id5 -->
- **设置高级参数，调整视频编码细节**

    您可以调用接口设置码控模式、宏块级码率控制参数、编码场景模式等，来调整视频编码的细节，进一步改善编码质量。

    **表 2**  高级配置项列表

    | 配置项 | 接口 | 参数名 | 说明 |
    | --- | --- | --- | --- |
    | 码控模式 | `acl.himpi.venc_create_chn` | `hi_venc_chn_attr`["rc_attr"]字典内的“rc_mode”属性 | 追求码率平稳或追求PSNR大且码率符合目标值，配置为CBR。<br>追求节省码率，对主观编码质量有一定要求，配置为VBR。<br>追求节省码率，对主观编码质量有一定要求，且场景中有较多静止画面，配置为AVBR。<br>追求PSNR且对码率上浮没有严格要求，配置为QVBR。<br>追求节省码率，对主观编码质量有一定要求，且可以根据带宽、存储空间要求进行更多调整，配置为CVBR。 |
    | 码率控制模型统计时间 | `acl.himpi.venc_create_chn` | `hi_venc_chn_attr`["rc_attr"]字典内各模式属性值字典内的`stats_time`属性 | 关注长期码率稳定，短期波动不在意的可以设置大一些，例：DVR存盘。设大可以提高重编码判决的门槛，重编码次数会减少，但是码率波动会加大。 |
    | 宏块级码率控制参数 | `acl.himpi.venc_set_rc_param` | `hi_venc_rc_param`字典内的`threshold_i`、`threshold_p`、“threshold_b”、“direction”、“row_qp_delta”属性。 | 如果图像内容复杂、细节较多或用户关注PSNR等客观指标时，需关闭宏块级码率控制。 |
    | 第一帧的起始QP值 | `acl.himpi.venc_create_chn` | `hi_venc_rc_param`字典内的`first_frame_start_qp`属性 | 典型场景下，用户配置的码率小于表1中给的参考值，且编码后的视频第一帧明显模糊，则建议配置`first_frame_start_qp`属性，参数值取[min_i_qp, max_i_qp]的中间值，例如，[min_i_qp, max_i_qp]为[30, 40]，则`first_frame_start_qp`配置为“35”，同时将`max_reencode_times`配置为“0”，会获得较好的编码质量。 |
    | 编码场景模式 | `acl.himpi.venc_set_scene_mode` | `hi_venc_scene_mode`类 | 安防场景配置为HI_VENC_SCENE_0；自动驾驶、直播、游戏、动画、电影配置为HI_VENC_SCENE_1。 |

<!-- npu="310p,310b" id6 -->
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

# 5.设置VENC模块参数。
param = {'mod_type':HI_VENC_MOD_H265}
param, ret = acl.himpi.venc_get_mod_param(param)
param['jpeg_mod_param']['one_stream_buf'] = 1
ret = acl.himpi.venc_set_mod_param(param)

# 6.创建通道。
channel_id = 0
venc_attr = {'type': HI_VENC_MOD_H265, 'profile': 0,
             'max_pic_width': 128, 'pic_width': 128,
             'max_pic_height': 128, 'pic_height': 128,
             'buf_size': 1024 * 1024 * 2, 'is_by_frame': 1}
rc_attr = {'rc_mode':HI_VENC_RC_MODE_H265_VBR,
           'h265_vbr':{'gop': 30, 'stats_time': 1,
                       'src_frame_rate': 30, 'dst_frame_rate': 30,
                       'max_bit_rate': 4000}}
gop_attr = {'gop_mode':0, 'normal_p':{'ip_qp_delta':3}}
attr = {'venc_attr':venc_attr, 'rc_attr':rc_attr, 'gop_attr':gop_attr}
ret = acl.himpi.venc_create_chn(channel_id, attr)

# 7.通知编码器开始接收输入数据。
recv_param = {'recv_pic_num':-1}
ret = acl.himpi.venc_start_chn(channel_id, recv_param)

# 8.发送输入数据。
# 8.1 申请输入内存。
input_size = 128 * 128 * 3 // 2
input_addr, ret = acl.himpi.dvpp_malloc(0, input_size)

# 如果运行模式为ACL_HOST，则需要申请Host内存，将输入数据读入Host内存，再通过acl.rt.memcpy接口将Host的数据传输到Device，数据传输完成后，需及时释放Host内存；否则直接将输入数据读入Device内存。
# 直接将输入数据读入Device内存。
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
           'time_ref': 0,'pts': cur_time}
frame = {'v_frame':v_frame, 'pool_id':0, 'mod_id':HI_ID_VENC}
ret = acl.himpi.venc_send_frame(channel_id, frame, 0)

# 9.获取编码结果。
# 9.1 通过EPOLL处理编码完成事件。
fd = acl.himpi.venc_get_fd(channel_id)
epoll_fd, ret = acl.himpi.sys_create_epoll(10)

event = {'data': fd, 'events': HI_DVPP_EPOLL_IN}
ret = acl.himpi.sys_ctl_epoll(epoll_fd, HI_DVPP_EPOLL_CTL_ADD, fd, event)

# 编码完成前，会超时阻塞在这里，一旦完成，才会往下执行。
events, eventCount, ret = acl.himpi.sys_wait_epoll(epoll_fd, 3, 1000)

# 9.2 获取编码结果。
status, ret = acl.himpi.venc_query_status(channel_id)
stream = {'pack_cnt': status['cur_packs']}
stream, ret = acl.himpi.venc_get_stream(self.channel_id, stream, 1000)
# 9.3 如果运行模式为ACL_HOST，且Host上需要使用编码输出的码流，则需要申请Host内存，通过acl.rt.memcpy接口将Device的输出码流传输到Host。
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

# 13. 媒体数据处理系统去初始化。
ret = acl.himpi.sys_exit()

# 14. 释放运行时资源。
# 15.去初始化。
ret = acl.finalize()
```
<!-- end id6 -->
<!-- end id1 -->
