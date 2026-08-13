# 算子执行过程中D2D拷贝出错

## 问题现象

参见[收集进程中断问题信息](collect_process_interrupt_info.md)收集日志文件，收集的日志所存放的目录，下文以$\{HOME\}/err\_log\_info/为例。

Host应用类日志（$\{HOME\}/err\_log\_info/log/\[run|debug\]/plog/plog-_pid_\_\*.log）日志中存在SDMA任务（即D2D拷贝任务）执行报错的信息，日志示例如下，YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。

```bash
[ERROR] RUNTIME(33549,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:1226]122568 ProcessStarsSdmaErrorInfo:[FINAL][FINAL]The error from device(chipId:7, dieId:0), serial number is 1. there is a fftsplus sdma error, sdma channel is 6, sdmaState=0x6, sdmaTslotid=0x5, sdmaCxtid=0x1, sdmaThreadid=0x0, irqStatus=0x420000, cqeStatus=0x150000.
```

## 故障根因

根据日志信息，获取cqeStatus=0x150000，将该参数值向右移1位cqeStatus\>\>1，可计算出真正的错误码code=000Ah，该错误码的含义如下：

| 错误码 | 描述 | 可能原因 |
| --- | --- | --- |
| 000Ah | SDMAA上报的错误，表示SDMAA搬运过程中出现COMPDATAERR。 | 数据异常，访问HBM返回error。<br>一般出现该报错大概率是HBM比特ECC故障了。 |

## 解决方法

在Device的slog日志（slog/dev-os-_id_/run/event/event\_\*.log）中搜索“**event\_id**”关键字，并获取其参数值（该参数值就是故障码），然后再单击《[健康管理故障定义](https://support.huawei.com/enterprise/zh/ascend-computing/ascend-hdk-pid-252764743)》获取对应版本的手册，并查找该故障的解决方法。
