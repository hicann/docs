# DVPP Engine Error

## Symptom

Video decoding fails. The error message "\[dvpp\_ioct1\_vpc 845\] call proc failed:-512, engine\_id:1" is displayed in the device log, as shown in the following:

```text
[ERROR] KERNEL(1200,sklogd):2019-11-29-21:42:07.421.714 [8078.067669] [dvpp] [dvpp_print_vpc_job 156] outctl out2_select:0
[ERROR] KERNEL(1200,sklogd):2019-11-29-21:42:07.421.740 [8078.067672] [dvpp] [dvpp_print_vpc_job 184] OUT
[ERROR] KERNEL(1200,sklogd):2019-11-29-21:42:07.421.764 [8078.067673] [dvpp] [dvpp_print vpc_job 185] out use_flag:1
[ERROR] KERNEL(1200,sklogd):2019-11-29-21:42:07.421.789 [8078.067675] [dvpp] [dvpp_print_vpc_job 186] wr0 addr_frame_start:ffff35a00000
[ERROR] KERNEL(1200,sk1ogd):2019-11-29-21:42:07.421.823 [8078.067677] [dvpp] [dvpp_print_vpc_job 187] wr1 addr_frame_start:ffff35aca800
[ERROR] KERNEL(1200,sk1ogd):2019-11-29-21:42:07.421.853 [8078.067679] [dvpp] [dvpp_print_vpc_job 188] wr2 addr_frame_start:0
[ERROR] KERNEL(1200,sk1ogd):2019-11-29-21:42:07.421.880 [8078.067680] [dvpp] [dvpp_print_vpc_job 189] wr3 addr_frame_start:0
[ERROR] KERNEL(1200,sk1ogd):2019-11-29-21:42:07.421.905 [8078.067693] [dvpp] [dvpp_ioctl_vpc 845] call proc failed:-512, engine_id:1
```

## Possible Cause

According to the log, it is an error code returned by the VPC engine.  **-512**  indicates that it is caused by the abnormal interrupt when waiting for video decoding. It may occur when the user-mode process exits, resulting in abnormal interrupt when waiting for decoding.

## Solution

View the log file on the host to check the cause of the abnormal exit of the user-mode process.

## Other Error Codes

In addition to the  **-512**  error code returned by the VPC in the samples, other engines of the DVPP driver have their own return codes, as shown in Table 1.

Similarly, you can determine the engine that returns the error code based on the service type and the error code displayed in the device log file. Then, obtain the corresponding error code description based on the error code value to preliminarily determine the fault cause.

**Table  1**  DVPP Engine Error

| Engine Type | IOCTL Return Code | Description | Common Error Log |
| --- | --- | --- | --- |
| JPEGE | -22 | Argument invalid or not supported. | Common error log messages:<br><br>  - Return value: -35 with the message "JPEGE time wait, engine_id:xx." Encoding times out due to incorrect encoding parameters entered by the executor or other causes.<br>  - Return value: -512 with the message "Signal interrupted, engine_id:xx." Encoding is incorrect due to abnormal interrupt to the code. |
| -11 | Abnormal engine processing. Try again. |  |  |
| -14 | Abnormal address during user-mode data copy or engine destruction failure. |  |  |
| -16 | Engine application failed. |  |  |
| -35 | Encoding timed out. |  |  |
| -5 | Encoding failed and reset succeeded. |  |  |
| 5 | Encoding and reset failed. |  |  |
| -512 | Abnormal interrupt when waiting for encoding. |  |  |
| PNGD | -22 | Argument invalid or not supported. | Common error log messages:<br><br>  - Return value: 5/-5 with the message "Time out: wait failed xx." Decoding times out due to stream exceptions such as an incorrect image format.<br>  - Return value: 5/-5 with the message "Signal interrupted:xx, engine_id:xx." Decoding is interrupted abnormally. |
| -14 | Abnormal address during user-mode data copy or engine release failure. |  |  |
| -16 | Engine application failed. |  |  |
| -5 | Decoding failed and reset succeeded. |  |  |
| 5 | Decoding and reset failed. |  |  |
| JPEGD | -22 | Argument invalid or not supported; or decoding succeeded but register reset failed. | Common error log messages:<br><br>  - Return value: -1/-23 with the message "Decode abnormal, abnormal status:xx decode error! engine id: xx." The hardware reports an abnormal interrupt due to stream exceptions such as incorrect image format.<br>  - Return value: -2/-24 with the message "Decode abnormal, abnormal status:xx decode over time!, engine id:xx." Decoding times out due to busy bus or system page faults. |
| -14 | Abnormal address during user-mode data copy or engine destruction failure. |  |  |
| -16 | Engine application failed. |  |  |
| -1 | Decoding failed and reset succeeded. |  |  |
| -2/-3 | Decoding times out and reset succeeded. |  |  |
| -23 | Decoding and reset failed. |  |  |
| -24/-25 | Decoding timed out and reset failed. |  |  |
| VPC | -22 | Argument invalid or not supported. | Common error log messages:<br><br>  - Return value: -35 with the message "dvpp_vpc_engine_proc pipe wait time out: engine id:xx." Decoding times out due to busy bus or system page faults.<br>  - Return value: -32 with the message "Hardware process failed, engine id:xx." Incorrect decoding occurs due to stream exceptions. |
| -11 | Abnormal engine processing. Try again. |  |  |
| -14 | Abnormal address during user-mode data copy or engine destruction failure. |  |  |
| -16 | Engine application failed. |  |  |
| -35 | Decoding timed out. |  |  |
| -512 | Abnormal interrupt when waiting for decoding. |  |  |
| -32 | An exception detected by the driver when hardware decoding failed. |  |  |
| VPC_cmdlist | -22 | Argument invalid or not supported. | Common error log messages:<br><br>  - Return value: -35 with the message "dvpp_vpc_engine_proc pipe wait time out: engine id:xx." Decoding times out due to busy bus or system page faults.<br>  - Return value: -32 with the message "Hardware process failed, engine id:xx." Incorrect decoding occurs due to stream exceptions. |
| -11 | Abnormal engine processing. Try again. |  |  |
| -14 | Abnormal address during user-mode data copy or engine destruction failure. |  |  |
| -16 | Engine application failed. |  |  |
| -35 | Decoding timed out. |  |  |
| -512 | Abnormal interrupt when waiting for decoding. |  |  |
| -32 | Hardware decoding failed. |  |  |
| VENC | -22 | Argument invalid or not supported. | Common error log messages:<br><br>  - Return value: -35 with the message "wait timeout, Ret value is xx." Encoding fails before the completion interrupt is received due to incorrect executor configuration parameters or busy bus.<br>  - Return value: -61 with the message "venc err interrupt state = xx, wait_time_remain = xx." Encoding fails due to incorrect executor configuration parameters. |
| -11 | Abnormal engine processing. Try again. |  |  |
| -14 | Abnormal address during user-mode data copy or engine destruction failure. |  |  |
| -16 | Engine application failed. |  |  |
| -35 | Encoding failed before the completion interrupt received. |  |  |
| -61 | Encoding timeout interrupt. |  |  |
| VDEC | -22 | Argument invalid or not supported. | Common error log messages:<br><br>  - Return value: -35 with the message "VDM wait time out, wait_time_remain = xx, engine_id:xx." Decoding times out due to stream exceptions or busy bus.<br>  - Return value: -61 with the message "wait_time_remain = xx,have vdm_error,p_vdm_backup_state->VdmState=xx, engine_id:xx." Decoding error reporting is interrupted due to stream exceptions. |
| -11 | Abnormal engine processing. Try again. |  |  |
| -14 | Abnormal address during user-mode data copy or engine destruction failure. |  |  |
| -16 | Engine application failed. |  |  |
| -35 | Decoding timed out. |  |  |
| -61 | Decoding error reporting interrupted. |  |  |
| -4 | Abnormal interrupt when waiting for decoding. |  |  |
