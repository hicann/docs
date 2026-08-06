# 采集&解析性能数据

本节介绍**推理**场景下使用**msprof命令行**方式采集和解析性能数据、并通过生成的结果文件分析性能瓶颈的基本方法。**在使用msprof命令行前**，您需要先参见[《性能调优工具》](https://hiascend.com/document/redirect/CannCommunityToolProfiling)准备好环境、了解使用约束以及基本的参数使用方法。

## 采集、解析并导出性能数据

1. 登录装有Toolkit软件包的运行环境，执行如下命令，可一键式采集、解析并导出性能数据：

    ```bash
    msprof --output=/home/HwHiAiUser/profiling_output /home/HwHiAiUser/HIAI_PROJECTS/MyAppname/out/main
    ```

    **表 1**  参数说明

    | 参数 | 描述 | 可选/必选 |
| --- | --- | --- |
| --output | 收集到的Profiling数据的存放路径，默认为AI任务文件所在目录。路径中不能包含特殊字符："\n", "\f", "\r", "\b", "\t", "\v", "\u007F"。 | 可选 |

    命令执行完成后，在output指定的目录下生成PROF_\__XXX目录，存放自动解析后的性能数据（以下仅展示性能数据）。

    ```bash
    ├── device_{id}   //保存原始数据，用户无需关注
    │    └── data
    └── mindstudio_profiler_output
          ├── msprof_{timestamp}.json
          ├── step_trace_{timestamp}.json
          ├── xx_*.csv
           ...
          └── README.txt
    ```

2. 进入mindstudio\_profiler\_output目录，查看性能数据文件。

    默认情况下采集到的文件如表2所示。

    **表 2**  msprof默认配置采集的性能数据文件

    | 文件名 | 说明 |
| --- | --- |
| msprof_*.json | timeline数据总表。 |
| step_trace_*.json | 迭代轨迹数据，每轮迭代的耗时。单算子场景下无此性能数据文件。 |
| op_summary_*.csv | AI Core和AI CPU算子数据。 |
| op_statistic_*.csv | AI Core和AI CPU算子调用次数及耗时统计。 |
| step_trace_*.csv | 迭代轨迹数据。单算子场景下无此性能数据文件。 |
| task_time_*.csv | Task Scheduler任务调度信息。 |
| fusion_op_*.csv | 模型中算子融合前后信息。单算子场景下无此性能数据文件。 |
| api_statistic_*.csv | 用于统计CANN层的API执行耗时信息。 |
| prof_rule_0_*.json | 调优建议。 |
| 注：“*”表示{timestamp}时间戳。 |  |

    - json文件需要在Chrome浏览器中输入**chrome://tracing**，将文件拖到空白处进行打开，通过键盘上的快捷键（w：放大，s：缩小，a：左移，d：右移）。通过该文件可查看当前AI任务运行的时序信息，比如运行过程中接口调用时间线，如图1所示。

        **图 1**  查看json文件  
        ![](figures/查看json文件.png "查看json文件")

    - csv文件可直接打开查看。通过该文件可以看到AI任务运行时的软硬件数据，比如各算子在AI处理器软硬件上的运行耗时，通过字段排序等可以快速找出需要的信息，如图2所示。

        **图 2**  查看csv文件  
        ![](figures/查看csv文件.png "查看csv文件")

## 性能分析

从上文我们可以看到，性能数据文件较多，分析方法也较灵活，以下介绍几个重要文件及分析方法。

- 通过msprof\_\*.json文件从整体角度查看AI任务运行的时序信息，进而分析出可能存在的瓶颈点。

    **图 3**  msprof\_\*.json文件示例  
    ![](figures/msprof_-json文件示例.png "msprof_-json文件示例")

    - 区域1：CANN层数据，主要包含Runtime等组件以及Node（算子）的耗时数据。
    - 区域2：底层NPU数据，主要包含Ascend Hardware下各个Stream任务流的耗时数据和迭代轨迹数据、AI处理器系统数据等。
    - 区域3：展示timeline中各算子、接口的详细信息（单击各个timeline色块展示）。

    从上图可以大致分析出耗时较长的API、算子、任务流等，并且根据对应的箭头指向找出对应的下发关系，分析执行推理过程中下层具体耗时较长的任务，查看区域3的耗时较长的接口和算子，再结合csv文件进行量化分析，定位出具体的性能瓶颈。

- 通过op\_statistic\_\*.csv文件分析各类算子的调用总时间、总次数等，排查某类算子总耗时是否较长，进而分析这类算子是否有优化空间。

    **图 4**  op\_statistic\_\*.csv文件示例  
    ![](figures/op_statistic_-csv文件示例.png "op_statistic_-csv文件示例")

    可以按照Total Time排序，找出哪类算子耗时较长。

- 通过op\_summary\_\*.csv文件分析具体某个算子的信息和耗时情况，从而找出高耗时算子，进而分析该算子是否有优化空间。

    **图 5**  op\_summary\_\*.csv文件示例  
    ![](figures/op_summary_-csv文件示例.png "op_summary_-csv文件示例")

    Task Duration字段为算子耗时信息，可以按照Task Duration排序，找出高耗时算子；也可以按照Task Type排序，查看不同核（AI Core和AI CPU）上运行的高耗时算子。
