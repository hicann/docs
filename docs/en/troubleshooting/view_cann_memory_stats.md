# Checking Memory Statistics of Each CANN Component

1. Check and analyze logs.

    Search for the keyword  **mem\_stats**  in the user-mode plog on the host. The following is an example of the search result. YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

    ```text
    [INFO] DRV(4176893,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176893, 4185695][drv][devmm][_svm_mem_stats_show 148]SVM_MEM Mem stats (Bytes). (module_name=RUNTIME; module_id=7; current_alloced_size=19927040; alloced_peak_size=19927040; alloc_cnt=37; free_cnt=0)
    [INFO] DRV(4176893,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176893, 4185695][drv][devmm][_svm_mem_stats_show 148]DEV_MEM dev6 Mem stats (Bytes). (module_name=HCCL; module_id=3; current_alloced_size=419467264; alloced_peak_size=419500032; alloc_cnt=6; free_cnt=2)
    [INFO] DRV(4176893,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176893, 4185695][drv][devmm][_svm_mem_stats_show 148]DEV_MEM dev6 Mem stats (Bytes). (module_name=APP; module_id=33; current_alloced_size=64680361984; alloced_peak_size=64680361984; alloc_cnt=3113; free_cnt=0)
    ```

    Log level: Memory statistics are printed when the log level is ERROR \(memory allocation fails\) or the process exits.

    Printing format:  **\[_Memory attribute_\] Mem stats \(Bytes\).** **\(module\_name=_\[Module name\]_; module\_id=_\[ID\]_; current\_alloced\_size=_\[Size\]_; alloced\_peak\_size=_\[Size\]_; alloc\_cnt=_\[Size\]_; free\_cnt=_\[Size\]_\)**

    - _Memory attribute_:  **SVM\_MEM**  \(address of page faults, used in CANN\),  **DEV\_MEM**  \(dev memory\),  **HOST\_MEM**  \(host memory\), or  **DVPP\_MEM**  \(DVPP memory\)
    - **module\_name**: module name, for example,  **GE**,  **RUNTIME**, or  **DVPP**.
    - **current\_alloced\_size**: current memory size \(bytes\) occupied by the module.
    - **alloced\_peak\_size**: peak memory size \(bytes\) occupied by the module.
    - **alloc\_cnt**: number of times that memory is allocated.
    - **free\_cnt**: number of times that memory is freed. If the number of times that memory is freed does not match the number of times that memory is allocated, check whether the memory usage is proper. For example, the upper-layer service framework manages the memory in memory pool mode or memory leak occurs.

2. Check which component whose allocated memory increases causes OOM.

    - If you run the application for the first time, check whether the memory usage of each component meets the expectation or exceeds the physical memory of the hardware based on the memory statistics in the logs. If the memory usage does not meet the expectation or exceeds the physical memory of the hardware, adjust the code logic or replan the memory usage.

        Take a model with 13 billion parameters as an example. Each parameter is of the float32 type and occupies 32-bit memory, that is, 4-byte memory. 1 GB equals 1024<sup>3</sup>  bytes. The 13-billion model occupies about the memory of 48.4 GB \(13 x 10<sup>9</sup>  \* 4 \(bytes\) ÷ 1024<sup>3</sup>\). If the current hardware memory is only about 50 GB, there is a high probability that the memory required for running the model exceeds the physical memory of the hardware, causing OOM.

    - If the application is not run for the first time, compare the memory statistics in the historical success scenario with that in the current failure scenario, and check the memory attribute and the value of  **alloced\_peak\_size**  for each module \(Check the  **DEV\_MEM**  attribute since most problems occur because the allocated dev memory is insufficient\). Find the component whose peak value increases and focus on the component whose allocated memory is greatly different from that in the historical success scenario.

        The following is an example of the memory statistics for a historical success scenario \(about 2 GB memory is allocated for the application\):

        ```text
        [INFO] DRV(4052516,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052516, 4052516][drv][devmm][_svm_mem_stats_show 148]DEV_MEM dev0 Mem stats (Bytes). (module_name=RUNTIME; module_id=7; current_alloced_size=44138496; alloced_peak_size=44138496; alloc_cnt=18; free_cnt=0)
        [INFO] DRV(4052516,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052516, 4052516][drv][devmm][_svm_mem_stats_show 148]DEV_MEM dev0 Mem stats (Bytes). (module_name=APP; module_id=33; current_alloced_size=2078195712; alloced_peak_size=2078195712; alloc_cnt=996; free_cnt=0)
        ```

        The following is an example of the memory statistics for the existing failure scenario \(about 20 GB memory is allocated for the application\):

        ```text
        [INFO] DRV(4052522,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052522, 4052522][drv][devmm][_svm_mem_stats_show 148]DEV_MEM dev0 Mem stats (Bytes). (module_name=RUNTIME; module_id=7; current_alloced_size=44138496; alloced_peak_size=44138496; alloc_cnt=18; free_cnt=0)
        [INFO] DRV(4052522,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052522, 4052522][drv][devmm][_svm_mem_stats_show 148]DEV_MEM dev0 Mem stats (Bytes). (module_name=APP; module_id=33; current_alloced_size=20781957120; alloced_peak_size=20781957120; alloc_cnt=996; free_cnt=0)
        ```

    **Note:**

    - If the statistics shows that the component whose  **module\_name**  is  **APP**  uses a large amount of memory, the application process uses a large amount of memory. In this case, you need to analyze the difference between the allocated memory and the estimated memory. If the difference is large, you need to analyze the cause, locate the fault, and optimize the memory allocation logic in the application code.
    - If the value of  **module\_name**  is  **GE**,  **RUNTIME**, or  **HCCL**, the memory is used by the CANN component. Check whether the memory usage of the CANN component is high based on the following memory usage values:
        - In training scenarios, the memory usage of CANN components varies depending on the framework. The following uses the PyTorch framework as an example. The memory usage of key components is listed below for reference. If a CANN component uses a large amount of memory, contact technical support.
            - GE: about 3 MB
            - RUNTIME: about 26 MB
            - HCCL: Memory usage = Memory used by communication links + Buffer memory. The memory used by communication links depends on the cluster scale and communication links. The memory used by buffers depends on the number of communicators and the buffer size used by a single communicator.

                For example, there are 1,024 servers in a cluster, 10 communication links and 3 communicators need to be established, and each communicator occupies the sending and receiving memory of 2 x  **HCCL\_BUFFSIZE**. \(**HCCL\_BUFFSIZE**  is an environment variable and is configured by the user. The default value is 200 MB.\) In this case, the memory usage calculation formulas are as follows: Memory used by communication links in single-operator mode = Number of communication links x 4 MB = 10 x 4 MB = 40 MB; Memory used by communication links in graph mode = Number of communication links x Number of operators in the graph x 0.3 MB = 10 x Number of operators in the graph x 0.3 MB = Number of operators in the graph x 3 MB; Buffer memory = Number of communicators x Sending and receiving memory occupied by each communicator = 3 x 2 x 200 MB.

        - In inference scenarios, take the PyTorch model as an example. The following lists the memory usage of key components when the model is converted into the  AI processor-adapted offline model  for inference. The memory usage can be used for reference during problem analysis. If a CANN component uses a large amount of memory, contact technical support.
            - GE: about 86 MB
            - RUNTIME: about 18 MB

    - You can use the msSanitizer memory detection tool in the  [Operator Development Tool](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/latest/devaids/optool/MindStudio/26.1.0/en/user_guide/msot_user_guide.md)  to locate memory problems of user applications. Currently, this tool supports only  Atlas A2 training products   and  Atlas inference products.
