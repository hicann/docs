# Input Scalar Execution Error of the AI CPU Operator

## Symptom

An error is reported during Runtime execution on the host. The Runtime error message "PrintAicpuErrorInfo" is printed in the application run logs.

In  Ascend EP  form, the application run logs,  **plog-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/plog**  by default.

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

An error is reported during execution on the device. Check the specific AI CPU log. The following uses the GatherV2 operator as an example. An error is reported for the input parameter  **Shape Size**.

In  Ascend EP  form, the logs,  **device-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-_id_**  by default.

In  Ascend RC  form, the application run logs,  **device-app-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-app-_pid_**  by default.

```text
[ERROR] AICPU(28880,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [gatherv2.cc:157][GetInputAndCheck][tid:28891]Shape must be at least rank [1] but is rank [0]
[ERROR] AICPU(28880,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [gatherv2.cc:173][Compute][tid:28891]GetInputAndCheck failed
[ERROR] CCECPU(28880,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ae_kernel_lib_aicpu.cc:300][TransformKernelErrorCode][tid:28891][AICPU_PROCESSER] call aicpu api RunCpuKernel in libcpu_kernels.so failed, ret:4294967295.
[ERROR] CCECPU(28880,aicpu_scheduler):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpusd_event_process.cpp:666][PostProcessTsKernelTask][tid:28891] Aicpu engine process failed, result[4294967295], opName[GatherV2], streamId[2], taskId[0].
```

## Possible Cause

Some AI CPU operator inputs do not support 0D tensors \(scalars\).

## Solution

Create the scalar input of the operator as a 1D tensor.

After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the fault persists.
