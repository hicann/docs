# 多帧码流当一帧送入解码导致VDEC视频解码异常

## 问题现象描述

解码发生丢帧，有ERROR日志。

Device日志示例如下：

```bash
User send more than one stream data, but only send one outbuf
```

>**说明：** 
>EP模式下，运行解码进程后，登录Host，在有读、写、执行权限的目录下执行**msnpureport -a**命令，可导出Device的日志信息。
>RC模式下，登录板端环境，执行**cat /proc/umap/vdec**命令，可导出解码相关信息。

## 原因分析

VDEC视频解码当前仅支持按帧发送模式，因此调用hi\_mpi\_vdec\_send\_stream接口时，要求用户每次送入独立的一帧码流数据以及对应的输出buffer，当用户一次送入多帧数据（即输入码流内存中有多帧码流数据），这时VDEC视频解码时除了第一帧解码成功外，其余帧都会被丢弃，同时打印ERROR日志。

## 解决方法

需排查代码逻辑，检查hi\_mpi\_vdec\_send\_stream接口的输入码流内存（stream-\>addr参数）中是否一次读入多帧数据，若是则需调整代码逻辑。
