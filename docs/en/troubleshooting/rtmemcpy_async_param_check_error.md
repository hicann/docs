# Reported error in rtMemcpyAsync asynchronous parameter verification

## Symptom

Collect the log file by referring to  [Collect Information About Process Interruption](collect_process_interrupt_info.md). The following uses  **$\{HOME\}/err\_log\_info/**  as an example of directory for storing collected logs.

The host application log file \(**$\{HOME\}/err\_log\_info/log/\[run|debug\]/plog/plog-_pid_\_\*.log**\) contains the keywords  **Memory async failed**  and  **kind=x is invalid**. A log example is as follows:

```text
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_error.cc:963]291577 MemcpyAsyncCheckKindAndLocation:[EXEC][EXEC]report error module_name=EE1001
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_error.cc:963]291577 MemcpyAsyncCheckKindAndLocation:[EXEC][EXEC]Memory async failed, src loc type=2, dst loc type=2, kind=1 is invalid!
[INFO] GE(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:301]291577 ReportErrMessage:report error_message, error_code:EE1001, work_stream_id:11.
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_error.cc:881]291577 MemcpyAsync:[EXEC][EXEC]report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_error.cc:881]291577 MemcpyAsync:[EXEC][EXEC]Memory async failed, check kind and loc,retCode=0x7110001
[INFO] GE(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:2551]291577 ReportInterErrMessage:report error_message, error_code:EE8888, work_stream_id:11
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:1428]291577 rtMemcpyAsync:[EXEC][EXEC]ErrCode=107000, desc=[invalid value], InnertCode=0x7110001
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]291577 FuncErrorReason:[EXEC][EXEC]report error module_name=EE1001
[ERROR] RUNTIME(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:48]291577 FuncErrorReason:[EXEC][EXEC]rtMemcpyAsync execute failed, reason=[invalid value]
[INFO] GE(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_manager.cc:301]291577 ReportErrMessage:report error_message, error_code:EE1001, work_stream_id:11
[ERROR] ASCENDCL(291088,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [memory.cc:336]291577 aclrtMemcpyAsync:[EXEC][EXEC]asynchronized memcpy failed, kind = 1, runtime result = 107000
```

The key fields in the log are described as follows:

- The values of loc type are described as follows:
    - 1: host memory address
    - 2: device memory address
    - 3: SVM memory address
    - 4: DVPP memory address

- The values of kind \(copy type\) are described as follows:
    - 0: data copy on the host
    - 1: data copy from host to device
    - 2: data copy from device to host
    - 3: data copy within a device or between two devices
    - 4: management memory, used by internal components
    - 5: data copy within a device or between two devices, level-2 pointer copy, used by internal components

## Fault Root Causes

During asynchronous copy, you need to specify the src and dst addresses and the copy type kind \(such as H2D and D2H\). Then the runtime verifies the validity of the src and dst addresses based on the kind, such as H2D, in this case, the src address should be the host memory address, and the dst address should be the device memory address. If the address types of src and dst do not match kind, an error is reported.

## Solution

Check the code logic of asynchronous copy and specify the correct src and dst addresses and copy type kind.
