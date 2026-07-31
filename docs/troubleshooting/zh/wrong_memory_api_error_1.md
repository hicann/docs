# 调用错误的内存申请接口，导致内存地址校验出错

## 问题现象描述

日志报错如下：

```bash
address check failed ret 0x3, please check: 1. use hi_mpi_dvpp_malloc or aclDvppMalloc to alloc dvpp memory; 2. current buffer size 3110400 may be larger than actually allocated.
```

## 可能原因

根据日志提示，可能由于：

1. 没有使用指定的DVPP内存申请接口;
2. 接口传入的buffer size小于实际申请的内存大小。

## 处理步骤

检查代码：

1. 是否使用媒体数据处理V1版本中的acldvppMalloc接口/媒体数据处理V2版本中的hi\_mpi\_dvpp\_malloc接口申请存放JPEGD图片解码/VDEC视频解码输入或输出数据的内存;
2. 对于DVPP内存申请接口，增加日志打印内存大小及地址，检查接口hi\_mpi\_vdec\_get\_frame/aclvdecSendFrame/acldvppJpegDecodeAsync送入的buffer size是否超出了实际申请的内存区域。
