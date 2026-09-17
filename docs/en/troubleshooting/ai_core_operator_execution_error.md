# Execution Error of the AI Core Operator

## Symptom

An error is reported during Runtime execution. Key information about  **fault** **kernel\_name**  and  **func\_name**  is printed in the application run logs.

In  Ascend EP  form, the application run logs,  **plog-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/plog**  by default.

In  Ascend RC  form, the application run logs,  **device-app-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-app-_pid_**  by default.

```text
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [engine.cc:1103]4150867 ReportExceptProc:[EXEC][DEFAULT]Task exception! device_id=0, stream_id=20, task_id=1, type=13, retCode=0x91, [the model stream execute failed].
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:495]4150867 PrintCoreErrorInfo:[EXEC][DEFAULT]The error from device(0), serial number is 193, there is an aicore error, core id is 8, error code = 0x800000, dump info: pc start: 0x800120080047000, current: 0x1200800471cc, vec error info: 0x7cafc4e, mte error info: 0x3000052, ifu error info: 0xc33f87bd7a80, ccu error info: 0xffd2bbd5005fe9d7, cube error info: 0x84, biu error info: 0, aic error mask: 0x65000200d000288, para base: 0x120080016300, errorStr: The DDR address of the MTE instruction is out of range.
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:526]4150867 PrintCoreErrorInfo:[EXEC][DEFAULT]report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:526]4150867 PrintCoreErrorInfo:[EXEC][DEFAULT]The extend info from device(0), serial number is 193, there is aicore error, core id is 8, aicore int: 0x10, aicore error2: 0, axi clamp ctrl: 0, axi clamp state: 0x1717, biu status0: 0x101d14000000000, biu status1: 0x80000201020000, clk gate mask: 0, dbg address: 0, ecc en: 0, mte ccu ecc 1bit error: 0x2e80000000000000, vector cube ecc 1bit error: 0, run stall: 0x1, dbg data0: 0, dbg data1: 0, dbg data2: 0, dbg data3: 0, dfx data: 0x8b
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:1021]4150867 PrintErrorInfo:[EXEC][DEFAULT]Aicore kernel execute failed, device_id=0, stream_id=23, report_stream_id=20, task_id=24, flip_num=0, fault kernel_name=16805736118314619649-1_0_1_Add_35, func_name=te_add_729e2a87c649f49de98ac1a6fd491b3262ee7db9c1c2d6f4add7d7439aa3d22e_1__kernel0, program id=22, hash=3338199064661472585.
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:3275]4150867 ReportErrorInfo:[EXEC][DEFAULT]model execute error, retCode=0x91, [the model stream execute failed].
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:3247]4150867 PrintErrorInfo:[EXEC][DEFAULT]model execute task failed, device_id=0, model stream_id=20, model task_id=1, flip_num=0, model_id=3, first_task_id=65535
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stream.cc:929]4150867 GetError:[EXEC][DEFAULT]Stream Synchronize failed, stream_id=20, retCode=0x91, [the model stream execute failed].
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cc:581]4150867 SynchronizeExecute:[EXEC][DEFAULT]Fail to synchronize forbidden stream_id=20, retCode=0x7150050!
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cc:605]4150867 GetStreamToSyncExecute:[EXEC][DEFAULT]report error module_type=0, module_name=EE9999
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cc:605]4150867 GetStreamToSyncExecute:[EXEC][DEFAULT]Model synchronize execute failed, model_id=3!
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [logger.cc:856]4150867 ModelExecute:[EXEC][DEFAULT]Execute model failed.
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:2063]4150867 rtModelExecute:[EXEC][DEFAULT]ErrCode=507011, desc=[the model stream execute failed], InnerCode=0x7150050
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]4150867 FuncErrorReason:[EXEC][DEFAULT]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]4150867 FuncErrorReason:[EXEC][DEFAULT]rtModelExecute execute failed, reason=[the model stream execute failed]
```

## Possible Cause

According to the error message in the log, the AI Core operator execution failure is possibly caused by operator code errors, such as data input mismatch, out-of-bounds access, and computation overflow/underflow.

View the plog and obtain the names of the operator and function that report the error based on  **fault kernel\_name**  and  **func\_name**.

```text
[ERROR] RUNTIME(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:1021]4150867 PrintErrorInfo:[EXEC][DEFAULT]Aicore kernel execute failed, device_id=0, stream_id=23, report_stream_id=20, task_id=24, flip_num=0, fault kernel_name=16805736118314619649-1_0_1_Add_35, func_name=te_add_729e2a87c649f49de98ac1a6fd491b3262ee7db9c1c2d6f4add7d7439aa3d22e_1__kernel0, program id=22, hash=3338199064661472585.
```

## Solution

Contact technical support for troubleshooting.

## Possible Fault

In the model offloading scenario, the acl API error message "Execute model failed" may be displayed in the plog.

```text
[ERROR] ASCENDCL(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cpp:699]4150867 ModelExecute: [EXEC][DEFAULT][Exec][Model]Execute model failed, ge result[507011], modelId[1]
[ERROR] ASCENDCL(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cpp:1547]4150867 aclmdlExecute: [EXEC][DEFAULT][Exec][Model]modelId[1] execute failed, result[507011]
```

In the non-model offloading scenario, an operator execution failure may occur. The acl API error message "get op desc failed" and Runtime error message "Aicore kernel execute failed" are displayed in the plog.

```text
[ERROR] RUNTIME(2856615,xaclfk):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:1058]2856939 PreCheckTaskErr:[EXEC][DEFAULT]Kernel task happen error, retCode=0x26, [aicore exception].
[ERROR] RUNTIME(2856615,xaclfk):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task.cc:1029]2856939 PrintErrorInfo:[EXEC][DEFAULT]Aicore kernel execute failed, device_id=0, stream_id=0, report_stream_id=0, task_id=615, flip_num=0, fault kernel_name=12646006_1663210912148832_-1_0_while/transformer_0/decoder/layer_0/rnn/rnn/while/Select, func_name=te_select_7b314df6791292127cb82df985d04ddaf6d069cb31aaccec00e0b8ee2e997f20_1__kernel0, program id=131, hash=14736095126365135477.
[ERROR] GE(2856615,xaclfk):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [graph_execute.cc:557]2856939 GetOpDescInfo: ErrorNo: 4294967295(failed) [EXEC][DEFAULT][Get][OpDescInfo] failed, device_id:0, stream_id:0, task_id:615.
[ERROR] GE(2856615,xaclfk):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ge_executor.cc:1332]2856939 GetOpDescInfo: ErrorNo: 4294967295(failed) [EXEC][DEFAULT][Get][OpDescInfo] failed, device_id:0, stream_id:0, task_id:615.
[ERROR] ASCENDCL(2856615,xaclfk):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cpp:2216]2856939 aclmdlCreateAndGetOpDesc: [EXEC][DEFAULT][Get][OpDescInfo]get op desc failed, ge result[-1], deviceId[0], streamId[0], taskId[615]
```
