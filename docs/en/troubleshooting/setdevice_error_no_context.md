# No Context Is Available Due to an Error in Invoking the SetDevice Interface

## Symptom

Collect the log file by referring to  [Collect Information About Process Interruption](collect_process_interrupt_info.md). The following uses  **$\{HOME\}/err\_log\_info/**  as an example of directory for storing collected logs.

The host application log file \(**$\{HOME\}/err\_log\_info/log/\[run|debug\]/plog/plog-_pid_\_\*.log**\) contains the keywords  **ctx is NULL**  and  **context pointer null**. A log example is as follows:

```text
[ERROR]RUNTIME(2977549,test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu[api_impl.cc:5544]2978321 CtxGetSysParamOpt:report error module_type=3,module_name=EE8888
[ERROR]RUNTIME(2977549,test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu[api_impl.cc:5544]2978321 CtxGetSysParamOpt:ctx is null!
[ERROR]RUNTIME(2977549,test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu[api_c.cc:5200]2978321 rtCtxGetSysParamOpt:ErrCode=107002, desc=[context pointer null],InnerCode=0x7070001
[ERROR]RUNTIME(2977549,test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu[error_message_manage.cc:48]2978321 FuncErrorReason:rtCtxGetSysParamOpt execute
failed, reason=[context pointer null]
[ERROR]RUNTIME(2977549,test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu[api_impl.cc:5553]2978321 CtxGetOverflowAddr:report error module_type=3,
module_name=EE8888
```

## Fault Root Causes

An exception occurs when the API related to the SetDevice operation is called. As a result, no context is available.

Corresponding acl API:  **aclrtSetDevice**

Corresponding runtime API:  **rtSetDevice**/**rtSetDeviceEx**

## Solution

Run the  **export ASCEND\_GLOBAL\_LOG\_LEVEL=1**  command to set the log level to  **info**, execute the service again, collect logs, search for the keyword  **SetDevice**  in the plog file, check whether the following incorrect SetDevice invoking mode exists, and optimize the code logic based on the check scenario.

- If  **SetDevice**  is found, check the following code logic:
    - Check whether the device in the operating environment is abnormal. If yes, the context cannot be created.

        **Error Scenario Example**: The SetDevice operation is performed, but no device exists in the operating environment.

        ```text
        [root@localhost plog]# grep -rn "SetDevice"
        plog-27441_******.log:2210:[INFO] ASCENDCL(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device.cpp:148]28980 aclrtSetDevice: start to execute aclrtSetDevice, deviceId = 0
        plog-27441_******.log:2231:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 28980 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:2235:[WARNING] ASCENDCL(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device.cpp:157]28980 aclrtSetDevice: update platform info with device failed, deviceId = 0
        plog-27441_******.log:2236:[INFO] ASCENDCL(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device.cpp:160]28980 aclrtSetDevice: successfully execute aclrtSetDevice, deviceId = 0
        plog-27441_******.log:6861:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 29157 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:11191:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 29157 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:36695:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 28980 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:36738:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 28980 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:36781:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 28980 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:36796:[INFO] RUNTIME(28980,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 28980 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:561:[INFO] RUNTIME(30104,host_cpu_executor):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1798] 30104 rtSetDevice: There is no devId, do nothing.
        plog-27441_******.log:9522:[INFO] HCCL(30104,host_cpu_executor):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [hccl_impl_base.cc:2644] [30104][SetDevice] entry
        plog-27441_******.log:9526:[INFO] HCCL(30104,host_cpu_executor):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [hccl_impl_base.cc:2622] [31143][SetDeviceThread]ctx[(nil)]
        plog-27441_******.log:9527:[INFO] HCCL(30104,host_cpu_executor):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [hccl_impl_base.cc:2637] [31143][SetDeviceThread]exit
        plog-27441_******.log:9528:[INFO] HCCL(30104,host_cpu_executor):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [hccl_impl_base.cc:2657] [30104][SetDevice]exit
        ```

        ```text
        [root@localhost plog]# grep -rn "ERROR"
        plog-27441_******.log:36899:[ERROR] RUNTIME(28980,python3:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu) [api_impl.cc:1038]28980 GetMaxStreamAndTask:[FINAL][FINAL]report error module_type=3, module_name=EE8888
        plog-27441_******.log:36900:[ERROR] RUNTIME(28980,python3:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu) [api_impl.cc:1038]28980 GetMaxStreamAndTask:[FINAL][FINAL]ctx is NULL!
        plog-27441_******.log:36902:[ERROR] RUNTIME(28980,python3:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu) [logger.cc:417]28980 GetMaxStreamAndTask:[FINAL][FINAL]GetMax stream and task failed, streamType=0.
        plog-27441_******.log:36903:[ERROR] RUNTIME(28980,python3:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu) [api_c.cc:850]28980 rtGetMaxStreamAndTask:[FINAL][FINAL]ErrCode=107002, desc[contextpointer null], InnerCode=0x7070001
        plog-27441_******.log:36904:[ERROR] RUNTIME(28980,python3:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu) [error_message_manage.cc:48]28980 FuncErrorReason:[FINAL][FINAL]report error module_name=EE1001
        plog-27441_******.log:36905:[ERROR] RUNTIME(28980,python3:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu) [error_message_manage.cc:48]28980 FuncErrorReason:[FINAL][FINAL]rtGetMaxStreamAndTask execute failed, reason=[context pointer null]
        ```

    - In the multi-thread scenario, check whether the SetDevice operation thread is the same as the thread that reports the error. Check whether the SetDevice operation is performed only for the main thread \(thread ID: 2977549\) and not for the sub-thread \(thread ID: 2978321\). If yes, no context is available in the subthread.

        **Error Scenario Example**: SetDevice is performed only for the main thread and not for other thread. As a result, an error is reported.

        ```text
        [root@localhost plog]# grep -rn "ERROR"
        104069:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu  [api_impl.cc:5544]2978321
        CtxGetSysParamOpt:report error module_type=3, module_name=EE8888
        104070:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_impl.cc:5544]2978321 CtxGetSysParamOpt:ctx is NULL!
        104072:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:5200]2978321 rtCtxGetSysParamOpt:ErrCode=107002, desc[context pointer null], InnerCode=0x7070001
        104073:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]2978321 FuncErrorReason:report error module_name=EE1001
        104074:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]2978321 FuncErrorReason:rtCtxGetSysParamOpt execute failed, reason=[context pointer null]
        104080:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu  [api_impl.cc:5553]2978321
        CtxGetOverflowAddr:report error module_type=3, module_name=EE8888
        104081:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu  [api_impl.cc:5553]2978321 CtxGetOverflowAddr:ctx is NULL!
        104083:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:5210]2978321 rtCtxGetOverflowAddr:ErrCode=107002, desc[context pointer null], InnerCode=0x7070001
        104084:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]2978321 FuncErrorReason:report error module_name=EE1001
        104085:[ERROR] RUNTIME(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]2978321 FuncErrorReason:rtCtxGetOverflowAddr execute failed, reason=[context pointer null]
        104087:[ERROR] OP(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [nnopbase_executor.cpp:73][NNOP][NnopbaseSetOverFlowAddr][2978321] errno[361001] Assert ((rtCtxGetOverflowAddr(&addr)) == 0) failed
        104089:[ERROR] OP(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [nnopbase_executor.cpp:216][NNOP][NnopbaseSetExecutorSetGlobalConfig][2978321]
        errno[361001] Check NnopbaseSetOverFlowAddr(g_nnopbaseSysCfgParams.overflowAddr) failed
        104091:[ERROR] OP(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [nnopbase_api.cpp:44][NNOP][NnopbaseInit][2978321] errno[361001] Check
        NnopbaseExecutorSetGlobalConfig() failed
        104093:[ERROR] OP(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [nnopbase_api.cpp:53][NNOP][NnopbaseCreateExecutorSpace][2978321]  errno[361001] Assert ((NnopbaseInit()) == 0) failed
        104095:[ERROR] OP(2977549, test_incre):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [nnopbase_api.cpp:19][NNOP][NnopbaseOpLogE][2978321] errno[361001] Check
        NnopbaseCreateExecutorSpace(&executorSpace) failed
        ```

    - Check whether SetDevice is invoked after an error is reported. If yes, no context is available.

        **Error Scenario Example**: An error is reported because the SetDevice interface is not invoked before memory allocation.

        ```text
        [ERROR] RUNTIME(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_impl.cc:1401]45179 DevMalloc: [DUMP] [DEFAULT] report error module_type=3, module_name=EE8888
        [ERROR] RUNTIME(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_impl.cc:1401]45179 DevMalloc: [DUMP] [DEFAULT] ctx is NULL!
        [INFO] GE(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:296]45179 ReportInterErrMessage:report error message, error_code:EE8888, work_stream_id:4452545179
        [ERROR] RUNTIME(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [logger.cc:581]45179 DevMalloc:[DUMP][DEFAULT]Device malloc failed, size=9(Byte), type=2.
        [ERROR] RUNTIME(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1173]45179 rtMalloc:[DUMP][DEFAULT]ErrCode=107002, desc=[context pointer null], InnerCode=0x7070001
        [ERROR] RUNTIME(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]45179 FuncErrorReason:[DUMP][DEFAULT] report error module_name=EE1001
        [ERROR]RUNTIME(44525,python) :YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]45179 FuncErrorReason:[DUMP][DEFAULT] rtMallocexecute failed, reason=[context pointer null]
        ```

- If  **SetDevice**  is not found, the SetDevice operation is not performed. As a result, no context is available.
