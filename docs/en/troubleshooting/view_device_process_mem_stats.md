# Checking the Memory Statistics of the Device Service Processes

1. Check and analyze logs.

    Search for the keyword  **DEV\_PROC\_MEM**  in the user-mode plog on the host. The following is an example of the search result:

    ```text
    [INFO] DRV(4176893,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176893, 4185695][drv][devmm][svm_mem_stats_show_device_proc_mem 358]DEV_PROC_MEM dev6 Mem stats (Bytes). (module_name=AICPU; module_id=36; total_size=75464704)
    [INFO] DRV(4176893,python3.7):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4176893, 4185695][drv][devmm][svm_mem_stats_show_device_proc_mem 358]DEV_PROC_MEM dev6 Mem stats (Bytes). (module_name=CUSTOM; module_id=76; total_size=75464704)
    ```

    **DEV\_PROC\_MEM**  indicates a process on the device.  **module\_name**  is used to identify a process on the device \(such as the AI CPU process, custom operator CUSTOM process, or HCCP process\).  **total\_size**  indicates the physical memory used by each process, including the resident physical memory occupied by malloc of the process and the sharedpool memory allocated for the process to call the buff allocation API.

2. **Check which device service process whose allocated memory increases causes OOM.**
    - If you run the application for the first time, check whether the memory usage of each process meets the expectation or exceeds the physical memory of the hardware based on the memory statistics in the logs. If the memory usage does not meet the expectation or exceeds the physical memory of the hardware, contact technical support for further fault locating.
    - If the application is not run for the first time, compare the memory statistics in the historical success scenario with that in the current failure scenario to focus on the service process whose allocated memory is greatly different from that in the historical success scenario.

        The following is an example of the memory statistics for a historical success scenario \(about 72 MB memory is allocated for the AI CPU process\):

        ```text
        [INFO] DRV(4052516,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052516, 4052516][drv][devmm][svm_mem_stats_show_device_proc_mem 358]DEV_PROC_MEM dev0 Mem stats (Bytes). (module_name=AICPU; module_id=36; total_size=75505664)
        [INFO] DRV(4052516,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052516, 4052516][drv][devmm][svm_mem_stats_show_device_proc_mem 358]DEV_PROC_MEM dev0 Mem stats (Bytes). (module_name=CUSTOM; module_id=76; total_size=75505664)
        ```

        The following is an example of the memory statistics for the existing failure scenario \(about 150 MB memory is allocated for the AI CPU process\):

        ```text
        [INFO] DRV(4052533,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052533, 4052533][drv][devmm][svm_mem_stats_show_device_proc_mem 358]DEV_PROC_MEM dev0 Mem stats (Bytes). (module_name=AICPU; module_id=36; total_size=157286400)
        [INFO] DRV(4052533,main_aarch64):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [ascend][curpid: 4052533, 4052533][drv][devmm][svm_mem_stats_show_device_proc_mem 358]DEV_PROC_MEM dev0 Mem stats (Bytes). (module_name=CUSTOM; module_id=76; total_size=75505664)
        ```
