# VDEC视频解码

本节介绍VDEC视频解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

VDEC（Video Decoder）负责将H264/H265格式的视频码流解码为YUV/RGB格式的图片。关于VDEC功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

开发应用时，如果涉及视频解码，则应用程序中必须包含解码的代码逻辑。

**图 1**  VDEC视频解码功能调用的流程  
![](figures/VDEC_API_call_process_V2.png "VDEC视频解码功能调用的流程")

当前系统支持解码H264/H265的视频码流，关键接口的说明如下：

1. 调用aclInit接口初始化系统。
2. 调用aclrtSetDevice接口指定计算设备。
3. 调用hi\_mpi\_sys\_init接口进行媒体数据处理系统初始化。
4. 调用hi\_vdec\_get\_pic\_buf\_size接口获取解码所需的帧存大小、调用hi\_vdec\_get\_tmv\_buf\_size接口获取矢量预测缓冲区的大小，在创建通道时需要使用这些数据。
5. 调用hi\_mpi\_vdec\_create\_chn接口创建通道。
6. 调用hi\_mpi\_dvpp\_malloc接口申请Device上的内存，存放输入或输出数据。
7. 解码前，需调用hi\_mpi\_vdec\_start\_recv\_stream接口通知解码器启动接收码流，再调用hi\_mpi\_vdec\_send\_stream接口发送解码码流，hi\_mpi\_vdec\_send\_stream接口是异步接口，调用该接口仅表示任务下发成功，还需要调用hi\_mpi\_vdec\_get\_frame接口获取解码结果数据，成功获取解码数据后，可以调用hi\_mpi\_vdec\_release\_frame接口释放帧相关的资源。解码结束后，需调用hi\_mpi\_vdec\_stop\_recv\_stream接口通知解码器停止接收码流。
8. 调用hi\_mpi\_dvpp\_free接口释放输入、输出内存。
9. 调用hi\_mpi\_vdec\_destroy\_chn接口销毁通道。
10. 调用hi\_mpi\_sys\_exit接口进行媒体数据处理系统去初始化。
11. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
12. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 示例代码

以下是VDEC视频解码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id1 -->
您可以单击[vdec\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/vdec_sample)获取样例。
<!-- end id1 -->

```cpp
// ....

// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_vdec_chn chnId;
hi_vdec_chn_attr chnAttr;
hi_pic_buf_attr buf_attr{1920, 1080, 0, 8, HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420, HI_COMPRESS_MODE_NONE};

chnAttr.type = HI_PT_H264;
chnAttr.mode = HI_VDEC_SEND_MODE_FRAME;
chnAttr.pic_width = 1920;
chnAttr.pic_height = 1080;
chnAttr.stream_buf_size = 1920 * 1080 * 3 / 2;
chnAttr.frame_buf_cnt = 16;
chnAttr.frame_buf_size = hi_vdec_get_pic_buf_size(HI_PT_H264, &buf_attr);
chnAttr.video_attr.ref_frame_num = 12;
chnAttr.video_attr.temporal_mvp_en = HI_TRUE;
chnAttr.video_attr.tmv_buf_size = hi_vdec_get_tmv_buf_size(HI_PT_H264, 1920, 1080);

ret = hi_mpi_vdec_create_chn(chnId, &chnAttr);

// 3.设置通道属性
hi_vdec_chn_param chnParam;
ret = hi_mpi_vdec_get_chn_param(chnId, &chnParam);

chnParam.video_param.dec_mode = HI_VIDEO_DEC_MODE_IPB;        
chnParam.video_param.compress_mode = HI_COMPRESS_MODE_HFBC;        
chnParam.video_param.video_format = HI_VIDEO_FORMAT_TILE_64x16;        
chnParam.display_frame_num = 3;
chnParam.video_param.out_order = HI_VIDEO_OUT_ORDER_DISPLAY;

ret = hi_mpi_vdec_set_chn_param(chnId, &chnParam);

// 4.解码器启动接收码流
ret = hi_mpi_vdec_start_recv_stream(chnId);

// 5.发送码流
// 5.1 申请输入内存
uint8_t* inputAddr = nullptr;
// inputsize表示每一帧码流占用的内存大小，此处以1024 Byte为例，用户需根据实际情况计算内存大小
int32_t inputSize = 1024;
ret = hi_mpi_dvpp_malloc(0, &inputAddr, inputSize);

// 直接将输入码流数据读入Device内存
// 将输入码流读入Device内存中，该自定义函数ReadStreamFile由用户实现
ReadStreamFile(streamName, inputAddr, inputSize);

// 5.2 申请输出内存
uint8_t* outputAddr = nullptr;
// 输出图片数据占用的内存大小与输出图片格式有关
int32_t outputSize = 1920 * 1080 * 3 / 2;
ret = hi_mpi_dvpp_malloc(0, &outputAddr, outputSize);

// 5.3 构造存放一帧输入码流信息的结构体
hi_vdec_stream stream;
stream.addr = inputAddr;
stream.len = inputSize;
stream.end_of_frame = HI_TRUE;
stream.end_of_stream = HI_FALSE;
stream.need_display = HI_TRUE;

// 5.4 构造存放一帧输出结果信息的结构体
hi_vdec_pic_info outPicInfo;
outPicInfo.width = 1920;
outPicInfo.height = 1080;
outPicInfo.width_stride = 1920;
outPicInfo.height_stride = 1080;
outPicInfo.pixel_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
outPicInfo.vir_addr = outputAddr;
outPicInfo.buffer_size = outputSize;

// 5.5 发送一帧码流
ret = hi_mpi_vdec_send_stream(chnId, &stream, &outPicInfo, 0);

// 6.接收解码结果
// 6.1 获取解码结果
hi_video_frame_info frame;    
hi_vdec_stream stream;
hi_vdec_supplement_info stSupplement;
ret = hi_mpi_vdec_get_frame(chnId, &frame, &stSupplement, &stream, 0);
if (ret == HI_SUCCESS) {
   decResult = frame.v_frame.frame_flag;
   if (decResult == 0) { // 0: Decode success
       printf("[%s][%d] Chn %u GetFrame Success, Decode Success \n",__FUNCTION__, __LINE__, chnId);
   } else if (decResult == 1) { // 1: Decode fail
       printf("[%s][%d] Chn %u GetFrame Success, Decode Fail \n",__FUNCTION__, __LINE__, chnId);
   } else if (decResult == 2) { // 2:This result is returned for the second field of
       printf("[%s][%d] Chn %u GetFrame Success, No Picture \n", __FUNCTION__, __LINE__, chnId);
   } else if (decResult == 3) { // 3: Reference frame number set error
       printf("[%s][%d] Chn %u GetFrame Success, RefFrame Num Error \n",__FUNCTION__, __LINE__, chnId);
   } else if (decResult == 4) { // 4: Reference frame size set error
       printf("[%s][%d] Chn %u GetFrame Success, RefFrame Size Error \n",__FUNCTION__, __LINE__, chnId);
  }
}

// 6.2 获取解码结果数据
// 可以直接使用VDEC的输出图片数据，在frame.v_frame.virt_addr[0]指向的内存中
// TODO: 推理相关的代码逻辑


// 6.3 释放输入、输出内存
ret = hi_mpi_dvpp_free(frame.v_frame.virt_addr[0]);
ret = hi_mpi_dvpp_free(stream.addr);

// 6.4 释放资源
ret = hi_mpi_vdec_release_frame(chnId, &frame);

// 7.解码器停止接收码流
ret = hi_mpi_vdec_stop_recv_stream(chnId);

// 8.销毁通道
ret = hi_mpi_vdec_destroy_chn(chnId);

// 9. 媒体数据处理系统去初始化
ret = hi_mpi_sys_exit();

// ....
```
