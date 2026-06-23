# 合理选择VDEC视频解码输出格式和分辨率，性能更优

## 背景说明

如果用户需要借助DVPP进行视频解码，想要得到RGB格式图片，在部分AI处理器上，当前视频解码接口aclvdecSendFrame支持输出YUV420SP格式或RGB888格式，且支持在解码时对图片进行缩放，所以从提升性能的角度，可以优化代码逻辑，直接调用视频解码接口aclvdecSendFrame输出RGB888格式。

**图 1**  VDEC解码输出的组合场景  
![](figures/VDEC解码输出的组合场景.png "VDEC解码输出的组合场景")

## 基本原理

部分AI处理器上视频解码接口aclvdecSendFrame支持输出YUV420SP格式或RGB888格式，可设置接口参数输出不同的格式，省去调用acldvppVpcConvertColorAsync进行格式转换的步骤，减少接口调用。

若视频码流分辨率与模型输入图片的分辨率不一致，需要对解码后的图片进行缩放处理，也可以在视频解码接口aclvdecSendFrame中设置输出图片的分辨率，在解码的同时完成图片的缩放，省去单独调用缩放接口的步骤，减少接口调用。

总结下来，可以在视频解码接口aclvdecSendFrame中完成解码+缩放+色域转换三个功能，减少调用接口的数量，提升性能。

## 使用示例

您可以单击[vdec\_resnet50\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vdec_resnet50_classification)获取样例。

如果视频解码需要输出RGB888格式，并且同时实现缩放功能，您需要设置aclvdecSendFrame接口的output参数（表示输出图片描述信息）中的图片格式、宽、高、宽Stride、高Stride，例如：

```cpp
//创建输出图片描述信息
acldvppPicDesc picOutputDesc = acldvppCreatePicDesc();

//定义输出图片格式、宽、高、宽Stride、高Stride以及存放输出图片数据的内存
uint32_t width = 224;
uint32_t height = 224;
uint32_t widthStride = 224 * 3;
uint32_t heightStride = 224;
uint32_t size = widthStride * heightStride;
void *picOutBufferDev = nullptr;
acldvppMalloc(&picOutBufferDev, size);

//设置输出图片格式、宽、高、宽Stride、高Stride以及存放输出图片数据的内存
acldvppSetPicDescData(picOutputDesc, picOutBufferDev);
acldvppSetPicDescSize(picOutputDesc, size);
acldvppSetPicDescFormat(picOutputDesc, PIXEL_FORMAT_RGB_888);
acldvppSetPicDescWidth(picOutputDesc, width);
acldvppSetPicDescHeight(picOutputDesc, height);
acldvppSetPicDescWidthStride(picOutputDesc, widthStride);
acldvppSetPicDescHeightStride(picOutputDesc, heightStride);

//调用解码接口
aclvdecSendFrame(channelDesc, picInputDesc, picOutputDesc, nullptr, nullptr);
```
