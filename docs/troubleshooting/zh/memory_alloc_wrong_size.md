# 使用正确的内存申请接口，但内存大小传值错误

## 问题现象描述

不同版本的报错日志可能存在差别：

- 日志示例1

    ```bash
    buffer size(3110400) is smaller than need buffer size(4147200) when format is 3.
    ```

- 日志示例2

    ```bash
    device 0, vpc end address is illegal, check allocated buffer size: configured buffer size: 3110400, current pic: format 3 width_stride 1920 height_stride 1080.
    ```

- 日志示例3

    ```bash
    dvpp_check_mem_usable [Line]:85 mem:0x****f000****4020 is not usable, please check:1. mem not allocated or has been freed;2. make sure mem actual size should be:8017920
    ```

## 可能原因

1. 代码中申请的内存大小小于该格式所需的输入或输出内存大小;
2. VPC任务接口传入的buffer size正常，与输入格式匹配，但是超出了实际申请的内存长度，所以校验出来结束地址非法。

## 解决方法

1. 检查代码，根据[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)中的“媒体数据处理V1 API \> VPC图像处理功能”或“媒体数据处理V2 API \> VPC图像处理功能”，检查对应格式的内存大小要求;
2. 在代码中增加打印内存长度的日志，检查VPC任务接口传入的buffer size是否与实际申请的内存长度一致。
