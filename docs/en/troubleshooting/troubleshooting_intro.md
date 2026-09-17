# Troubleshooting Overview

This document provides self-service fault locating and troubleshooting methods based on various fault symptoms that developers may encounter during inference and training, helping developers quickly locate and rectify faults. The content includes error code information printed on the screen and troubleshooting methods, one-click log collection, and usage of various fault locating tools.

The troubleshooting process includes collecting the fault information, analyzing the fault cause, and rectifying the fault.  Figure 1 shows the troubleshooting process.

**Figure  1**  Troubleshooting process
![](figures/troubleshooting-process.png "troubleshooting-process")

- Collecting the fault information

    Collect fault information as it is critical to troubleshooting. The information includes but is not limited to logs and environment information.

    Fault information includes application logs, on-device system logs, and other maintenance and debugging information.

    - Application logs: record user-mode logs generated when applications run on the host and device. The common log is  **plog-_pid_\__\*_.log**, which is usually called plog.

        For details about log levels, log paths, and log files, see  [Log Reference](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/logreference/logreference_0001.html).

    - On-device system logs and other maintenance and debugging information: record system running information, including kernel-mode logs and user-mode logs generated during system process running.

        On-device system logs and other maintenance and debugging information need to be exported to the host using the msnpureport tool. For details about the usage and restrictions, see  [msnpureport Tool](https://support.huawei.com/enterprise/en/ascend-computing/ascend-hdk-pid-252764743?category=reference-guides&subcategory=command-reference).

- Analyzing the fault cause

    Analyzing the cause of a fault is a process of finding out the cause of the fault from multiple possible causes. Analyze and compare these possible causes using certain methods or measures and determine the specific cause of the fault.

    Log information can be analyzed using the top-to-bottom log analysis method typically. Fault symptoms are narrowed down to the bottom layer based on the service process.

- Rectifying the fault

    Rectify the fault based on its possible causes.

    Record key information about the troubleshooting process, and provide preventive measures and workarounds to avoid similar faults.

>**NOTE:**
>The third-party tools \(such as eseye u and Netron\) involved in the troubleshooting process provided in this document are only examples. You can replace them with other similar tools to meet your actual requirements.
