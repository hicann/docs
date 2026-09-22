# 采用VPC批处理接口，降低时延，性能更优

## 背景说明

在对图像进行抠图、缩放等处理时，媒体数据处理部分提供了以下两类接口：

- 一次处理一张图片，例如hi\_mpi\_vpc\_crop\_resize\_make\_border接口

    该方式下，如果存在多张输入图片，一般都采用for循环的方式，针对每张图片，都调用一次hi\_mpi\_vpc\_crop\_resize\_make\_border接口。

- 一次处理多张图片（即批处理接口），例如hi\_mpi\_vpc\_batch\_crop\_resize\_make\_border接口

    该方式下，如果存在多张输入图片，只需调用一次hi\_mpi\_vpc\_batch\_crop\_resize\_make\_border接口。

以上两类接口的对应关系表如下。

| 单张图片处理接口 | 批量图片处理接口 |
| --- | --- |
| hi_mpi_vpc_crop_resize_paste（抠图缩放贴图） | hi_mpi_vpc_batch_crop_resize_paste（批量抠图缩放贴图） |
| hi_mpi_vpc_crop_resize_make_border（抠图缩放填充） | hi_mpi_vpc_batch_crop_resize_make_border（批量抠图缩放填充） |

## 基本原理

AI处理器内置图像处理单元DVPP（Digital Video Pre-Processing），在DVPP中，有多个VPC（Vision Preprocessing Core）模块，处理图片的抠图、缩放、格式转换等任务。

在调用批处理接口时，批量任务会被均分到多个VPC模块、并行处理，批量接口的处理时延会降低，性能提升。

## 使用示例

此处以批量抠图、缩放、填充为例说明如何调用多功能组合接口hi\_mpi\_vpc\_batch\_crop\_resize\_make\_border。

您可以单击[sample\_comm\_vpc\_batchCropResizeMakeBorder](https://gitee.com/ascend/samples/blob/master/cplusplus/level1_single_api/7_dvpp/vpc_sample/src/common/sample_comm_vpc_batchCropResizeMakeBorder.cpp)获取样例。
