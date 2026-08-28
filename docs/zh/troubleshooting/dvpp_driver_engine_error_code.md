# DVPP驱动引擎异常返回码

## 问题现象描述

视频解码失败，Device日志提示-512返回码：\[dvpp\_ioctl\_vpc 845\] call proc failed:-512, engine\_id:1，如下所示。

```bash
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067669] [dvpp] [dvpp_print_vpc_job 156] outctl out2_select:0
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067672] [dvpp] [dvpp_print_vpc_job 184] OUT
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067673] [dvpp] [dvpp_print vpc_job 185] out use_flag:1
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067675] [dvpp] [dvpp_print_vpc_job 186] wr0 addr_frame_start:ffff35a00000
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067677] [dvpp] [dvpp_print_vpc_job 187] wr1 addr_frame_start:ffff35aca800
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067679] [dvpp] [dvpp_print_vpc_job 188] wr2 addr_frame_start:0
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067680] [dvpp] [dvpp_print_vpc_job 189] wr3 addr_frame_start:0
[ERROR] KERNEL(1200,sklogd):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [8078.067693] [dvpp] [dvpp_ioctl_vpc 845] call proc failed:-512, engine_id:1
```

## 可能原因

根据日志信息，判断为VPC引擎返回的异常码，再根据-512返回码可以判断为等待视频解码异常中断。可能原因：用户态进程退出，导致等待解码时被异常中断。

## 解决方法

查看Host侧的日志文件，检查用户态进程异常退出原因。

## 其他异常码参考

除样例VPC引擎返回的-512异常码外，DVPP驱动引擎还有其他引擎及各自的返回码，如表1所示。

您可以参考上述样例的方法，根据自身业务类型及Device日志文件中记录的异常返回码信息，先判断返回异常码的引擎类型，再根据返回码数值获取对应的返回码说明，初步判断故障原因。

**表 1**  DVPP驱动引擎异常返回码

| 引擎类型 | 驱动IOCTL返回码 | 返回码说明 | 常见错误日志参考 |
| --- | --- | --- | --- |
| JPEGE | -22 | 参数错误或者不支持 | 常见错误打印：<br><br>  - 返回值-35：日志“JPEGE time wait, engine_id:xx”编码超时（执行器输入编码参数不对等导致）。<br>  - 返回值-512：日志“Signal interrupted, engine_id:xx”编码错误（编码被异常中断）。 |
| -11 | 引擎处理异常，需要重试 |  |  |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -35 | 编码超时 |  |  |
| -5 | 编码失败且复位成功 |  |  |
| 5 | 编码失败且复位失败 |  |  |
| -512 | 等待编码时被异常中断 |  |  |
| PNGD | -22 | 参数错误或者不支持 | 常见错误打印：<br><br>  - 返回值5/-5：日志1“Time out: wait failed xx”解码超时（图片格式不正确等码流异常等导致）。<br>  - 返回值5/-5：日志2“Signal interrupted:xx, engine_id:xx”解码时被异常中断。 |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -5 | 解码失败且复位成功 |  |  |
| 5 | 解码失败且复位失败 |  |  |
| JPEGD | -22 | 参数错误或者不支持或者解码成功但是重置寄存器失败 | 常见错误打印：<br><br>  - 返回值-1/-23：日志“Decode abnormal, abnormal status:xx decode error! engine id:xx”硬件上报异常中断（图片格式不正确等码流异常导致）。<br>  - 返回值-2/-24：日志“Decode abnormal, abnormal status:xx  decode over time!, engine id:xx”解码超时（总线繁忙，系统缺页等导致）。 |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -1 | 解码失败且复位成功 |  |  |
| -2/-3 | 解码超时且复位成功 |  |  |
| -23 | 解码失败并且复位失败 |  |  |
| -24/-25 | 解码超时并且复位失败 |  |  |
| VPC | -22 | 参数错误或者不支持 | 常见错误打印：<br><br>  - 返回值-35：日志“dvpp_vpc_engine_proc pipe wait time out: engine id:xx”解码超时（总线繁忙、异常缺页等导致）。<br>  - 返回值-32：日志“Hardware process failed, engine id:xx”解码错误（码流异常等导致）。 |
| -11 | 引擎处理异常，需要重试 |  |  |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -35 | 解码超时 |  |  |
| -512 | 等待解码时被异常中断 |  |  |
| -32 | 硬件解码失败驱动捕捉到异常 |  |  |
| VPC_cmdlist | -22 | 参数错误或者不支持 | 常见错误打印：<br><br>  - 返回值-35：日志“dvpp_vpc_engine_proc pipe wait time out: engine id:xx”解码超时（总线繁忙、异常缺页等导致）。<br>  - 返回值-32：日志“Hardware process failed, engine id:xx”解码错误（码流异常等导致）。 |
| -11 | 引擎处理异常，需要重试 |  |  |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -35 | 解码超时 |  |  |
| -512 | 等待解码时被异常中断 |  |  |
| -32 | 硬件解码失败 |  |  |
| VENC | -22 | 参数错误或者不支持 | 常见错误打印：<br><br>  - 返回值-35：日志“wait timeout, Ret value is xx”未等到完成中断，编码失败（执行器配置参数错误或者总线繁忙等导致）。<br>  - 返回值-61：日志“venc err interrupt state = xx, wait_time_remain = xx”编码失败（执行器配置参数错误）。 |
| -11 | 引擎处理异常，需要重试 |  |  |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -35 | 未等到完成中断，编码失败 |  |  |
| -61 | 上报编码超时中断 |  |  |
| VDEC | -22 | 参数错误或者不支持 | 常见错误打印：<br><br>  - 返回值-35：日志“VDM wait time out,wait_time_remain = xx ,engine_id:xx”解码超时（码流异常、总线繁忙等导致）。<br>  - 返回值=-61：日志“wait_time_remain = xx,have vdm_error,p_vdm_backup_state->VdmState=xx ,engine_id:xx”上报解码错误中断（码流异常等导致）。 |
| -11 | 引擎处理异常，需要重试 |  |  |
| -14 | 拷贝用户态数据时地址异常或者释放引擎失败 |  |  |
| -16 | 申请引擎失败 |  |  |
| -35 | 解码超时 |  |  |
| -61 | 上报解码错误中断 |  |  |
| -4 | 等待解码被异常中断 |  |  |
