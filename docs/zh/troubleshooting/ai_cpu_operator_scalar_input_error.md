# AI CPU算子输入标量执行报错

## 问题现象

Host侧Runtime执行报错，在应用程序运行日志中Runtime打印了PrintAicpuErrorInfo错误信息。

Ascend EP形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/plog路径下，日志文件为plog-_pid\_\*_.log。

```bash
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.791.865 [engine.cc:1103]16282 ReportExceptProc:Task exception! device_id=0, stream_id=7, task_id=2, type=1, retCode=0x2a, [aicpu exception].
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.793.489 [device_error_proc.cc:669]16282 ProcessAicpuErrorInfo:report error module_type=0, module_name=E39999
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.793.498 [device_error_proc.cc:669]16282 ProcessAicpuErrorInfo:An exception occurred during AICPU execution, stream_id:7, task_id:2, errcode:5, msg:aicpu execute failed.
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.793.932 [task.cc:1050]16282 PreCheckTaskErr:report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.793.941 [task.cc:1050]16282 PreCheckTaskErr:Kernel task happen error, retCode=0x2a, [aicpu exception].
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.793.981 [task.cc:759]16282 PrintAicpuErrorInfo:report error module_type=0, module_name=E39999
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.793.990 [task.cc:759]16282 PrintAicpuErrorInfo:Aicpu kernel execute failed, device_id=0, stream_id=7, task_id=2.
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.116 [task.cc:777]16282 PrintAicpuErrorInfo:Aicpu kernel execute failed, device_id=0, stream_id=7, task_id=2, flip_num=0, fault so_name=, fault kernel_name=, fault op_name=Unique, extend_info=(info_type:4, info_len:6, msg_info:Unique).
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.384 [stream.cc:929]16243 GetError:[EXEC][DEFAULT]Stream Synchronize failed, stream_id=7, retCode=0x2a, [aicpu exception].
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.407 [stream.cc:932]16243 GetError:[EXEC][DEFAULT]report error module_type=0, module_name=E39999
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.419 [stream.cc:932]16243 GetError:[EXEC][DEFAULT]Aicpu kernel execute failed, device_id=0, stream_id=7, task_id=2, flip_num=0, fault so_name=, fault kernel_name=, fault op_name=Unique, extend_info=(info_type:4, info_len:6, msg_info:Unique)
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.482 [logger.cc:305]16243 StreamSynchronize:[EXEC][DEFAULT]Stream synchronize failed, stream = 0x5643fe3e28d0
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.510 [api_c.cc:661]16243 rtStreamSynchronize:[EXEC][DEFAULT]ErrCode=507018, desc=[aicpu exception], InnerCode=0x715002a
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.519 [error_message_manage.cc:49]16243 FuncErrorReason:[EXEC][DEFAULT]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.532 [error_message_manage.cc:49]16243 FuncErrorReason:[EXEC][DEFAULT]rtStreamSynchronize execute failed, reason=[aicpu exception]
```

同时Device侧执行报错，查阅具体的AI CPU日志，这里以**GatherV2算子**报错为例，其输入参数Shape Size报错。

Ascend EP形态，日志默认在$HOME/ascend/log/\[run|debug\]/device-_id_路径下，日志格式为device-pid\_\*.log。

Ascend RC形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/device-app-_pid_路径下，日志文件为device-app-_pid_\_\*.log。

```bash
[ERROR] AICPU(28880,aicpu_scheduler):2025-03-05-17:32:22.832.371 [gatherv2.cc:157][GetInputAndCheck][tid:28891]Shape must be at least rank [1] but is rank [0]
[ERROR] AICPU(28880,aicpu_scheduler):2025-03-05-17:32:22.832.384 [gatherv2.cc:173][Compute][tid:28891]GetInputAndCheck failed
[ERROR] CCECPU(28880,aicpu_scheduler):2025-03-05-17:32:22.832.408 [ae_kernel_lib_aicpu.cc:300][TransformKernelErrorCode][tid:28891][AICPU_PROCESSER] call aicpu api RunCpuKernel in libcpu_kernels.so failed, ret:4294967295.
[ERROR] CCECPU(28880,aicpu_scheduler):2025-03-05-17:32:22.832.425 [aicpusd_event_process.cpp:666][PostProcessTsKernelTask][tid:28891] Aicpu engine process failed, result[4294967295], opName[GatherV2], streamId[2], taskId[0].
```

## 可能原因

部分AI CPU算子输入不支持零维Tensor（即标量）。

## 解决方法

将算子输入的标量按照1维Tensor创建。

若仍无法解决，  您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
