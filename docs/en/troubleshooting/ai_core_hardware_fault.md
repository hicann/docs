# AI Core Hardware Fault

## Symptom

The host application logs \(**log/\[run|debug\]/plog/plog-_pid_\__\*_.log**\) contain the following error information:

```text
[ERROR] RUNTIME(377228,ascend-dmi):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_proc.cc:1164] 377265 ProcessStarsCoreErrorInfo:An error occurs on the device(chipId:2, dield:0), the serial number is 4, the error is fftsplus aivector error, core id is 34, error code = 0, dump info: pc start: 0x12406ce78f54, current: 0x12406ce7C430, vec error info: 0xef1d17c368, mte error info: 0xf3dff1cf9b, ifu error info: 0x63f70dc00e200, ccu error info : 0x6f6d518f0004d700, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x1240403e5000． The extend info: errcode:(0, 0x80000000, 0) errorStr: A 2-bit ECC error occurs in the data-cache data-ram. fixp_error0 info: 0xff1cf9b, fixp_error1 info: 0xf3 fsmId:0, tslot:0, ctxid:0, blk:16, subblk:0, subErrType:4.
```

## Fault Root Causes

Use the ascend-dmi tool to perform a stress test on the AI Core. If the stress test is abnormal and  **EMERGENCY\_WARN**  is displayed, the AI Core is faulty.

The ascend-dmi tool needs to be installed separately. The following is an example of the command for performing a pressure test on the AI Core:

```bash
ascend-dmi --dg -i aicore
```

The ascend-dmi tool is contained in the MindCluster ToolBox software package. For details about the mapping between the software and CANN, click  [here](https://www.hiascend.com/developer/download/community/result?module=dl+cann). For details about how to install and use the ascend-dmi tool, click  [here](https://www.hiascend.com/document/detail/en/mindcluster/latest/toolbox/toolboxug/toolboxug_0002.html).

## Solution

Contact technical support to replace the hardware.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
