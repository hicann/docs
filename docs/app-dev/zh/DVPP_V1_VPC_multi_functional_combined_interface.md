# 采用VPC多功能组合接口，减少系统调度压力，性能更优

## 背景说明

在对图像进行抠图、缩放、贴图、填充等处理时，媒体数据处理部分提供了以下实现功能的接口：

- 一个接口只做一次操作（即单功能接口），例如acldvppVpcCropAsync、acldvppVpcResizeAsync、acldvppVpcMakeBorderAsync接口

    该方式下，如果想实现多个功能，例如抠图+缩放+填充，您需要调用以上3个接口。

- 一个接口做多个操作（即多功能组合接口），例如：acldvppVpcBatchCropResizePasteAsync、acldvppVpcBatchCropResizeMakeBorderAsync接口

    该方式下，如果想实现多个功能，例如抠图+缩放+填充，您仅需要调用1个接口acldvppVpcBatchCropResizeMakeBorderAsync。

单功能接口与多功能组合接口的对应关系如下。

| 单功能接口 | 多功能组合接口 |
| --- | --- |
| - acldvppVpcCropAsync（抠图）<br>  - acldvppVpcResizeAsync（缩放） | - acldvppVpcCropResizeAsync（抠图缩放）或acldvppVpcBatchCropResizeAsync（批量抠图缩放）<br>  - acldvppVpcCropAndPasteAsync（抠图贴图）或acldvppVpcBatchCropAndPasteAsync（批量抠图贴图）<br>  - acldvppVpcCropResizePasteAsync（抠图缩放贴图）、acldvppVpcBatchCropResizePasteAsync（批量抠图缩放贴图） |
| - acldvppVpcCropAsync（抠图）<br>  - acldvppVpcResizeAsync（缩放）<br>  - acldvppVpcMakeBorderAsync（填充） | acldvppVpcBatchCropResizeMakeBorderAsync（批量抠图缩放填充） |

## 基本原理

一个接口内部会有多次Host和Device的任务交互，每次交互有时延，若对于抠图、缩放等多个功能，调用多次接口，Host和Device的任务交互次数就会增加，时延自然也会随之增加。

采用多个功能组合接口，调用一个接口完成多个功能，虽然是多个功能，但对于Device来说都是一次处理（一个多功能组合接口和一个单功能接口的硬件执行时间相同），相对调用多个单功能接口，能够减少Host和Device的调度次数，减少Device的处理次数，对调度和性能有较多的提升，在性能优化时可以考虑。

## 使用示例

此处以批量抠图、缩放为例说明如何调用多功能组合接口acldvppVpcBatchCropResizeAsync。

您可以单击[batchcrop](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/0_data_process/batchcrop)获取样例。
