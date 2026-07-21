# VDEC视频解码花屏

## 问题现象描述

输入码流给VDEC进行解码，得到的解码数据不正确，产生花屏现象，如图1所示。并且日志中存在类似“decode error”、“input stream error, can't decode, report to user”、“num\_ref\_idx\_l0\_active\(30\) out of range\(0,16\)”、“dvpp\_vdec\_vdm\_process failed”、“Chan 0 ErrRatio = 44”信息。

**图 1**  视频花屏  
![](figures/video_artifacts.png "视频花屏")

## 可能原因

输入的码流中某些帧数据不完整、存在坏帧，导致硬件解码产生花屏。

## 处理步骤

针对可能原因分析，参考以下步骤处理：

1. 检查输入的源码流是否有问题。

    使用第三方工具（如：eseye u等）对输入码流进行解码播放，查看是否存在花屏，若不花屏则进行第2步；若花屏则替换输入码流。

2. 若查看的源码流结果为正常，则可能码流在传输给设备侧VDEC的过程中遭到破坏，需要在调用发送码流接口之前，通过fwrite函数将输送给VDEC的码流保存下来。
    - 使用第三方工具对保存的码流进行检查，如果码流异常，用户需自行排查将码流送进去之前是否有送流问题。

    - 通过对应版本的sample，解码这段保留下来的码流，验证码流是否正常或VDEC是否支持该格式。

        如果sample解码正常，那就是开发本身的代码逻辑有问题，可以参考[《应用开发C&C++》](https://hiascend.com/document/redirect/cannCommunityadev)中的“专用加速器 \> 媒体数据处理（DVPP）\> 媒体数据处理V1 \>VDEC视频解码”或“专用加速器 \> 媒体数据处理（DVPP）\> 媒体数据处理V2 \>VDEC视频解码”章节优化代码逻辑。
