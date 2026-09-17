# AI Core Timeout Fault

## Symptom

The host application logs \(**log/\[run|debug\]/plog/plog-_pid_\__\*_.log**\) contain the following error information. YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

```text
[ERROR] RUNTIME(2897353,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:1227]2897467 PrintCoreInfo:An error occurs on the device(chipId:0, dieId:0), the serial number is 7, the error is aivec error, core id is 9, error code = 0, dump info: pc start: 0x1240000000e4, current: 0x12400000013c, vec error info: 0x6211f34358, mte error info: 0x7e33ba0d8b, ifu error info: 0x2075ca373f800, ccu error info: 0x2447806309616cb7, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c100001000, aic cond: 0. The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0x3ba0d8b, fixp_error1 info: 0x7e, fsmId:1, tslot:0, thread:0, ctxid:0, blk:0, sublk:0, subErrType:2. For details, see the troubleshooting document on the Ascend official website. Search for the keyword "AI Core Error".
```

The event logs on the device \(**slog/dev-os-_id_/run/event/event\__\*_.log**\) contain the keyword  **event\_id=0x80C98001**  or  **event\_id=0x80CB8001**.

## Fault Root Causes

Use the ascend-dmi tool to perform a stress test on the AI Core. If the stress test is abnormal and the message "a timeout error occurred" is displayed, the AI Core times out. The following is an example of the error message:

```text
Hardware:
    aicore:
        FAIL
        *** Some processes are seizing the NPU. Test results may be affected.
        *** Device 4: a timeout error occurred.
```

The ascend-dmi tool needs to be installed separately. The following is an example of the command for performing a pressure test on the AI Core:

```bash
ascend-dmi --dg -i aicore -s -q
```

The ascend-dmi tool is contained in the MindCluster ToolBox software package. For details about the mapping between the software and CANN, click  [here](https://www.hiascend.com/developer/download/community/result?module=dl+cann). For details about how to install and use the ascend-dmi tool, click  [here](https://www.hiascend.com/document/detail/en/mindcluster/latest/toolbox/toolboxug/toolboxug_0002.html).

## Handling Method

Power off and restart the device and then use the ascend-dmi tool to perform a stress test again. If the timeout error persists, the hardware is faulty. Contact technical support to replace the hardware.

After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
