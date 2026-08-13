# HDMI OPEN失败

## 适用场景

- 业务场景：通过HDMI接口送显
- 适用处理器：Atlas 200I/500 A2 推理产品
- 处理器形态：EP、RC

## 问题现象描述

在执行HDMI接口送显业务时，在日志中产生如下HDMI OPEN失败的用户态错误：

```bash
[ERROR] DSS(4808,vo_test_nvr_hdmi_hi_test):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [mpi_hdmi_com.c:338][lib_hdmi][mpi_hdmi_com_open]:HDMI device not init
```

## 可能原因

调用hi\_mpi\_hdmi\_open接口前没有调用hi\_mpi\_hdmi\_init接口。

## 处理步骤

1. 检查用例中hi\_mpi\_hdmi\_open接口、hi\_mpi\_hdmi\_init接口的调用顺序，修正用例。
2. 再次执行hdmi接口送显用例。
