# Execution Error of the Moe Dispatch/Combine Operator Due to Network Issues

## Symptom

In the  Atlas A3 training products/Atlas A3 inference products  scenario, an error is reported during Runtime execution on the host. Key information about  **fault kernel\_name**  and  **func\_name**  is printed in the application run logs.  **fault kernel\_name**  is the MoeDistributeDispatchV2 operator or MoeDistributeCombineV2 operator, and the error message is "errcode:\(0x800000, 0, 0\) errorStr: The DDR address of the MTE instruction is out of range".

In  Ascend EP  form, the application run logs,  **plog-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/plog**  by default.

```text
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stars_engine.cc:1502]1254 ProcLogicCqReport:Task run failed, device_id=9, stream_id=3, task_id=5981, sqe_type=7(notify wait), errType=0x20(sq sw status error), sqSwStatus=0x16620324
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:333]1254 ProcessStarsCoreErrorInfo:report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:333]1254 ProcessStarsCoreErrorInfo:The error from device(chipId:4, dieId:1), serial number is 1, there is an exception of fftsplus aivector error, core id is 18, error code = 0x800000, dump info: pc start: 0x12c0c6ce5000, current: 0x12c0c6ce5a6c, vec error info: 0xc3117b71b5, mte error info: 0x960700006b, ifu error info: 0x77688bb0aec0, ccu error info: 0x7ccdbee64ba3149b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c0c86c2a98.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:353]1254 ProcessStarsCoreErrorInfo:report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:353]1254 ProcessStarsCoreErrorInfo:The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x700006b, fixp_error1 info: 0x96, fsmId:1, tslot:7, thread:0, ctxid:0, blk:1, sublk:0, subErrType:4.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:246]1254 HasMemUceErr:Get isSmmuFault is 0.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:369]1254 ProcessStarsCoreErrorInfo:mte error, devId=9, streamId=1634, taskId=804, errorCode=546.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stream.cc:3285]1254 EnterFailureAbort:stream_id=3 enter failure abort.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [stream.cc:1188]1254 GetError:Stream Synchronize failed, stream_id=3, retCode=0x222, [suspect remote error].
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model_execute_task_info.cc:593]1254 ReportErrorInfoForModelExecuteTask:model execute error, retCode=0x91, [the model stream execute failed].
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model_execute_task_info.cc:551]1254 PrintErrorInfoForModelExecuteTask:stream_id=3, task_id=5980, sqVirtualAddr=0, head equal tail flag=0.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model_execute_task_info.cc:507]1254 PrintErrorModelExecuteTaskFuncCall:funcCallSvmMem=0x1252011a9000, funCallMemSize=816.
[ERROR] RUNTIME(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [davinci_kernel_task.cc:1471]1254 PrintErrorInfoForDavinciTask:Aicore kernel execute failed, device_id=9, stream_id=1634, report_stream_id=3, task_id=804, flip_num=0, fault kernel_name=te_moedistributecombinev2_2dec9514b32cf64e557fcc584b62d9e99571340395f19b500a6362eb101348634ff5f1847bfbf56fb634f3ea4a8c75f0fc95d46f8ac4af1a2420c2bb85b154c9_static_bin, fault kernel info ext=te_moedistributecombinev2_2dec9514b32cf64e557fcc584b62d9e99571340395f19b500a6362eb10134863, program id=213, hash=12167788236099877968.
[ERROR] GE(1254,ker_DP25_EP25):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_tracking.cc:113]1254 ErrorTrackingCallback: ErrorNo: 4294967295(failed) Error happened, origin_op_name [MoeDistributeCombineV2_48], op_name [MoeDistributeCombineV2_48], task_id 804, stream_id 1634.
```

## Possible Fault

The stream synchronization may fail, with acl API error message "Execute model failed" reported and recorded in the plog. As a result, the inference service may be interrupted.

```text
[ERROR] ASCENDCL(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cpp:699]4150867 ModelExecute: [EXEC][DEFAULT][Exec][Model]Execute model failed, ge result[507011], modelId[1]
[ERROR] ASCENDCL(4150867,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [model.cpp:1547]4150867 aclmdlExecute: [EXEC][DEFAULT][Exec][Model]modelId[1] execute failed, result[507011]
```

## Possible Cause

- Cause 1: If the problem occurs after the service is started, check whether the ranks in the EP domain cross supernodes. The MTE solution depends on the HCCS link. The communication domain of the rank executed by the operator must be in the same supernode.
- Cause 2: \(The problem of high-priority for check arises during long-term stable operation.\) Check whether the network switch is faulty at the time when the error is reported, for example, intermittent network disconnection, switch fault, or timeout due to optical link problems. The timeout mechanism of the LingQu network causes the cross-device communication operator to report the error "MTE out of range" with the error code 0x800000.
- Cause 3: \(The problem of high-priority for check arises during long-term stable operation.\) Check whether the service processes on other devices in the EP domain exit abnormally. If a remote process exits, the address resources of the remote process mapped to the local end are released. When the local end accesses the remote end, the error code 0x800000 "MTE out of range" of the operator is reported. You need to find the cause of the remote process exit. You can check whether a core file is generated first.
- Cause 4: If an error is reported on all devices, check the time when the error is reported and preferentially check the devices that report the error first. \(When an instance is released by the inference service and exits, other devices may not have time to report errors, and no error information is recorded in the plog.\)
- Cause 5: If the preceding symptoms are normal, sort out the sequence in which processes exit, find the process that exits first, and analyze the cause of the process exit.

## Solution

1. Collect the plogs of all ranks and check the environment and logs by referring to Possible Cause.
2. Search for the keyword  **fault\_kernel\_name**  in the plogs to check whether operator errors are reported on all NPUs.
    - Scenario 1: If the plog contains error information, analyze the error information by error occurrence time by referring to  step 4 and view the first error log.
    - Scenario 2: If the plog of the rank in the EP domain does not contain error information, check whether the host core dump occurs on the rank and preferentially confirm the core dump problem. If no host exception occurs, check the service exit time point based on the device system log by referring to step 3.

3. Use the msnpureport tool to collect device system logs on the server \(if the instance crosses multiple servers, collect the logs on all servers\). Go to the  **slog**  directory, search for the keyword  **app exit begin**  globally, sort the logs by time, and confirm the rank where the first error occurs. Then go to next step. For details, see Fault Example.
4. Sort the first error information.

    If  **op\_type**  in the plog of the first error reported on the device is  **MoedistributeDispatch**  or  **MoeDistributeCombine**  and the error message is "The DDR address of the MTE instruction is out of range", check whether the network switch is faulty at the time when the error is reported. Otherwise, the error "The DDR address of the MTE instruction is out of range" in the EP domain is caused by the abnormal process of the first error. In this case, check the host and plogs of the rank at the exit time to check whether other abnormal behaviors exist.

5. After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the fault persists.

## Fault Example

This example describes how to find the earliest exited process from the device system logs and determine whether the process belongs to scenario 1 or scenario 2.

1. Log in to the msnpureport tool provided by the physical machine on the server and run the following command to collect device system logs:

    >**NOTE:**
    >For details about how to obtain the tool and parameters, see  [msnpureport Tool](https://support.huawei.com/enterprise/en/ascend-computing/ascend-hdk-pid-252764743?category=reference-guides&subcategory=command-reference).

    ```bash
    msnpureport -f
    ```

    After the command is executed, a folder named after the timestamp is generated in the current path, for example,  **2025-12-20-19-11-27**.

2. Go to the  **slog**  directory of the device log, search for the keyword  **app exit begin**  globally, and sort the results by time.

    ```bash
    cd 2025-12-20-19-11-27/slog
    grep -rn "app exit begin" | grep 2025-12-19-15 | awk -F"):" '{print $2}' | awk '{print $1}' | sort
    ```

    ![](figures/image_0000002506096920.png)

    The number of output lines depends on the number of processes on a single device \(die\). For example, if a single die has only one process, there should be 16 output lines \(corresponding to 16 dies\). If a single die has two processes, there should be 32 output lines. The rest can be deduced by analogy. The output lines are sorted by time in ascending order. The first line indicates the earliest exit time.

    For a cross-server decode instance, you need to check another server in the same EP domain, for example, two servers with 32 dies.

3. Search for the earliest time and determine the device.

    For example, if the earliest timestamp is  **15:50:03.650.471**, run the following command to confirm that the earliest device that exits is device 1:

    ```bash
    grep -rn "app exit begin" | grep 2025-12-19-15 | grep "15:50:03.650.471"
    ```

    ![](figures/image_0000002538136543.png)

    >**NOTE:**
    >Atlas A3 training products/Atlas A3 inference products: This product uses the dual-die architecture. The two dies share the OS.  **dev-os-0**  contains  **device-0**  and  **device-1**.

4. Analyze whether an error is reported before the device 1 process exits and check the direct cause of the error.

    Open the log file of the device 1 process, view the context of  **app exit begin**  at the time when the error is reported, and check whether an error is reported before the process exits and the direct cause of the error.

    ```bash
    vi dev-os-0/debug/device-1/device-1_20251219114418919.log
    ```

    ![](figures/image_0000002537993743.png)

    According to the logs, a task error occurs on device 1 before  **app exit begin**  \(that is, before the process exits\). This error causes the process to exit. The specific symptom is that an error is reported during the execution of the MoE communication operator in the plog of device 1. Therefore, it can be determined that the error is the direct cause of the instance exception.
