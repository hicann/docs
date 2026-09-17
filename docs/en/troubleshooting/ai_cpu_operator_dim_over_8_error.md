# Number of Dimensions of the AI CPU Operator Exceeds 8

## Symptom

An error is reported during GE execution. The GE error messages "ReportErrMessage" and "shape dim num should be less than 8" are displayed in the application run log.

In  Ascend EP  form, the application run logs,  **plog-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/plog**  by default.

In  Ascend RC  form, the application run logs,  **device-app-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-app-_pid_**  by default.

```text
[ERROR] OP(1491846,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpu_ext_info_handle.cpp:290][NNOP][UpdateShape][1491965] errno[561000] OpName:[aclnnGatherV2_0_GatherV2AiCPU] shape dim num should be less than 8, but got [9].
[INFO] GE(1491846,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:411]1491965 ReportErrMessage:report error_message, error_code:EZ9999, work_stream_id:149186091965, error_mode:0.
[ERROR] OP(1491846,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpu_ext_info_handle.cpp:290][NNOP][UpdateShape][1491965] errno[561000] OpName:[aclnnGatherV2_0_GatherV2AiCPU] shape dim num should be less than 8, but got [9].
[INFO] GE(1491846,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:411]1491965 ReportErrMessage:report error_message, error_code:EZ9999, work_stream_id:149186091965, error_mode:0.
[ERROR] OP(1491846,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [aicpu_ext_info_handle.cpp:101][NNOP][AppendExtInfoShape][1491965] errno[561000] OpName:[aclnnGatherV2_0_GatherV2AiCPU] Assert ((UpdateShape(shape, &inputs[index])) == OK) failed
```

## Possible Cause

The number of dimensions of the input/output parameter of the AI CPU operator exceeds the upper limit \(8 dimensions\).

## Solution

Modify the input/output dimensions of the operator parameters to ensure that the number of dimensions does not exceed 8.

After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the fault persists.
