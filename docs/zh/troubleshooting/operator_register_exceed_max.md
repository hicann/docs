# 注册算子数超过最大规格

## 问题现象描述

推理过程中，用户load model出现报错。

日志中包含ProgramRegister:Program register failed, program out of xxx和Register binary failed关键信息，日志示例如下：

```bash
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [runtime.cc:967]3093 ProgramRegister:Program register failed, program out of 40000000
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [logger.cc:23]3093 DevBinaryRegister:Register binary failed.
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:127]3093 rtDevBinaryRegister:ErrCode=507032, desc=[program register num out of use], InnerCode=0x7090007
[ERROR] RUNTIME(3093,rtstest_host):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:26]3093 ReportFuncErrorReason:rtDevBinaryRegister execute failed, reason=[program register num out of use]
```

## 可能原因

通过日志分析报错的原因可能是一个进程内算子等资源注册超过最大规格。

## 处理步骤

针对上述可能原因，可以按以下方式处理：

- 分析model，简化模型或者降低动态batch档次。
- 算子数是进程资源，model太大的情况下建议一个进程open一个device。
- 避免同一算子在不同模型中反复注册。
- 注册算子数不超过最大规格。
