# 实际码流类型与接口中设置的解码器类型不一致导致VDEC视频解码失败

## 问题现象描述

每一帧解码都失败。

Device日志示例如下：

```bash
temporal_id(-1) is not supported.
sps id 2 is larger than 2.
pid 2487 usr chn 4 device 0 video format unsupport at event chn 4
```

>**说明：** 
>Ascend EP形态下，运行解码进程后，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令，可导出Device的日志信息。
>Ascend RC形态下，登录板端环境，执行**cat /proc/umap/vdec**命令，可导出解码相关信息。

## 原因分析

创建VDEC视频解码通道时，需设置解码协议类型，VDEC视频解码涉及HI\_PT\_H264、HI\_PT\_H265两种类型，若设置的解码协议类型与实际解码码流的类型不一致时，会出现以上解码失败问题。

## 解决方法

需排查hi\_mpi\_vdec\_create\_chn接口传入的入参，attr-\>type是HI\_PT\_H264还是HI\_PT\_H265，并和码流实际类型做对比。
