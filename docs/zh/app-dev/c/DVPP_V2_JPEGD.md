# JPEGD图片解码

本节介绍JPEGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

JPEGD（JPEG Decoder）负责完成图像解码功能，将.jpg、.jpeg、.JPG、.JPEG图片解码成YUV格式图片。关于JPEGD功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

**图 1**  JPEGD图片解码功能调用流程  
![](figures/JPEGD_API_call_process_V2.png "JPEGD图片解码功能调用流程")

当前系统支持解码JPEG图片，关键接口的说明如下：

1. 调用aclInit接口初始化系统。
2. 调用aclrtSetDevice接口指定计算设备。
3. 调用hi\_mpi\_sys\_init接口进行媒体数据处理系统初始化。
4. 调用hi\_mpi\_vdec\_create\_chn接口创建通道。
5. 调用hi\_mpi\_dvpp\_malloc接口申请Device上的内存，存放输入或输出数据。
6. 解码前，需调用hi\_mpi\_vdec\_start\_recv\_stream接口通知解码器启动接收码流，再调用hi\_mpi\_vdec\_send\_stream接口发送解码码流，hi\_mpi\_vdec\_send\_stream接口是异步接口，调用该接口仅表示任务下发成功，还需要调用hi\_mpi\_vdec\_get\_frame接口获取解码结果数据，成功获取解码数据后，可以调用hi\_mpi\_vdec\_release\_frame接口释放帧相关的资源。解码结束后，需调用hi\_mpi\_vdec\_stop\_recv\_stream接口通知解码器停止接收码流。
7. 调用hi\_mpi\_dvpp\_free接口释放输入、输出内存。
8. 调用hi\_mpi\_vdec\_destroy\_chn接口销毁通道。
9. 调用hi\_mpi\_sys\_exit接口进行媒体数据处理系统去初始化。
10. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
11. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 示例代码

以下是JPEGD图片解码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id1 -->
您可以单击[jpegd\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/jpegd_sample)获取样例。
<!-- end id1 -->

```cpp
// ....

// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_vdec_chn chnId;
hi_vdec_chn_attr chnAttr;

chnAttr.type = HI_PT_JPEG;
chnAttr.mode = HI_VDEC_SEND_MODE_FRAME;
chnAttr.pic_width = 1920;
chnAttr.pic_height = 1080;
chnAttr.stream_buf_size = 1920 * 1080;

ret = hi_mpi_vdec_create_chn(chnId, &chnAttr);

// 3.设置通道属性
hi_vdec_chn_param chnParam;
ret = hi_mpi_vdec_get_chn_param(chnId, &chnParam);

chnParam.pic_param.pixel_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
chnParam.pic_param.alpha = 255;
chnParam.display_frame_num = 0;
ret = hi_mpi_vdec_set_chn_param(chnId, &chnParam);

// 4.解码器启动接收码流
ret = hi_mpi_vdec_start_recv_stream(chnId);

// 5.发送码流
// 5.1 申请输入内存
uint8_t* inputAddr = nullptr;
// inputsize表示输入图片占用的内存大小，此处以1024 Byte为例，用户需根据实际情况计算内存大小
int32_t inputSize = 1024;
ret = hi_mpi_dvpp_malloc(0, &inputAddr, inputSize);
// 将输入图片读入内存中，该自定义函数ReadStreamFile由用户实现
ReadStreamFile(fileName, inputAddr, inputSize);

// 5.2 构造存放输入图片信息的结构体
hi_vdec_stream stStream{};
hi_img_info stImgInfo{};
stStream.pts = 0;
if (g_runMode == ACL_HOST) {
    stStream.addr  = (uint8_t *)hostInputAddr;
} else {
    stStream.addr  = (uint8_t *)inputAddr;
}
stStream.len = inputSize;
stStream.end_of_frame = HI_TRUE;
stStream.end_of_stream = HI_FALSE;
stStream.need_display  = HI_TRUE;

ret = hi_mpi_dvpp_get_image_info(HI_PT_JPEG, &stStream, &stImgInfo);
if (g_runMode == ACL_HOST) {
    // 如果不使用Host上的数据，需及时释放
   aclrtFreeHost(hostInputAddr);
    hostInputAddr = nullptr;
}
stStream.addr = (uint8_t *)inputAddr;

// 5.3 构造存放输出图片信息的结构体，并申请输出内存
hi_vdec_pic_info outPicInfo{};
void *outBuffer = nullptr;
outPicInfo.width  = stImgInfo.width;
outPicInfo.height = stImgInfo.height;
outPicInfo.width_stride  = stImgInfo.width_stride;
outPicInfo.height_stride = stImgInfo.height_stride;
outPicInfo.buffer_size   = stImgInfo.img_buf_size;
outPicInfo.pixel_format  = HI_PIXEL_FORMAT_UNKNOWN;

ret = hi_mpi_dvpp_malloc(0, &outBuffer, outPicInfo.buffer_size);

outPicInfo.vir_addr = (uint64_t)outBuffer;

// 5.4 发送需解码的输入图片
ret = hi_mpi_vdec_send_stream(chnId, &stStream, &outPicInfo, 0);

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
   } else { // Decode fail
       printf("[%s][%d] Chn %u GetFrame Success, Decode Fail \n",__FUNCTION__, __LINE__, chnId);
   }
}

// 6.2 获取JPEGD的输出图片数据，在frame.v_frame.virt_addr[0]指向的内存中
......

// 6.3 释放输入、输出内存
ret = hi_mpi_dvpp_free(frame.v_frame.virt_addr[0]);
ret = hi_mpi_dvpp_free(stream.addr);

// 6.4 释放资源
ret = hi_mpi_vdec_release_frame(chnId, &frame);

// 7.解码器停止接收码流
ret = hi_mpi_vdec_stop_recv_stream(chnId);

// 8.销毁通道
ret = hi_mpi_vdec_destroy_chn(chnId);

// 9.媒体数据处理系统去初始化
ret = hi_mpi_sys_exit();

// ....
```
