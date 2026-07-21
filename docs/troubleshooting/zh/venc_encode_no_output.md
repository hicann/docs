# VENC编码无输出

## 问题现象描述

VENC通道创建，发送帧都成功，但调用VENC获取码流的接口hi\_mpi\_venc\_get\_stream返回0xa008800e，获取不到编码后码流数据。

## 可能原因

可能原因有以下：

- 用户传入的图像帧内存不是使用dvpp内存申请接口hi\_mpi\_dvpp\_malloc申请的。
- 用户传入的图像帧内存和分辨率不匹配。
- OS内存管理出现问题。

## 处理步骤

针对分析的可能原因，请参考以下方法处理：

- 查看日志是否有出现看门狗相关的打印，如下图所示，如果出现看门狗，基本可以确认是内存使用存在问题

    ```bash
    [Chnl]:chnl_watch_dog_timer_isr [Line]:1141 find VEDU_0  down,now reset it
    [Chnl]:chnl_watch_dog_blackbox [Line]:1097 vpu_id is 0, venc watchdog fail enter blackbx
    ```

- 排查用户代码中输入图像帧的内存申请方式，如果不是使用dvpp内存申请接口hi\_mpi\_dvpp\_malloc申请的，VENC芯片将无法正常访问该内存，导致编码无输出，需要修改为使用hi\_mpi\_dvpp\_malloc申请输入内存。
- 排查输入图像帧的内存和分辨率是否不匹配，比如NV12或NV21格式的YUV，一帧图像大小为宽x高x1.5，如果实际送给VENC的内存大小比设置的分辨率宽x高x1.5小的话，会产生访问越界等不可预期的行为，也会导致编码无输出。需要保证申请的内存大小和实际设置的分辨率参数匹配。
- 如果以上排查都不存在问题，可能是OS的内存管理出现问题。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
