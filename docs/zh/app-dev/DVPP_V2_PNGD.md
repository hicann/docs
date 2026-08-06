# PNGD图片解码

本节介绍PNGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

PNGD（PNG decoder）负责PNG格式图片的解码。关于PNGD功能的详细介绍及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

**图 1**  PNGD图片解码功能调用流程  
![](figures/PNGD图片解码功能调用流程.png "PNGD图片解码功能调用流程")

当前系统支持解码PNG图片，关键接口的说明如下：

1. 调用aclInit接口初始化系统。
2. 调用aclrtSetDevice接口指定计算设备。
3. 调用hi\_mpi\_sys\_init接口进行媒体数据处理系统初始化。
4. 调用hi\_mpi\_pngd\_create\_chn接口创建通道。
5. 调用hi\_mpi\_dvpp\_malloc接口申请Device上的内存，存放输入或输出数据。
6. 调用hi\_mpi\_pngd\_send\_stream接口发送解码码流，hi\_mpi\_pngd\_send\_stream接口是异步接口，调用该接口仅表示任务下发成功，还需要调用hi\_mpi\_pngd\_get\_image\_data接口获取解码结果数据。
7. 调用hi\_mpi\_dvpp\_free接口释放输入、输出内存。
8. 调用hi\_mpi\_pngd\_destroy\_chn接口销毁通道。
9. 调用hi\_mpi\_sys\_exit接口进行媒体数据处理系统去初始化。
10. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
11. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 示例代码

以下是PNGD图片解码功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id1 -->
您可以单击[pngd\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/pngd_sample)获取样例。
<!-- end id1 -->

```cpp
// ....

// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_pngd_chn chnId;
hi_pngd_chn_attr chnAttr; // hi_pngd_chn_attr是保留参数，无需设置
ret = hi_mpi_pngd_create_chn(chnId, &chnAttr);

// 3.发送码流
// 3.1 申请输入内存
uint8_t* inputAddr = nullptr;
// inputsize表示输入图片占用的内存大小，此处以1024 byte为例，用户需根据实际情况计算内存大小
int32_t inputSize = 1024;
ret = hi_mpi_dvpp_malloc(0, &inputAddr, inputSize);
// 将输入图片读入内存中，该自定义函数ReadStreamFile由用户实现
ReadStreamFile(fileName, inputAddr, inputSize);

// 3.2 构造存放输入图片信息的结构体
hi_img_stream stStream{};
hi_img_info stImgInfo{};
stStream.pts = 0;
if (g_runMode == ACL_HOST) {
    stStream.addr  = (uint8_t *)hostInputAddr;
} else {
    stStream.addr  = (uint8_t *)inputAddr;
}
stStream.len  = inputSize;
stStream.type = HI_PT_PNG;

ret = hi_mpi_png_get_image_info(&stStream, &stImgInfo);
if (g_runMode == ACL_HOST) {
    // 如果不使用Host上的数据，需及时释放
   aclrtFreeHost(hostInputAddr);
    hostInputAddr = nullptr;
}
stStream.addr = (uint8_t *)inputAddr;

// 3.3 构造存放输出图片信息的结构体，并申请输出内存
hi_pic_info outPicInfo{};
void *outBuffer = nullptr;
outPicInfo.picture_width  = stImgInfo.width;
outPicInfo.picture_height = stImgInfo.height;
outPicInfo.picture_width_stride  = stImgInfo.width_stride;
outPicInfo.picture_height_stride = stImgInfo.height_stride;
outPicInfo.picture_buffer_size   = stImgInfo.img_buf_size;
outPicInfo.picture_format = HI_PIXEL_FORMAT_UNKNOWN;

ret = hi_mpi_dvpp_malloc(0, &outBuffer, outPicInfo.buffer_size);

outPicInfo.picture_address = (uint64_t)outBuffer;

// 3.4 发送需解码的输入图片
ret = hi_mpi_pngd_send_stream(chnId, &stream, &outPicInfo, 0);

// 4.接收解码结果
// 4.1 获取解码结果
hi_pic_info picInfo;
hi_img_stream stream;
ret = hi_mpi_pngd_get_image_data(chnId, &picInfo, &stream, 0);
if (ret == HI_SUCCESS) { // Decode success
    printf("[%s][%d] Chn %u GetFrame Success, Decode Success \n",__FUNCTION__, __LINE__, chnId);
} else if (ret == HI_ERR_PNGD_BUF_EMPTY){ // Decoding
    printf("[%s][%d] Chn %u Decoding, try again \n",__FUNCTION__, __LINE__, chnId);
} else { // Decode fail
    printf("[%s][%d] Chn %u GetFrame Success, Decode Fail \n",__FUNCTION__, __LINE__, chnId);
}

// 4.2 获取PNGD的输出图片数据，在outputPic.picture_address指向的内存中
......

// 4.3 释放输入、输出内存
ret = hi_mpi_dvpp_free(frame.v_frame.virt_addr[0]);
ret = hi_mpi_dvpp_free(stream.addr);

// 5.销毁通道
ret = hi_mpi_pngd_destroy_chn(chnId);

// 6.媒体数据处理系统去初始化
ret = hi_mpi_sys_exit();

// ....
```
