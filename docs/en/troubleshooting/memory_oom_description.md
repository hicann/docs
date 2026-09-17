# Symptoms of Memory OOM Errors

Memory allocation fails because services use too much memory.

The following is an example of the error information in the plog. In this example,  **aclrtMallocPhysical**  is used to allocate physical memory on the device, but the memory allocation fails. YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

```text
[ERROR] DRV(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176881, 4176881][drv][devmm][share_log_read_in_single_module 634]Msg send failed. (ret=-12; devid=0; vfid=0; host_pid=4176881)
[ERROR] DRV(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176881, 4176881][drv][devmm][halMemCreate 3073]<errno:12, 6> Mem create failed. (ret=6; size=20971520; side=1; devid=0)
[ERROR] RUNTIME(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [npu_driver.cc:5757]4176881 MallocPhysical:[INIT][DEFAULT][drv api]halMemCreate failed. drvRetCode=6.
[ERROR] RUNTIME(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:4738]4176881 rtMallocPhysical:[INIT][DEFAULT]ErrCode=207001, desc=[driver error:out of memory], InnerCode=0x7020016
[ERROR] RUNTIME(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:53]4176881 FuncErrorReason:[INIT][DEFAULT]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:53]4176881 FuncErrorReason:[INIT][DEFAULT]rtMallocPhysical execute failed, reason=[driver error:out of memory]
[ERROR] ASCENDCL(4176881,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [memory.cpp:634]4176881 aclrtMallocPhysical: [INIT][DEFAULT]malloc physical memory failed, runtime result = 207001
```

If the system memory on the device is insufficient, the syslog \(**_\{Log export directory\}_/_\{Timestamp directory\}_/message/dev-os-_\{id\}_/messages.\***\) exported from the device contains the keyword  **oom**. The following is an example:

```text
(none) kern.info kernel: [144171.324674][T28699] [kbox] catch oom event on cpu 0.
(none) kern.info kernel: [144171.324682][T28699] [kbox] catch oom event, start logging, idx: 2120, time: YYYY‑MM‑DD HH:MM:SS.ffffff
```
