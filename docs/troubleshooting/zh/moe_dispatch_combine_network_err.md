# 网络问题导致Moe Dispatch/Combine算子执行报错

## 问题现象

Atlas A3 训练系列产品/Atlas A3 推理系列产品场景下，Host侧Runtime执行报错，在应用程序运行日志中Runtime打印了fault kernel\_name和func\_name的关键信息，其中fault kernel\_name为MoeDistributeDispatchV2、MoeDistributeCombineV2算子，报错Error为“ errcode:\(0x800000, 0, 0\) errorStr: The DDR address of the MTE instruction is out of range”。

Ascend EP形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/plog路径下，日志文件为plog-_pid\_\*_.log。

```bash
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:05.598.128 [stars_engine.cc:1502]1254 ProcLogicCqReport:Task run failed, device_id=9, stream_id=3, task_id=5981, sqe_type=7(notify wait), errType=0x20(sq sw status error), sqSwStatus=0x16620324
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:05.598.682 [device_error_core_proc.cc:333]1254 ProcessStarsCoreErrorInfo:report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:05.598.690 [device_error_core_proc.cc:333]1254 ProcessStarsCoreErrorInfo:The error from device(chipId:4, dieId:1), serial number is 1, there is an exception of fftsplus aivector error, core id is 18, error code = 0x800000, dump info: pc start: 0x12c0c6ce5000, current: 0x12c0c6ce5a6c, vec error info: 0xc3117b71b5, mte error info: 0x960700006b, ifu error info: 0x77688bb0aec0, ccu error info: 0x7ccdbee64ba3149b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c0c86c2a98.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:05.598.722 [device_error_core_proc.cc:353]1254 ProcessStarsCoreErrorInfo:report error module_type=5, module_name=EZ9999
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:05.598.725 [device_error_core_proc.cc:353]1254 ProcessStarsCoreErrorInfo:The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x700006b, fixp_error1 info: 0x96, fsmId:1, tslot:7, thread:0, ctxid:0, blk:1, sublk:0, subErrType:4.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.237 [device_error_core_proc.cc:246]1254 HasMemUceErr:Get isSmmuFault is 0.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.245 [device_error_core_proc.cc:369]1254 ProcessStarsCoreErrorInfo:mte error, devId=9, streamId=1634, taskId=804, errorCode=546.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.263 [stream.cc:3285]1254 EnterFailureAbort:stream_id=3 enter failure abort.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.281 [stream.cc:1188]1254 GetError:Stream Synchronize failed, stream_id=3, retCode=0x222, [suspect remote error].
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.285 [model_execute_task_info.cc:593]1254 ReportErrorInfoForModelExecuteTask:model execute error, retCode=0x91, [the model stream execute failed].
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.324 [model_execute_task_info.cc:551]1254 PrintErrorInfoForModelExecuteTask:stream_id=3, task_id=5980, sqVirtualAddr=0, head equal tail flag=0.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.326 [model_execute_task_info.cc:507]1254 PrintErrorModelExecuteTaskFuncCall:funcCallSvmMem=0x1252011a9000, funCallMemSize=816.
[ERROR] RUNTIME(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.764 [davinci_kernel_task.cc:1471]1254 PrintErrorInfoForDavinciTask:Aicore kernel execute failed, device_id=9, stream_id=1634, report_stream_id=3, task_id=804, flip_num=0, fault kernel_name=te_moedistributecombinev2_2dec9514b32cf64e557fcc584b62d9e99571340395f19b500a6362eb101348634ff5f1847bfbf56fb634f3ea4a8c75f0fc95d46f8ac4af1a2420c2bb85b154c9_static_bin, fault kernel info ext=te_moedistributecombinev2_2dec9514b32cf64e557fcc584b62d9e99571340395f19b500a6362eb10134863, program id=213, hash=12167788236099877968.
[ERROR] GE(1254,ker_DP25_EP25):2025-12-19-15:50:06.805.807 [error_tracking.cc:113]1254 ErrorTrackingCallback: ErrorNo: 4294967295(failed) Error happened, origin_op_name [MoeDistributeCombineV2_48], op_name [MoeDistributeCombineV2_48], task_id 804, stream_id 1634.
```

## 可能导致的故障

该问题会导致流同步失败，acl接口报错“Execute model failed”，并记录在plog日志中，最终可能会导致推理服务中断。

```bash
[ERROR] ASCENDCL(4150867,msame):2022-09-22-09:27:46.404.834 [model.cpp:699]4150867 ModelExecute: [EXEC][DEFAULT][Exec][Model]Execute model failed, ge result[507011], modelId[1]
[ERROR] ASCENDCL(4150867,msame):2022-09-22-09:27:46.404.857 [model.cpp:1547]4150867 aclmdlExecute: [EXEC][DEFAULT][Exec][Model]modelId[1] execute failed, result[507011]
```

<a id="section20876063"></a>

## 可能原因

- 原因1：如果该问题是服务启动后必定出现的问题，请检查EP域的组成Rank是否跨越了超节点：MTE方案依赖HCCS链路，算子执行Rank的通信域必须在一个超节点内。
- 原因2：（长稳时高优排查）检查报错时间点是否出现网络交换机故障，例如网络闪断、交换机故障、光链路问题导致超时代答等。灵渠网络的超时代答机制会使跨卡通信算子以error code为0x800000的“MTE out of range”报错形式表现。
- 原因3：（长稳时高优排查）排查EP域其他卡上的服务进程有无异常退出：远端进程退出会导致映射至本端的远端进程地址资源释放，本端通信访问远端时会表现为算子error code为0x800000的“MTE out of range”报错，需要找到远端进程退出原因，可优先确认是否有core文件产生。
- 原因4：如果所有卡都存在报错，请确认报错时间点，优先排查最先报错的几张卡ERROR（实例被推理服务主动释放退出时，其他卡可能来不及报错，plog无报错信息）。
- 原因5：若上述表现均正常，可以梳理进程退出的先后顺序，找到最先退出的进程，分析该进程退出的原因。

## 解决方法

1. 收集所有Rank的plog日志，并按照[可能原因](#section20876063)进行环境、日志排查确认。
2. 在plog日志中搜索关键字fault\_kernel\_name，确认所有卡是否存在算子报错。
    - 场景1：如果plog日志有报错信息，参见第4步，按报错时间顺序分析，先查看首报错日志信息。
    - 场景2：如果EP域Rank对应的plog日志无报错信息，检查对应Rank有无Host CoreDump现象，并优先确认coreDump问题。若无Host异常，参见第3步，通过Device系统日志确认业务退出时间点。

3. 基于msnpureport工具收集Server端Device系统日志（实例跨多Server时都要收集），进入slog目录，全局搜索关键字“app exit begin”并按照时间排序，确认首报错Rank再进行第4步。详细的处理过程可参见[故障示例](#section5623024911)。
4. 对首报错信息进行排序。

    若首报错卡plog日志的op\_type为MoedistributeDispatch或MoeDistributeCombine，且错误为“The DDR address of the MTE instruction is out of range”，请检查报错时间点是否存在网络交换机故障；否则EP域内的“The DDR address of the MTE instruction is out of range”报错为首报错进程异常所导致，需进一步检查Rank在退出时间点的HOST、plog日志，检查是否有其他异常行为。

5. 若仍未解决问题，您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。

<a id="section5623024911"></a>

## 故障示例

本示例通过Device系统类日志找到最早退出的进程，并确认其属于上述的场景1或场景2。

1. 登陆Server物理机自带的msnpureport工具，执行如下命令收集Device系统类日志。

    >**说明：** 
    >工具的获取和参数介绍参见[《msnpureport工具》](https://support.huawei.com/enterprise/zh/ascend-computing/ascend-hdk-pid-252764743?category=reference-guides&subcategory=command-reference)。

    ```bash
    msnpureport -f 
    ```

    执行完后，在当前路径下生成以时间戳命名的文件夹，假设为“2025-12-20-19-11-27”。

2. 进入Device日志slog目录，全局搜索"app exit begin"关键字并按时间排序。

    ```bash
    cd 2025-12-20-19-11-27/slog
    grep -rn "app exit begin" | grep 2025-12-19-15 | awk -F"):" '{print $2}' | awk '{print $1}' | sort
    ```

    ![](figures/zh-cn_image_0000002506096920.png)

    输出行数取决于单Device（die）上进程数量，如单die只有1个进程，应该会有16条（对应16个die）；如果单die有2进程，会有32条，依此类推。输出按时间从小到大排序，第一行为最早退出时间。

    跨Server的decode实例，需将同个EP域内另外一个Server一并查看，如两机32die。

3. 根据最早时间搜索并确认是哪张卡。

    例如确认最早的时间戳是 “15:50:03.650.471“，执行如下命令，确认最早退出的device为device-1。

    ```bash
    grep -rn "app exit begin" | grep 2025-12-19-15 | grep "15:50:03.650.471"
    ```

    ![](figures/zh-cn_image_0000002538136543.png)

    >**说明：** 
    >Atlas A3 训练系列产品/Atlas A3 推理系列产品：该产品为双die架构，两个die共用os，dev-os-0内包含了device-0和device-1。

4. 分析device-1进程退出前有无报错以及报错的直接原因。

    打开device-1进程log文件，查看对应报错时间点的"app exit begin"上下文，检查进程退出前有无报错和报错的直接原因。

    ```bash
    vi dev-os-0/debug/device-1/device-1_20251219114418919.log
    ```

    ![](figures/zh-cn_image_0000002537993743.png)

    通过日志发现device-1在“app exit begin”前（即退进程动作开始前）发生了task error。这个error导致了进程退出，具体表现为device-1的plog中Moe通信算子执行报错。因此，基本可以确认该报错是引发实例异常的直接原因。
