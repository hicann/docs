# Kernel Execution Error of the AI CPU Operator

## Symptom

An error is reported during Runtime execution. The Runtime error message "PrintAicpuErrorInfo" is printed in the application run logs.

In  Ascend EP  form, the application run logs,  **plog-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/plog**  by default.

In  Ascend RC  form, the application run logs,  **device-app-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-app-_pid_**  by default.

```text
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [engine.cc:1103]16282 ReportExceptProc:Task exception! device_id=0, stream_id=7, task_id=2, type=1, retCode=0x2a, [aicpu exception].
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:669]16282 ProcessAicpuErrorInfo:report error module_type=0, module_name=E39999
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:669]16282 ProcessAicpuErrorInfo:An exception occurred during AICPU execution, stream_id:7, task_id:2, errcode:5, msg:aicpu execute failed.
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:1050]16282 PreCheckTaskErr:report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:1050]16282 PreCheckTaskErr:Kernel task happen error, retCode=0x2a, [aicpu exception].
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:759]16282 PrintAicpuErrorInfo:report error module_type=0, module_name=E39999
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:759]16282 PrintAicpuErrorInfo:Aicpu kernel execute failed, device_id=0, stream_id=7, task_id=2.
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:777]16282 PrintAicpuErrorInfo:Aicpu kernel execute failed, device_id=0, stream_id=7, task_id=2, flip_num=0, fault so_name=, fault kernel_name=, fault op_name=Unique, extend_info=(info_type:4, info_len:6, msg_info:Unique).
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stream.cc:929]16243 GetError:[EXEC][DEFAULT]Stream Synchronize failed, stream_id=7, retCode=0x2a, [aicpu exception].
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stream.cc:932]16243 GetError:[EXEC][DEFAULT]report error module_type=0, module_name=E39999
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stream.cc:932]16243 GetError:[EXEC][DEFAULT]Aicpu kernel execute failed, device_id=0, stream_id=7, task_id=2, flip_num=0, fault so_name=, fault kernel_name=, fault op_name=Unique, extend_info=(info_type:4, info_len:6, msg_info:Unique)
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [logger.cc:305]16243 StreamSynchronize:[EXEC][DEFAULT]Stream synchronize failed, stream = 0x5643fe3e28d0
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:661]16243 rtStreamSynchronize:[EXEC][DEFAULT]ErrCode=507018, desc=[aicpu exception], InnerCode=0x715002a
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]16243 FuncErrorReason:[EXEC][DEFAULT]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]16243 FuncErrorReason:[EXEC][DEFAULT]rtStreamSynchronize execute failed, reason=[aicpu exception]
```

## Possible Cause

According to the error message in the log, the AI CPU operator fails to be executed. The possible causes are operator code errors, such as data input mismatch \(including data format or broadcast dimension\), out-of-bounds access, AI CPU thread suspension, and operator execution timeout \(30 seconds by default\).

>**NOTE:**
>In terms of the broadcast dimension constraint, for some operators implemented based on TensorFlow, after the axes that need to be broadcast contiguously and those that do not need to be broadcast continuously are combined, the number of dimensions must be less than 6. Otherwise, an error is reported.
>Example:
>
>- If a.shape=\(5, 1, 5, 1, 5, 1\) and b.shape=\(5, 5, 5, 5, 5, 5\) do not have axes to be combined, the final shape is 6D. In this case, an error is reported.
>- If a.shape=\(5, 1, 5, 5, 1, 1\) and b.shape=\(5, 5, 5, 5, 5, 5\) have the second and third dimensions not to be broadcast but the fourth and fifth dimensions to be broadcast contiguously, after the axes are combined, the final shape is 4D. In this case, the broadcast is successful.

Check the logs of the AI CPU to locate the error cause.

In  Ascend EP  form, the logs,  **device-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-_id_**  by default.

In  Ascend RC  form, the logs,  **device-app-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-app-_pid_**  by default.

- Example 1: The input data dimensions of the UniqueExt operator do not meet the requirements.

    ```text
    [ERROR] CCECPU(2309,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpu_tf_kernel.cc:348][tid:2317][TFAdapter] AICPUKernelAndDevice::Run failure, kernel_id=0, op_name=Unique, op_type=UniqueExt, error=Invalid argument: unique expects a 1D vector.
    [ERROR] CCECPU(2309,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [tf_adpt_session_mgr.cc:74][tid:2317][TFAdapter] [sessionID:0] Failed to Run kernel, kernel_id=0.
    [ERROR] CCECPU(2309,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [tf_adpt_session_mgr.cc:434][tid:2317][TFAdapter] [sessionID:0] Run kernel on session failed.
    [ERROR] CCECPU(2309,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [tf_adpt_api.cc:85][tid:2317][TFAdapter] [sessionID:0] Invoke TFOperateAPI failed.
    [ERROR] CCECPU(2309,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ae_kernel_lib_fwk.cc:229][TransformKernelErrorCode][tid:2317][AICPU_PROCESSER] Call tf api return failed:5, input param to tf api:0x124040017004
    [ERROR] CCECPU(2309,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpusd_event_process.cpp:1325][ExecuteTsKernelTask][tid:2317] Aicpu engine process failed, result[5].
    ```

- Example 2: The input data of the BitwiseXor operator has more than six dimensions and does not conform to the broadcast rule.

    Given a.shape=\[15, 15, 8, 18, 15, 7, 14\] and b.shape=\[3, 15, 1, 8, 1, 1, 7, 14\], the error cause is as follows:

    1. According to the broadcast rule, a.shape needs to be aligned with b.shape in dimensions and 1 is added to the left of a.shape. As a result, a\_new.shape=\[1, 15, 15, 8, 18, 15, 7, 14\] is created.
    2. According to the TensorFlow broadcast rule, the fourth and fifth dimensions of a\_new.shape and b.shape need to be broadcast, while the sixth and seventh dimensions do not. After the axes are combined, the final shape is 6D. In this case, the broadcast fails.

    ```text
    [ERROR] CCECPU(12226,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpu_tf_kernel.cc:363][ProcessKernelRunOutput][tid:12236][TFAdapter]AICPUKernelAndDevice::Run failure, kernel_id=10000, op_name=BitwiseXor, op_type=BitwiseXor, error=UNIMPLEMENTED: Broadcast between [15,15,8,18,15,7,14] and [3,15,1,8,1,1,7,14] is not supported yet.
    [ERROR] CCECPU(12226,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpu_tf_kernel_cache.cc:273][RunKernel][tid:12236][TFAdapter]Failed to Run kernel, kernel_id=10000.
    [ERROR] CCECPU(12226,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [tf_adpt_api.cc:86][APIInternalImpl][tid:12236][TFAdapter][sessionID:18446744073709551535] Invoke TFOperateAPI failed.
    [ERROR] CCECPU(12226,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ae_kernel_lib_fwk.cc:352][TransformKernelErrorCode][tid:12236][AICPU_PROCESSER] Call tf api return failed:5, returncode:5, input param to tf api:0x12c100340004
    [ERROR] CCECPU(12226,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpusd_event_process.cpp:1690][PostProcessTsKernelTask][tid:12236] Aicpu engine process failed, result[5], opName[BitwiseXor].
    ```

- Example 3: The execution of the RealDiv operator timed out.

    ```text
    [ERROR] CCECPU(21711,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpusd_monitor.cpp:437][HandleTaskTimeout][tid:21724] Send timeout to tsdaemon, tsdaemon will kill aicpu-sd process, thread index[2], op name[RealDiv], serialNo=279, stream_id=7, task_id=6812, nowTick:1846897065957, startTick:1845482875742, timeOut:1400000000, tickFreq:50000000.
    ```

## Solution

Check whether the operator code is correct. For example, check the dimension and format of the input data, out-of-bounds access, and execution timeout.

After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the fault persists.
