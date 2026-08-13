# 通过Device日志查看资源占用过高的信息

有些业务程序运行异常的情况可能由于Device的内存被耗尽、CPU占用率过高、文件句柄数达到上限、进程数达到上限等问题引起，因此在定位问题时，我们可以通过日志中的一些关键信息排查这部分问题。

1. 在Host侧服务器上，在某个有读、写、执行权限的目录（如“/var/log/npu/report”，下文以此路径为例）下执行msnpureport工具，通过msnpureport工具导出Device侧系统类日志和其他维测信息。

    msnpureport工具命令示例如下：

    ```bash
    msnpureport -f
    ```

    Device侧系统进程产生的运行日志默认在/var/log/npu/report/\*/slog/device-os-_id_/run/device-os/目录下，其中，\*表示时间戳，device-os-_id_中的_id_表示Device ID_。_

2. 在Device侧系统进程产生的运行日志中，通过SYSMONITOR模块的日志查看资源占用情况，包括内存占用率、CPU占用率、文件句柄数、僵尸进程数。日志片段中的YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。
    - 查看内存占用率

        **memory usage alarm**：出现了内存占用率超过阈值上限（90%）的告警。

        **memory usage stat**：一个周期（一小时）结束时，如果周期内有告警事件，打印该周期的统计结果。

        ```bash
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_monitor_frame.c:60][tid:2168] system resource monitor start, period: 10000ms
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:233][tid:2168] memory usage alarm: 93.7%
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] PID VSZ %VSZ COMMAND
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2112 950m 2.1 /usr/bin/mdc/base-plat/aosservice/iammgr
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2096 969m 2.1 /var/slogd
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2142 734m 1.6 /var/resource_mgr
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2088 726m 1.6 /usr/bin/mdc/base-plat/process-manager/process-manager
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2150 622m 1.4 /var/log-daemon
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2241 522m 1.1 /var/tsdaemon
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2195 510m 1.1 /usr/bin/mdc/base-plat/process-manager/proc_launcher
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2155 486m 1.0 /var/dmp_daemon
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2222 284m 0.6 /var/hdcd
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:225][tid:2168] 2211 284m 0.6 /var/hdcd
        [INFO] SYSMONITOR(2150,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_memory_monitor.c:251][tid:2168] memory usage stat: minUsage= 2.3%, maxUsage=93.7%, avgUsage= 2.6%, alarmNum=1, resumeNum=1, duration=10000ms
        ```

    - 查看CPU占用率

        **cpu usage alarm**：某个cpu占用率超过阈值上限（90%）时，会将Device上所有cpu的占用率都打印出来。

        **cpu usage stat**：一个周期（一小时）结束时，如果周期内有告警事件，打印该周期的统计结果。

        ```bash
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:216][tid:4739] cpu usage alarm, total: 17.6%, cpu0: 100.0%, cpu1:  5.6%, cpu2: 13.4%, cpu3: 17.6%, cpu4:  1.0%, cpu5:  0.7%, cpu6:  0.7%, cpu7:  0.7%
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]   PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]   492     2 root     RW       0  0.0   0  9.3 [kcompactd32]
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  7623  4989 HwHiAiUs S<   14.0t22939.3   0  3.4 aicpu_scheduler --deviceId=0 --pid=2547436 --pidSign=000000000000000000000000000000000000000000000000 --profilingMode=0 --vfId=0 --logLevelInPid=103 --ccecpuLogLevel= --aicpuLogLevel= --deviceMode=0 --aicpuSchedMode=0 --groupNameList= --groupNameNum=0 --hostProcName=
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  7645  4989 HwHiAiUs S<    553m  0.8   0  2.3 hccp_service.bin --deviceId=0 --pid=2547436 --pidSign=000000000000000000000000000000000000000000000000 --logLevelInPid=103 --hdcType=18
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739] 30582 30581 HwHiAiUs R    11632  0.0   0  1.1 top -bn1
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  4989  4659 HwHiAiUs S<   2196m  3.4   0  0.0 /var/tsdaemon
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  4726  4659 HwDmUser S<   1675m  2.6   0  0.0 /var/dmp_daemon -I -U 8087
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  4667  4659 HwHiAiUs S    1541m  2.4   0  0.0 /var/slogd -n
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  4926  4659 HwHiAiUs S<   1261m  1.9   0  0.0 /var/hdcd 3
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  4659     1 root     S     884m  1.3   0  0.0 /usr/bin/mdc/base-plat/process-manager/process-manager /etc/mdc/base-plat/process-manager/startup_procmgr.yaml
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:199][tid:4739]  4722  4659 HwHiAiUs S     876m  1.3   0  0.0 /var/log-daemon -n
        [INFO] SYSMONITOR(4722,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_cpu_monitor.c:184][tid:4739] cpu usage stat: minUsage= 1.8%, maxUsage=100%, avgUsage= 3.6%, alarmNum=1, resumeNum=1, duration=10000ms
        ```

    - 查看文件句柄数

        **fd usage alarm**：出现了文件句柄使用率超过阈值上限（90%）的告警。

        **fd usage stat**： 一个周期（一小时）结束时，如果周期内有告警事件，打印该周期的统计结果。

        ```bash
        [INFO] SYSMONITOR(2170,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_fd_monitor.c:156][tid:2187] fd total: 4454775, used: 4445866, fd usage alarm: 99.8%
        [INFO] SYSMONITOR(2170,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_fd_monitor.c:126][tid:2187] sysmonitor fd process top three
        [INFO] SYSMONITOR(2170,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_fd_monitor.c:147][tid:2187] pid: 12170 , fd used: 4445532
        [INFO] SYSMONITOR(2170,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_fd_monitor.c:147][tid:2187] pid: 2271 , fd used: 28
        [INFO] SYSMONITOR(2170,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_fd_monitor.c:147][tid:2187] pid: 2116 , fd used: 26
        [INFO] SYSMONITOR(2170,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [INFO] SYSMONITOR(2170,log-daemon):2024-05-15-03:27:43.856.787 [sys_fd_monitor.c:162][tid:2187] fd usage stat: minUsage= 0.0%, maxUsage= 99.8%, avgUsage= 87.3%, alarmNum=1, resumeNum=1, duration=80000ms
        ```

    - 查看僵尸进程数

        **zombie process count alarm**：出现了僵尸进程数超过阈值上限（5）的告警。

        **zombie process count stat**：一个周期（一小时）结束时，如果周期内有告警事件，打印该周期的统计结果。

        ```bash
        [INFO] SYSMONITOR(2166,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_zp_monitor.c:119][tid:2195] zombie process count alarm: 98
        [INFO] SYSMONITOR(2166,log-daemon):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [sys_zp_monitor.c:134][tid:2195] zombie process count stat: minCount=0, maxCount=98, avgCount=98, alarmNum=1, resumeNum=0, duration=120000ms
        ```
