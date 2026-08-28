# 调用错误的内存申请接口，导致内存地址校验出错

## 问题现象描述

日志报错如下：

- 日志1

    ```bash
    device:0 chan 0, venc or jpege input buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or acldvppMalloc.
    ```

- 日志2

    ```bash
    device:0 chan 0, venc or jpege output buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or acldvppMalloc.
    ```

- 日志3

    ```bash
    device:0 chan 0, jpege input buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or acldvppMalloc.
    ```

- 日志4

    ```bash
    device:0 chan 0, jpege output buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or acldvppMalloc.
    ```

## 可能原因

根据日志提示，是由于没有使用指定的接口申请内存。

## 处理步骤

使用媒体数据处理V1版本中的acldvppMalloc接口/媒体数据处理V2版本中的hi\_mpi\_dvpp\_malloc接口申请DVPP内存，存放JPEGE图片编码/VENC视频编码输入或输出数据。
