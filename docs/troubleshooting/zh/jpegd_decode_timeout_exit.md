# JPEGD图像解码进程超时退出

## 问题现象描述

用户进程退出。

查看应用类日志，发现类似ERROR日志“task timeout, userData= ..., timeout=30, duration=…”和WARNING日志“frames statistic: ACL receive\(_n_\), send\(_n_-1\)”，_n_表示处理任务数量，需根据实际情况确定。

日志片段举例如下：

```bash
[ERROR] AICPU(pid,pName):DateTimeMS [dvpp_timeout_manager.cc:33][OnPulse][tid:2581][DVPP_KERNELS] WaitId[10] task timeout, userData=0xe7ffe0001280, timeout=30, duration=30.930062.
[INFO] AICPU(pid,pName):DateTimeMS [dvpp_kernel_base.cc:222][SendTaskCompleteToTs][tid:2581][DVPP_KERNELS] Send task complete to ts success, taskId=2, streamId=44, errorCode=1.
[WARNING] DVPP(pid,pName):DateTimeMS [JpegdAsyncManager.cpp:405][API] [PrintFrameCount:405] [T208] DFX[JPEGD]: frames statistic: ACL receive(16), send(15)
```

## 可能原因

多路并发解码JPEG图片场景下，如果每一路解码的JPEG图片中，都包含带旋转信息的大分辨率图片，例如3840\*2160分辨率及以上的图片，则可能导致图片解码时间过长，从而导致用户进程超时退出。

## 处理步骤

1. 确定大分辨率的图片是否包含旋转信息。

    使用JPEG码流分析工具（例如JPEGsnoop）解析大分辨率的图片，查看其是否包含旋转信息，若Orientation信息为1，则表示不旋转；否则，都带有一定角度的旋转，例如下图解析出来的Orientation信息为8，表示顺时针旋转270°。

    ![](figures/zh-cn_image_0000001881876542.png)

2. 如果确定这些图片是带旋转的大分辨率图片，则建议用户先调用第三方库（例如OpenCV）进行解码。
