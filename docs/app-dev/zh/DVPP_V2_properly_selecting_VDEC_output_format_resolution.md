# 合理选择VDEC视频解码输出格式和分辨率，性能更优

## 背景说明

如果用户需要借助DVPP进行视频解码，想要得到RGB格式图片，在部分AI处理器上当前视频解码接口hi\_mpi\_vdec\_send\_stream支持输出YUV420SP格式或RGB888格式，且支持在解码时对图片进行缩放，所以从提升性能的角度，可以优化代码逻辑，直接调用视频解码接口hi\_mpi\_vdec\_send\_stream输出RGB888格式。

**图 1**  VDEC解码输出的组合场景  
![](figures/VDEC解码输出的组合场景-10.png "VDEC解码输出的组合场景-10")

## 基本原理

部分AI处理器上视频解码接口hi\_mpi\_vdec\_send\_stream支持输出YUV420SP格式或RGB888格式，可设置接口参数输出不同的格式，省去调用hi\_mpi\_vpc\_convert\_color进行格式转换的步骤，减少接口调用。

若视频码流分辨率与模型输入图片的分辨率不一致，需要对解码后的图片进行缩放处理，也可以在视频解码接口hi\_mpi\_vdec\_send\_stream中设置输出图片的分辨率，在解码的同时完成图片的缩放，省去单独调用缩放接口的步骤，减少接口调用。

总结下来，可以在视频解码接口hi\_mpi\_vdec\_send\_stream中完成解码+缩放+色域转换三个功能，减少调用接口的数量，提升性能。

## 使用示例

您可以单击[vdec\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/vdec_sample)获取样例。
