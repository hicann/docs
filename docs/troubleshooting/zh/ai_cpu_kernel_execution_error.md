# AI CPU算子Kernel执行报错

## 问题现象

Runtime执行报错，在应用程序运行日志中Runtime打印了PrintAicpuErrorInfo的错误信息。

Ascend EP形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/plog路径下，日志文件为plog-_pid\_\*_.log。

Ascend RC形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/device-app-_pid_路径下，日志文件为device-app-_pid_\_\*.log。

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

## 可能原因

从日志报错可知，AI CPU算子执行失败，可能算子本身代码问题：**数据输入不匹配（例如数据格式、广播维度等）、访问越界、AI CPU线程挂死、算子执行超时（默认不超过30秒）**等问题。

>**说明：** 
>对于**广播维度约束**：部分基于TensorFlow实现的算子，其连续需要广播的轴和连续不需要广播的轴合并之后的维度要求小于6，否则会执行报错。
>举例：
>
>- 若a.shape=\(5, 1, 5, 1, 5, 1\)，b.shape=\(5, 5, 5, 5, 5, 5\)，没有需要合并的轴，最后维度为6，广播报错。
>- 若a.shape=\(5, 1, 5, 5, 1, 1\)，b.shape=\(5, 5, 5, 5, 5, 5\)，在第2和3维都不需要广播，4和5维都需要广播，分别连续合并，合并后的维度为4，广播成功。

比如通过查阅AI CPU的日志，排查具体报错原因。

Ascend EP形态，日志默认在$HOME/ascend/log/\[run|debug\]/device-_id_路径下，日志格式为device-pid\_\*.log。

Ascend RC形态，日志默认在$HOME/ascend/log/\[run|debug\]/device-app-_pid_路径下，日志文件为device-app-_pid_\_\*.log。

- 样例1：UniqueExt算子输入数据维度不符合要求。

    ```bash
    [ERROR] CCECPU(2309,aicpu_scheduler):2022-09-22-11:27:00.733.218 [aicpu_tf_kernel.cc:348][tid:2317][TFAdapter] AICPUKernelAndDevice::Run failure, kernel_id=0, op_name=Unique, op_type=UniqueExt, error=Invalid argument: unique expects a 1D vector.
    [ERROR] CCECPU(2309,aicpu_scheduler):2022-09-22-11:27:00.733.242 [tf_adpt_session_mgr.cc:74][tid:2317][TFAdapter] [sessionID:0] Failed to Run kernel, kernel_id=0.
    [ERROR] CCECPU(2309,aicpu_scheduler):2022-09-22-11:27:00.733.261 [tf_adpt_session_mgr.cc:434][tid:2317][TFAdapter] [sessionID:0] Run kernel on session failed.
    [ERROR] CCECPU(2309,aicpu_scheduler):2022-09-22-11:27:00.733.277 [tf_adpt_api.cc:85][tid:2317][TFAdapter] [sessionID:0] Invoke TFOperateAPI failed.
    [ERROR] CCECPU(2309,aicpu_scheduler):2022-09-22-11:27:00.733.296 [ae_kernel_lib_fwk.cc:229][TransformKernelErrorCode][tid:2317][AICPU_PROCESSER] Call tf api return failed:5, input param to tf api:0x124040017004
    [ERROR] CCECPU(2309,aicpu_scheduler):2022-09-22-11:27:00.733.366 [aicpusd_event_process.cpp:1325][ExecuteTsKernelTask][tid:2317] Aicpu engine process failed, result[5].
    ```

- 样例2：BitwiseXor算子输入数据维度大于6维，不支持广播规则。

    已知a.shape=\[15,15,8,18,15,7,14\]，b.shape=\[3,15,1,8,1,1,7,14\]，报错原因如下：

    1. 根据广播规则，首先a需要向b维度看齐，左侧补1，结果为a\_new.shape\[1,15,15,8,18,15,7,14\]。
    2. 根据TensorFlow广播规则，a\_new和b的第4和5维需要广播、第6和7维不需要广播，分别连续合并，合并后的维度为6，广播失败。

    ```bash
    [ERROR] CCECPU(12226,aicpu_scheduler):2024-09-25-10:56:20.250.270 [aicpu_tf_kernel.cc:363][ProcessKernelRunOutput][tid:12236][TFAdapter]AICPUKernelAndDevice::Run failure, kernel_id=10000, op_name=BitwiseXor, op_type=BitwiseXor, error=UNIMPLEMENTED: Broadcast between [15,15,8,18,15,7,14] and [3,15,1,8,1,1,7,14] is not supported yet.
    [ERROR] CCECPU(12226,aicpu_scheduler):2024-09-25-10:56:20.250.315 [aicpu_tf_kernel_cache.cc:273][RunKernel][tid:12236][TFAdapter]Failed to Run kernel, kernel_id=10000.
    [ERROR] CCECPU(12226,aicpu_scheduler):2024-09-25-10:56:20.250.324 [tf_adpt_api.cc:86][APIInternalImpl][tid:12236][TFAdapter][sessionID:18446744073709551535] Invoke TFOperateAPI failed.
    [ERROR] CCECPU(12226,aicpu_scheduler):2024-09-25-10:56:20.250.334 [ae_kernel_lib_fwk.cc:352][TransformKernelErrorCode][tid:12236][AICPU_PROCESSER] Call tf api return failed:5, returncode:5, input param to tf api:0x12c100340004
    [ERROR] CCECPU(12226,aicpu_scheduler):2024-09-25-10:56:20.250.346 [aicpusd_event_process.cpp:1690][PostProcessTsKernelTask][tid:12236] Aicpu engine process failed, result[5], opName[BitwiseXor].
    ```

- 样例3：RealDiv算子执行时间超时。

    ```bash
    [ERROR] CCECPU(21711,aicpu_scheduler):2024-05-31-20:14:39.806.495 [aicpusd_monitor.cpp:437][HandleTaskTimeout][tid:21724] Send timeout to tsdaemon, tsdaemon will kill aicpu-sd process, thread index[2], op name[RealDiv], serialNo=279, stream_id=7, task_id=6812, nowTick:1846897065957, startTick:1845482875742, timeOut:1400000000, tickFreq:50000000.
    ```

## 解决方法

根据报错信息检查算子代码是否正确，包括检查输入的数据维度/格式、是否越界、是否超时等。

若仍无法解决，  您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
