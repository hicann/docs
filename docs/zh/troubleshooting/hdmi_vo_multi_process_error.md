# HDMI与VO模块多进程时报错

## 适用场景

- 业务场景：通过vo模块及HDMI接口送显
- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

在执行通过VO模块及HDMI接口送显业务时，在日志中产生如下的不支持多进程错误。

```bash
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.632.632 [klogd.c:246][3146.786343] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.632.666 [klogd.c:246][3146.786375] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.647.470 [klogd.c:246][3146.793796] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.662.320 [klogd.c:246][3146.801217] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.662.343 [klogd.c:246][3146.808650] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.662.353 [klogd.c:246][3146.816065] [drv_vo][ERR][vo open:433]:VO functions must work in the same pid!!!
[ERROR] DSS(5303,vo test nvr hdmi hi test):2023-01-01-08:52:26.669.726 [mpi hdmi com.c:264][Lib_hdmi][mpi hdmi_com_init]:open HDMI err.
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:26.678.229 [klogd.c:246][3146.823479] [drv_hdmi][ERR][hdmi file open:2750]:HDMI functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:38.192.079 [klogd.c:246][3158.345748] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:38.192.199 [klogd.c:246][3158.345800] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
[ERROR] KERNEL(3720,sklogd):2023-01-01-08:52:38.207.148 [klogd.c:246][3158.353257] [drv_vo][ERR][vo_open:433]:VO functions must work in the same pid!!!
```

## 可能原因

有其他调用了VO、HDMI接口的用例在后台执行。

## 处理步骤

1. 检查是否通过mobax等软件开启了多个端口并正在执行调用了VO、HDMI接口的用例。
2. 检查后台是否有其他调用了VO、HDMI接口的用例，命令: ps -elf。
3. 关闭其他调用了VO、HDMI接口的用例。
4. 再次执行通过VO模块及HDMI接口送显业务用例。
