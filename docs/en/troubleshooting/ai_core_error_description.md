# Symptoms of AI Core Errors

The user application reports an error and exits. The error code in the terminal screen log is EZ9999 or EZ2001, and the log contains the following message:  **the error is aivec error**  or  **the error is aicore error**. Alternatively, the error log  **AI Core kernel execution failed**  exists in the plog.

**The following is an example of the EZ9999 terminal screen log.** YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

```text
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

**The following is an example of the EZ2001 terminal screen log.** YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

```text
[PID: 235403] YYYY‑MM‑DD‑HH:MM:SS.fff.uuu Execution_Error(EZ2001): An error occurs on the device(chipId:0, dieId:0), the serial number is 4, the error is aicore error, core id is 14, error code = 0x800000, dump info: pc start: 0x124000000ce0, current: 0x124000000d88, vec error info: 0, mte error info: 0x30300005d, ifu error info: 0x6e17f6e304080, ccu error info: 0xe3c78a280004021e, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c100000000, aic cond: 0.
The extend info: errcode:(0x800000, 0, 0) errorStr: MTE accesses an invalid GM address or the cross-device memory access times out. fixp_error0 info: 0x300005d, fixp_error1 info: 0x3, fsmId:1, tslot:0, thread:0, ctxid:0, blk:9, sublk:0, subErrType:4.
Fault RAS occurs in the system: [event_id:0x80e01801] Uncorrectable ECC / other uncorrectable memory error. For details about troubleshooting, see Health Management Error Definition.
TraceBack (most recent call last):
        An error occurred in the kernel task, retCode=0x26, [aicore exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1006]
        rtStreamSynchronize execution failed, reason=device mem error[FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:69]
```

**Description:**

- **chipId**  and  **dieId**: respectively represent the reported chipId and dieId, which can be used to determine whether it is a fixed chipId error;
- **core id:**  indicates the core ID of the error-reporting chip, which can be used to determine whether the error occurred on the same core;
- **errcode**  and  **errorStr**: respectively represent the error code and error description of the AI Core error;
- **fault kernel\_name/fault kernel info ext:**  means the name of the kernel that caused the error. The name can be used to view the error-causing operator.

    In the scenario of executing asynchronous tasks, such as issuing multiple operator execution tasks continuously, multiple operators may report errors, so the error message may contain errors of multiple operators. You need to troubleshoot the problems starting from the first error-reporting operator.
