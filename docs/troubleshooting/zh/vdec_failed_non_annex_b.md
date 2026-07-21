# 非annex-B格式的码流导致VDEC视频解码失败

## 问题现象描述

解码失败。

日志示例如下：

```bash
pid 0 usr chn 0 device 0 video format unsupport at event chn 0
```

或

```bash
pid 0 usr chn 0 device 0 chn 0, input stream error, can't decode, report to user
```

## 原因分析

VDEC视频解码模块目前只支持annex-B格式的裸码流，不支持其它格式（例如AVCC格式）的裸码流。

## 解决方法

annex-B格式裸码流，码流样式如下，固定以0x00000001开始（以H264为例），建议用户使用第三方工具打开码流，以16进制方式查看码流并排查格式。

![](figures/zh-cn_image_0000001927835353.png)
