# AI Core Error问题现象描述

用户应用程序报错退出，终端屏幕日志错误码为EZ9999或EZ2001，且日志中包含“**the error is aivec error**”或“**the error is aicore error**”；或者plog日志中存在报错日志“**AI Core kernel execution failed**”。

**EZ9999终端屏幕报错示例如下所示**，YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。

```bash
EZ9999: Internal error!
EZ9999[PID: 2574461] YYYY‑MM‑DD‑HH:MM:SS.fff.uuu (EZ9999):  An error occurs on the device(chipId:0, dieId:0), the serial number is 329, the error is aivec error, core id is 0, error code = 286, dump info: pc start: 0x120041000100, current: 0x12004100016c, sc error info: 0xffffffffffff, su error info: 0xeadbe7fe29c20051,0x80400000f800f7da, mte error info: 0x2f40000025969, vec error info: 0xbf7f93fe007efefa, cube error info: 0, l1 error info: 0, aic error mask: 0x395856, para base: 0x120000200400, mte error: 0, aic cond: 0.
The extend info: errcode:(286) errorStr: The trap instruction reports an error. subErrType: 0x4.
For details, see the troubleshooting document on the Ascend official website. Search for the keyword "AI Core Error".[FUNC:PrintDavidCoreInfo][FILE:device_error_proc_c.cc][LINE:711]
TraceBack (most recent call last):
       An error occurred in the kernel task, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1006]
       Vector Core kernel execution failed, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1875]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1875]
       [DFX_INFO]AI Core kernel execution failed, device_id=0, stream_id=60, report_stream_id=60, task_id=1, flip_num=0, fault kernel_name=ErrorOPf_1, fault kernel info ext=none, program id=0, hash=3348555330679819737.[FUNC:GetError][FILE:stream.cc][LINE:1875]
       rtStreamSynchronize execution failed, reason=vector core exception[FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:69]
```

**EZ2001终端屏幕报错示例如下所示**，YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。

```bash
[PID: 235403] YYYY‑MM‑DD‑HH:MM:SS.fff.uuu Execution_Error(EZ2001): An error occurs on the device(chipId:0, dieId:0), the serial number is 4, the error is aicore error, core id is 14, error code = 0x800000, dump info: pc start: 0x124000000ce0, current: 0x124000000d88, vec error info: 0, mte error info: 0x30300005d, ifu error info: 0x6e17f6e304080, ccu error info: 0xe3c78a280004021e, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c100000000, aic cond: 0.
The extend info: errcode:(0x800000, 0, 0) errorStr: MTE accesses an invalid GM address or the cross-device memory access times out. fixp_error0 info: 0x300005d, fixp_error1 info: 0x3, fsmId:1, tslot:0, thread:0, ctxid:0, blk:9, sublk:0, subErrType:4.
Fault RAS occurs in the system: [event_id:0x80e01801] Uncorrectable ECC / other uncorrectable memory error. For details about troubleshooting, see Health Management Error Definition.
TraceBack (most recent call last):
        An error occurred in the kernel task, retCode=0x26, [aicore exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1006]
        rtStreamSynchronize execution failed, reason=device mem error[FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:69]
```

**报错日志解读：**

- **chipId、dieId**：分别表示报错芯片chipId及dieId，可用于判定是否固定chipId报错；
- **core id：**表示报错芯片核id，可用于判定是否在同一个core上执行报错；
- **errcode**、**errorStr**：分别表示AI Core Error的报错错误码、错误描述；
- **fault kernel\_name/fault kernel info ext：**表示报错kernel名字，可用于查看报错算子。

    异步任务执行场景下，例如连续下发多个算子执行任务，可能会有多个算子报错，错误信息中可能包含多个算子错误，用户需从首报错算子开始排查问题。
