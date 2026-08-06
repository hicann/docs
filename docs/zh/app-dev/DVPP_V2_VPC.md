# VPC图片处理典型功能

本节以抠图、缩放为例说明VPC图像处理时的接口调用流程，同时配合以下典型功能的示例代码辅助理解该接口调用流程。

VPC（Vision Preprocessing Core）负责图像处理功能，支持对图片做抠图、缩放、格式转换等操作。关于VPC功能的详细介绍以及使用约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 典型功能接口调用流程（以缩放为例）

**图 1**  缩放功能调用流程  
![](figures/缩放功能调用流程.png "缩放功能调用流程")

当前系统支持对输入图片做抠图、缩放等处理，关键接口的说明如下：

1. 调用aclInit接口初始化系统。
2. 调用aclrtSetDevice接口指定计算设备。
3. 调用hi\_mpi\_sys\_init接口进行**媒体数据处理系统初始化**。
4. 调用 hi\_mpi\_vpc\_sys\_create\_chn接口**创建通道**。
5. 调用hi\_mpi\_dvpp\_malloc接口**申请Device上的内存**，存放输入或输出数据。
6. **执行图像处理任务，**此步骤以缩放为例说明。

    调用hi\_mpi\_vpc\_resize接口，对图片进行缩放。hi\_mpi\_vpc\_resize接口是异步接口，调用该接口成功仅表示任务下发成功，还需要调用hi\_mpi\_vpc\_get\_process\_result接口等待任务完成。

    - 可以跟hi\_mpi\_vpc\_resize接口在同一个线程中调用hi\_mpi\_vpc\_get\_process\_result接口，也可以新起一个线程调用hi\_mpi\_vpc\_get\_process\_result接口，后者多线程并行，提高效率，但用户需自行实现线程间同步。
    - 调用缩放接口时，通过将输入图片和输出图片的格式设置成不同的，达到转换图片格式的目的。
    <!-- npu="950,A3,910b,910,310p,310b" id1 -->
    - 如果在Host上调用DVPP接口，图像处理的结果数据都在Device的内存中，如果想访问结果数据，需要将结果数据传输回Host侧。
    <!-- end id1 -->

7. 调用hi\_mpi\_dvpp\_free接口**释放输入、输出内存**。
8. 调用hi\_mpi\_vpc\_destroy\_chn接口**销毁通道**。
9. 调用hi\_mpi\_sys\_exit接口进行**媒体数据处理系统去初始化**。
10. 调用aclrtResetDevice接口复位设备，释放Device上的资源。
11. 调用aclFinalize接口实现系统去初始化，用于释放进程内acl接口使用的相关资源。

## 图片缩放示例代码

以下是图片缩放功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id2 -->
您可以单击[vpc\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/vpc_sample)获取样例。
<!-- end id2 -->

```cpp
// ....

// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_vpc_chn chnId;
hi_vpc_chn_attr stChnAttr;
ret = hi_mpi_vpc_sys_create_chn(&chnId, &stChnAttr);

// 3.执行缩放
// 3.1 构造存放输入图片信息的结构体
hi_vpc_pic_info inputPic;
inputPic.picture_width = 1920;
inputPic.picture_height = 1080;
inputPic.picture_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
inputPic.picture_width_stride = 1920;
inputPic.picture_height_stride = 1080;
inputPic.picture_buffer_size = inputPic.picture_width_stride * inputPic.picture_height_stride * 3 / 2;

// 3.2 准备输入图片数据
// 将输入图片读入Device内存中，该自定义函数ReadPicFile由用户实现
ReadPicFile(picName, inputPic.picture_address, inputPic.picture_buffer_size);

// 3.3 构造存放输出图片信息的结构体
hi_vpc_pic_info outputPic;
outputPic.picture_width = 960;
outputPic.picture_height  = 540;
outputPic.picture_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
outputPic.picture_width_stride = 960;
outputPic.picture_height_stride = 540;
outputPic.picture_buffer_size = outputPic.picture_width_stride * outputPic.picture_height_stride * 3 / 2;
ret = hi_mpi_dvpp_malloc(0, &outputPic.picture_address, outputPic.picture_buffer_size);

// 初始化内存
memset(outputPic.picture_address, 0, outputPic.picture_buffer_size);

// 3.4 调用缩放接口
uint32_t taskID = 0;
ret = hi_mpi_vpc_resize(chnId, &inputPic, &outputPic, 0, 0, 0, &taskID, -1);

// 3.5 等待任务处理结束，任务处理结束后，输出图片数据在outputPic.picture_address指向的内存中
uint32_t taskIDResult = taskID;
ret = hi_mpi_vpc_get_process_result(chnId, taskIDResult, -1);

// 3.6 VPC的输出图片数据可以直接作为模型推理的输入
// 可以直接使用VPC的输出图片数据，在outputPic.picture_address指向的内存中
// TODO：推理相关的代码逻辑


// 3.7 释放输入、输出内存
ret = hi_mpi_dvpp_free(inputPic.picture_address);
ret = hi_mpi_dvpp_free(outputPic.picture_address);

// 4.销毁通道
ret = hi_mpi_vpc_destroy_chn(chnId);

// 5. 媒体数据处理系统去初始化
ret = hi_mpi_sys_exit();

// ....
```

## 抠图示例代码

以下是抠图功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="310p" id3 -->
您可以单击[vpc\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/vpc_sample)获取样例。
<!-- end id3 -->

```cpp
// ....

// 1.初始化媒体数据处理系统
int32_t ret = hi_mpi_sys_init();

// 2.创建通道
hi_vpc_chn chnId;
hi_vpc_chn_attr stChnAttr;
ret = hi_mpi_vpc_sys_create_chn(&chnId, &stChnAttr);

// 3.执行抠图
// 3.1 构造存放输入图片信息的结构体
hi_vpc_pic_info inputPic;
inputPic.picture_width = 1920;
inputPic.picture_height = 1080;
inputPic.picture_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
inputPic.picture_width_stride = 1920;
inputPic.picture_height_stride = 1080;
inputPic.picture_buffer_size = inputPic.picture_width_stride * inputPic.picture_height_stride * 3 / 2;

// 3.2 准备输入图片数据
// 申请Device内存，用于媒体数据处理
ret = hi_mpi_dvpp_malloc(0, &inputPic.picture_address, inputPic.picture_buffer_size);

// 将输入图片读入Device内存中，该自定义函数ReadPicFile由用户实现
ReadPicFile(picName, inputPic.picture_address, inputPic.picture_buffer_size);

// 3.3 构造存放输出图片信息的结构体
// 该参数表示抠图数量
uint32_t multiCount = 1;
// cropRegionInfos数组的大小与抠图数量保持一致
hi_vpc_crop_region_info cropRegionInfos[1];
hi_vpc_pic_info outputPic;
for (uint32_t i = 0; i < multiCount; i++) {
    outputPic.picture_width = 960;
    outputPic.picture_height  = 540;
    outputPic.picture_format = HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420;
    outputPic.picture_width_stride = 960;
    outputPic.picture_height_stride = 540;
    outputPic.picture_buffer_size = outputPic.picture_width_stride * outputPic.picture_height_stride * 3 / 2;
    ret = hi_mpi_dvpp_malloc(0, &outputPic.picture_address, outputPic.picture_buffer_size);

    // 初始化内存
    memset(outputPic.picture_address, 0, outputPic.picture_buffer_size);
    
    // 表示从输入图片中抠出以左上角为原点、分辨率960*540的子图
    cropRegionInfos[i].dest_pic_info = outputPic;
    cropRegionInfos[i].crop_region.left_offset = 0;
    cropRegionInfos[i].crop_region.top_offset = 0;
    cropRegionInfos[i].crop_region.crop_width = 960;
    cropRegionInfos[i].crop_region.crop_height = 540;
}

// 3.4 调用抠图接口
uint32_t taskID = 0;
ret = hi_mpi_vpc_crop(chnId, &inputPic, cropRegionInfos, 1, &taskID, -1);

// 3.5 等待任务处理结束，任务处理结束后，输出图片数据在outputPic.picture_address指向的内存中
uint32_t taskIDResult = taskID;
ret = hi_mpi_vpc_get_process_result(chnId, taskIDResult, -1);

// 3.6 VPC的输出图片数据可以直接作为模型推理的输入
// 可以直接使用VPC的输出图片数据，在outputPic.picture_address指向的内存中
// TODO：推理相关的代码逻辑

// 3.7 释放输入、输出内存
ret = hi_mpi_dvpp_free(inputPic.picture_address);
inputPic.picture_address = nullptr;
for (uint32_t i = 0; i < multiCount; i++) {
     hi_mpi_dvpp_free(cropRegionInfos[i].dest_pic_info.picture_address);
     cropRegionInfos[i].dest_pic_info.picture_address = nullptr;
}

// 4.销毁通道
ret = hi_mpi_vpc_destroy_chn(chnId);

// 5. 媒体数据处理系统去初始化
ret = hi_mpi_sys_exit();

// ....
```
