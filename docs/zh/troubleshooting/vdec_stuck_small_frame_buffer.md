# 解码器帧存大小以及参考帧个数设置过小，VDEC视频解码卡住

## 问题现象描述

解码卡住，日志中提示无法申请帧存的相关错误。

Device日志示例如下：

```bash
pid 0 usr chn 0 device 0 chn 0, user set frame buffer size(1000 Byte) and ref frame num(5) is not enough for actual frame buffer size(2000 Byte) and actual ref frame num(7), pic width = 1280, height = 720, bit_width =8
```

>**说明：** 
>EP模式下，运行解码进程后，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令，可导出Device的日志信息。
>RC模式下，登录板端环境，执行**cat /proc/umap/vdec**命令，可导出解码相关信息。

## 原因分析

解码器内部需要申请一定个数的帧存，在进行帧存自适应时，如果用户创建通道时设置的**帧存大小\*帧存个数**小于实际所需要的**帧存大小\*帧存个数**，则解码时会失败。

## 解决方法

在调用hi\_mpi\_vdec\_create\_chn接口创建解码通道时，调整传入的帧存大小和帧存个数的值，即attr-\>frame\_buf\_size、attr-\>frame\_buf\_cnt参数，或者直接将这两个参数设置为0，由解码器内部自适应。
