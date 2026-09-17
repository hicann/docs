# D2D Copy Error During Operator Execution

## Symptom

Collect the log file by referring to  [Collect Information About Process Interruption](collect_process_interrupt_info.md). The following uses  **$\{HOME\}/err\_log\_info/**  as an example of directory for storing collected logs.

The host application log file \(**$\{HOME\}/err\_log\_info/log/\[run|debug\]/plog/plog-_pid_\_\*.log**\) contains the error information about the execution of the SDMA task \(D2D copy task\). A log example is as follows:

```text
[ERROR] RUNTIME(33549,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:1226]122568 ProcessStarsSdmaErrorInfo:[FINAL][FINAL]The error from device(chipId:7, dieId:0), serial number is 1. there is a fftsplus sdma error, sdma channel is 6, sdmaState=0x6, sdmaTslotid=0x5, sdmaCxtid=0x1, sdmaThreadid=0x0, irqStatus=0x420000, cqeStatus=0x150000.
```

## Fault Root Causes

Based on the log information, obtain  **cqeStatus=0x150000**  and shift the parameter value rightwards by one digit \(**cqeStatus\>\>1**\) to compute the actual error code  **000Ah**. The meaning of it is as follows.

| Error Code | Description | Possible Cause |
| --- | --- | --- |
| 000Ah | SDMAA error: COMPDATAERR in SDMAA transfer | The data is abnormal. An error is returned when the HBM is accessed.<br>Generally, there is a high probability that the HBM bit ECC is faulty. |

## Solution

Search for the keyword  **event\_id**  in the slog file \(**slog/dev-os-_id_/run/event/event\__\*_.log**\) of the device, obtain the parameter value \(error code\), click  _[Health Management Fault Definition](https://support.huawei.com/enterprise/en/ascend-computing/ascend-hdk-pid-252764743)_  to obtain the manual of the corresponding version, and find the solution to the fault.
