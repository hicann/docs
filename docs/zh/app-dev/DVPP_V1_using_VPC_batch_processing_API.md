# 采用VPC批处理接口，降低时延，性能更优

## 背景说明

在对图像进行抠图、缩放等处理时，媒体数据处理部分提供了以下两类接口：

- 一次处理一张图片，例如acldvppVpcCropAsync接口

    该方式下，如果存在多张输入图片，一般都采用for循环的方式，针对每张图片，都调用一次acldvppVpcCropAsync接口。

- 一次处理多张图片（即批处理接口），例如acldvppVpcBatchCropAsync接口

    该方式下，如果存在多张输入图片，只需调用一次acldvppVpcBatchCropAsync接口。

以上两类接口的对应关系表如下。

| 单张图片处理接口 | 批量图片处理接口 |
| --- | --- |
| acldvppVpcCropAsync（抠图） | acldvppVpcBatchCropAsync（批量抠图） |
| acldvppVpcCropResizeAsync（抠图缩放） | acldvppVpcBatchCropResizeAsync（批量抠图缩放） |
| acldvppVpcCropAndPasteAsync（抠图贴图） | acldvppVpcBatchCropAndPasteAsync（批量抠图贴图） |
| acldvppVpcCropResizePasteAsync（抠图缩放贴图） | acldvppVpcBatchCropResizePasteAsync（批量抠图缩放贴图） |
| - | acldvppVpcBatchCropResizeMakeBorderAsync（批量抠图缩放填充） |

## 基本原理

AI处理器内置图像处理单元DVPP（Digital Video Pre-Processing），在DVPP中，有多个VPC（Vision Preprocessing Core）模块，处理图片的抠图、缩放、格式转换等任务。

在调用批处理接口时，批量任务会被均分到多个VPC模块、并行处理，批量接口的处理时延会降低，性能提升。

## 使用示例

此处以批量抠图、缩放为例说明如何调用批处理接口acldvppVpcBatchCropResizeAsync，完整代码请您可以单击[batchcrop](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/0_data_process/batchcrop)获取样例。
