# VPC参数校验失败

## 问题现象描述

调用VPC功能接口返回0xA0078003，即HI\_ERR\_VPC\_ILLEGAL\_PARAM，参数超出合法范围。查看日志有类似如下报错信息，不同版本的报错日志可能存在差别：

- VPC缩放宽大于输出宽日志信息（1）：

    ```bash
    resize width (224) is greater than output width (120)
    ```

    或

    ```bash
    width should be in [10, 32768], width is 654321
    ```

- VPC抠图宽大于输入宽日志信息（2）：

    ```bash
    crop width 120 cannot be greater than input width 100
    ```

- 输入的缩放算法不正确日志信息（3）：

    ```bash
    resize interpolation [8] is not supported
    ```

    或

    ```bash
    flip mode[5] not supported, support mode [0, 1, 2]
    ```

- 图片内存大小不够日志信息（4）：

    ```bash
    buffer size(50176) is smaller than need buffer size(95264) when format is 1
    ```

    或

    ```bash
    buffer size(50176) is smaller than need buffer size(95264) when format is 1
    ```

- 图片地址校验失败日志信息（5）：

    ```bash
    on device 0, num 0 input addr (start 0x100020003000 end 0x100020004000) is illegal
    ```

    或

    ```bash
    buffer address is null
    ```

- VPC抠图的输出宽大于输入宽或者输出高大于输入高日志信息（6）：

    ```bash
    crop width[300] or height[300] is greater than input width[224] or height[224]
    ```

## 可能原因

针对上面日志信息分析，可能存在以下对应原因：

- 日志信息（1）：VPC缩放宽大于输出宽
- 日志信息（2）：VPC抠图宽大于输入宽

- 日志信息（3）：输入的缩放算法不正确
- 日志信息（4）：图片内存大小不够
- 日志信息（5）：图片地址校验失败
- 日志信息（6）：VPC抠图的输出宽大于输入宽或者输出高大于输入高

## 定位思路

1. 根据日志描述的错误信息，找到VPC对应的配置参数，根据提示进行修改。
2. 根据日志描述的错误信息，参考[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)中的“媒体数据处理V1 API \> VPC图像处理功能”或“媒体数据处理V2 API \> VPC图像处理功能”章节的约束修改。

## 解决方法

根据提示的错误信息进行修改：

1. 如果为日志信息（1），修改resize宽，使其小于等于输出宽。
2. 如果为日志信息（2）和（6），修改抠图宽，使其小于输入宽。
3. 如果为日志信息（3），修改缩放算法为当前版本支持的类型。
4. 如果为日志信息（4），需要按照格式申请足够的内存，并正确配置buffer\_size。
5. 如果为日志信息（5），使用hi\_mpi\_dvpp\_malloc或acldvppMalloc申请图片地址。
