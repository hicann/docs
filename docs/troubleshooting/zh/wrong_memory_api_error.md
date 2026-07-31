# 调用错误的内存申请接口，导致内存地址校验出错

## 问题现象描述

调用VPC接口，返回HI\_ERR\_VPC\_BADADDR （0xA0078011）错误码，同时日志中有错误提示，不同版本的报错日志可能存在差别：

- 日志示例1

    ```bash
    device 0, vpc address is illegal, please make sure it has been allocated with hi_mpi_dvpp_malloc or acldvppMalloc.
    ```

- 日志示例2

    ```bash
    dvpp_check_mem_usable [Line]:85 mem:0x****f000****4020 is not usable, please check:1. mem not allocated or has been freed;2. make sure mem actual size should be:8017920
    ```

## 可能原因

根据日志提示，是由于没有使用指定的接口申请内存。

## 解决方法

检查代码，是否使用媒体数据处理V1版本中的acldvppMalloc接口/媒体数据处理V2版本中的hi\_mpi\_dvpp\_malloc接口申请存放VPC输入或输出数据的内存。
