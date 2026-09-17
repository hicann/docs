# iCache Data Verification Fault

## Symptom

The event logs on the device \(**slog/dev-os-_id_/run/event/event\__\*_.log**\) contain the keyword  **event\_id=0x80C98000**.

On the  Atlas A2 training products/Atlas A2 inference products, the trace logs \(in the  **$HOME/ascend/atrace/**  directory by default\) contain the keyword  **stars\_print\_error\_pc\_icache\_and\_hbm\_info**.

```text
hisi_logs/device-2/******/log/ts.log:5177:[ERROR] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 35906 (dieid:0,cpuid:0) aicore.c:767 stars_print_error_pc_icache_and_hbm_info: stat for dump pc start, aiv_id=47, icache_miss_num=8161, hbm_miss_num=0, compare_num=32, compare_fail_num=0
```

On the  Atlas inference products, the trace logs \(in the  **$HOME/ascend/atrace/**  directory by default\) contain the keyword  **check\_error\_pc\_icache\_and\_hbm\_info**.

```text
[ERROR] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 438 (dieid:0,cpuid:0) aicore_icache_plat.c:848 check_error_pc_icache_and_hbm_info: stat for dump pc start, aic_id=1, icache_miss_num=8176, hbm_miss_num=0, compare_num=17, compare_fail_num=0
```

## Fault Root Causes

Locate the error keyword and check the value of  **compare\_fail\_num**. If the value is not  **0**, the iCache memory bit error occurs.

## Solution

Click  _[Health Management Fault Definition](https://support.huawei.com/enterprise/en/ascend-computing/ascend-hdk-pid-252764743)_  to obtain the manual of the corresponding version. The iCache memory bit error is described as follows \(some key fields are listed\):

|  |  |
| --- | --- |
| Event ID | 0x80C98000 |
| Event Name | The AI Core instruction data fails to be verified. |
| Fault Description/Possible Cause | The iCache data is inconsistent with the GM data. The possible causes are as follows:<br><br>  1. ICache data changes.<br>  2. The GM data is modified. |
| Impact | The current AI task fails. If the AI Core is not restored, subsequent AI tasks also fail. |
| System Action | 1. TSFW reports faults to the fault management module through TSDrv.<br>  2. TSFW records error logs.<br>  3. TSFW returns a task failure message through the service plane.<br>  4. TSFW resets the AIC. If the AIC is successfully reset, TSFW reports through TSDrv to clear the fault events. If the AIC fails to be reset, the core is removed (after the core is isolated, it will no longer be used for service scheduling) and an error log is recorded. |
| System Handling Suggestion | 1. Exit the AI training job and execute it again or initiate an inference request again.<br>  2. If the AI task fails to be executed again, you are advised to reset the SoC. If the fault persists, you are advised to return the device to the factory for repair. |
