# 送帧太快，VDEC视频解码发生OOM

## 问题现象描述

进行多路解码时，送帧间隔设置太短，导致发帧过快，出现OOM现象，解码卡住。

Device日志示例如下：

```bash
OOM_NOTIFIER: oom type 2
```

>**说明：** 
>EP模式下，运行解码进程后，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令，可导出Device的日志信息。
>RC模式下，登录板端环境，执行**cat /proc/umap/vdec**命令，可导出解码相关信息。

## 原因分析

每送一帧数据都需要申请一个输出buffer，当送帧间隔设置太短时，远远超过解码帧率时，则需申请大量的输出buffer，占用大量的内存，导致产生OOM。

## 解决方法

参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)中的VDEC性能指标数据，自行调整送帧间隔。
