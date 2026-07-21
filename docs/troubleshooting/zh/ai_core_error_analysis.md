# AI Core Error问题定位思路

您可以按如下步骤定位问题，若无法解决问题，再联系技术支持。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。

**图 1**  AI Core问题定位流程  
![](figures/aicore_error_locating.png "AI Core问题定位流程")

准备阶段，需收集故障信息，包括：CANN日志文件、exception dump文件、算子编译信息（\*.o和\*.json）。如何收集故障信息，请参见[收集AI Core Error问题信息](collect_ai_core_error_info.md)。

定位阶段如下：

1. 排查RAS硬件故障。

    RAS硬件故障是指与硬件的可靠性（Reliability）、可用性（Availability）和可服务性（Serviceability）有关的故障。

    从收集的日志中，在slog/dev-os-_id_/run/event/event\_\*.log中找到发生AI Core Error问题附近时间、对应Device的系统日志，检查日志中是否存在“event\_id”关键字，若不存在，则跳转到下一步继续排查；若存在，则获取“event\_id”的值（即RAS硬件故障码），单击《[健康管理故障定义](https://support.huawei.com/enterprise/zh/ascend-computing/ascend-hdk-pid-252764743)》获取对应版本的手册并查阅其中的解决方法，典型问题案例请参见[HBM比特ECC故障](hbm_bit_ecc_fault.md)、[icache数据校验故障](icache_data_validation_fault.md)、[AI Core超时故障](ai_core_timeout_fault.md)。

2. 排查NPU硬件故障。

    从收集的应用类日志中，找到发生AI Core Error问题附近时间的日志log/\[run|debug\]/plog/plog-_pid_\_\*.log，检查日志中的报错信息是否存在ECC相关报错（报错中有“ECC”或“ECC error”关键字）或者存在多次报错在同一个chipId上：

    - 若不存在，则跳转到[3](#li7527192804020)继续排查；

        若存在，则继续使用ascend-dmi工具压测AI Core，若压测异常，则表示已知硬件故障，需联系技术支持更换硬件（典型问题案例请参见[AI Core硬件故障](ai_core_hardware_fault.md)）；若压测正常，则需要在程序中指定其它Device，再执行程序看问题是否可以复现，如果复现则跳转[3](#li7527192804020)继续排查，如果不复现则表示可能为硬件故障，需联系技术支持更换硬件。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。

        ascend-dmi工具需要单独安装，压测AI Core的命令示例如下，若报错**GENERAL\_WARN**或**EMERGENCY\_WARN**表示可能存在AI Core问题：

        ```bash
        ascend-dmi --dg -i aicore -s
        ```

        ascend-dmi工具在MindCluster ToolBox软件包中，该软件与CANN的配套关系请单击[Link](https://www.hiascend.com/developer/download/community/result?module=dl+cann)查询，ascend-dmi工具的安装及详细使用指导请参见[Link](https://hiascend.com/document/redirect/mindxdl-ascenddmiug)。

3. 排查软件故障。<a id="li7527192804020"></a>

    1. 从收集的应用类日志中，找到发生AI Core Error问题附近时间的日志log/\[run|debug\]/plog/plog-_pid_\_\*.log，检查日志中是否存在索引类算子0x800000的报错，若不存在，则跳转到下一步继续排查；若存在，则参考[索引类算子索引越界](operator_index_out_of_bounds.md)排查算子输入数据问题。

        典型索引类算子包括GatherV2、Scatter、GatherElements等。

    2. 借助msaicerr工具分析准备阶段收集的信息，msaicerr工具输出分析报告（info.txt文件），将执行msaicerr工具的结果数据（包括分析AI Core Error问题的最小集信息、分析报告等）提供给技术支持，待进一步分析定位。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。

        msaicerr工具的详细操作请参见[使用msaicerr工具分析AI Core Error问题](use_msaicerr_ai_core_err.md)。
