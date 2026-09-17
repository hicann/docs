# HBM Bit ECC Fault

## Symptom

The event logs on the device \(**slog/dev-os-_id_/run/event/event\__\*_.log**\) contain the keyword  **event\_id=0x80E01809**  or  **event\_id=0x80E01801**.

The black box logs on the device \(in the  **hisi\_logs/device-_id_/_\*_/bbox**  directory\) contain the keyword  **Hardware Error**.

```text
/hisi_logs/device-2/******/bbox/kbox.txt:2014[2454.830692] {6}[Hardware Error] Hardware error from APEI Generic Hardware Error Source: 0
/hisi_logs/device-2/******/bbox/kbox.txt:2015[2454.830693] {6}[Hardware Error]event severity: recoverable
/hisi_logs/device-2/******/bbox/kbox.txt:2016[2454.830694] {6}[Hardware Error] Error 0, type: recoverable
/hisi_logs/device-2/******/bbox/kbox.txt:2017[2454.830696] {6}[Hardware Error]  section_type: memory error
/hisi_logs/device-2/******/bbox/kbox.txt:2018[2454.830697] {6}[Hardware Error]  physical_address: 0x0000101efe36d3c0
/hisi_logs/device-2/******/bbox/kbox.txt:2019[2454.830699] {6}[Hardware Error]  node: 2 card: 259 module: 51 rank: 1 bank: 10 row: 30691  column: 56
/hisi_logs/device-2/******/bbox/kbox.txt:2020[2454.830701] {6}[Hardware Error]  error_type: 3, multi-bit ECC
/hisi_logs/device-2/******/bbox/kbox.txt:2024[2454.830702] {6}[Hardware Error]  DIMM location: not present. DMI handle: 0x0000
```

## Fault Root Causes

Based on the error information in the preceding logs, it can be determined that the AI Core error is caused by the HBM bit ECC fault.

## Solution

Click  _[Health Management Fault Definition](https://support.huawei.com/enterprise/en/ascend-computing/ascend-hdk-pid-252764743)_  to obtain the manual of the corresponding version. The HBM bit ECC fault is described as follows \(some key fields are listed\):

|  |  |
| --- | --- |
| Event ID | 0x80E01809 |
| Event Name | Multi-bit ECC errors during the HBM patrol |
| Fault Description/Possible Cause | A multi-bit ECC error is triggered during HBMC patrol scrubbing and demand scrubbing. The possible cause is that some HBM chips fail or the HBM cannot store data properly. This is usually caused by hardware faults. |
| Impact | 1. If an incorrect address is accessed during the startup, the startup may fail.<br>2. If a service accesses an incorrect address, error data is returned, which may cause service failures.<br>3. The service does not access an incorrect address, and the current service is not affected. |
| System Action | 1. Reports a notification event to the device management module, records the error address, attempts to isolate the device online, and performs offline isolation after the device is restarted.<br>2. Records error logs. |
| System Handling Suggestion | No operation is required. |

|  |  |
| --- | --- |
| Event ID | 0x80E01801 |
| Event Name | Multi-bit ECC errors when accessing the HBM space |
| Fault Description/Possible Cause | A multi-bit ECC error is triggered and address hot isolation fails when the HBM space is accessed. The possible cause is that some HBM chips fail and the failed addresses are still occupied. This is usually caused by hardware faults. |
| Impact | Incorrect data is returned when the HBM is accessed, which may cause NPU startup failures or service failures. |
| System Action | 1. Reports fault events to the device management module.<br>2. Records error logs. |
| System Handling Suggestion | If the reported host PID is 0, you are advised to reset the SoC. If the reported host PID is not 0, kill the process and wait for a restoration period. If the fault persists, you are advised to reset the SoC. |
