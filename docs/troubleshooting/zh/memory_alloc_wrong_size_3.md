# 使用正确的内存申请接口，但内存大小传值错误

## 问题现象描述

日志报错如下：

```bash
device:0 chan 0, output terminal address is invalid, maybe outBufSize:3110400 is invalid.
```

## 可能原因

传入的buffer size太大，超出了实际申请的buffer范围，导致内部结束地址校验出错。

## 处理步骤

如果内存申请接口使用正常，业务流程中dvpp内存申请接口增加地址及长度日志，检查接口hi\_mpi\_venc\_send\_frame/hi\_mpi\_venc\_send\_jpege\_frame/aclvencSendFrame/acldvppJpegEncodeAsync传入buffer长度是否一致。
