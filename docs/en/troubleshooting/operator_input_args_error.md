# Operator Input Argument Errors

## Symptom

The host application logs \(**log/\[run|debug\]/plog/plog-_pid_\__\*_.log**\) contain the following error information. YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

```text
[ERROR] RUNTIME(85483,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task_info.cc:1678]85658 PrintErrorInfoForDavinciTask:Aicore kernel execute failed, device_id=0, stream_id=2, report_stream_id=2, task_id=57783, flip_num=3, fault kernel_name=RealDiv_ee98c6628030785f610b924ab1557b31_high_precision_210000000, fault kernel info ext=none, program id=9, hash=10612039229658031084.
[ERROR] RUNTIME(85483,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task_info.cc:1617]85658 GetArgsInfo:[AIC_INFO] args(0 to 9) after execute:0x4f453840, 0x124201ea7400, 0x12420240cc00, 0x1241c006dc28, 0x124100011000, 0x1, 0x1, 0x1, 0,
```

## Fault Root Causes

In the error information of the plogs, the  **args\(_xxxx_\) after execute**  part is critical. Check whether the parameter address in the  **args after execute**  part is proper. If  **0**  is displayed, the address allocation is incorrect.

On the  Atlas training products, the address starts with  **0x1240**. If the address does not start with  **0x1240**, an exception may occur. In the preceding error logs,  **0x4f453840**,  **0x124201ea7400**,  **0x12420240cc00**, and  **0x1241c006dc28**  are displayed in  **args after execute**  on the  Atlas training products. The first parameter  **0x4f453840**  does not start with  **0x1240**. It is suspected that the parameter address is the host memory address instead of the device memory address. As a result, the AI Core fails to read data.

On the  Atlas A2 training products/Atlas A2 inference products, the address does not start with  **0x1240**. If the address starts with  **0x1240**, an exception may occur.

## Solution

Check the training script. If division is used, for example,  **cpu\_tensor/npu\_tensor**  is used, the AI Core will fail to read data. The reason is that  **cpu\_tensor**  is the host memory address and  **npu\_tensor**  is the device memory address. In this case, you need to change these two addresses to the device memory addresses.
