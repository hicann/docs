# 查看日志

日志主要用于记录系统的运行过程及异常信息，帮助用户快速定位系统运行过程中出现的问题以及开发过程中的程序调试问题。日志分为如下几类：

- **系统类日志**：系统运行时在Device侧产生的日志。主要包括：
    - Control CPU上的系统类日志，包括内核态日志和系统进程运行产生的用户态日志，主要反映AI处理器的整体运行情况。
    - 非Control CPU（例如低功耗）上的系统类日志，主要反映低功耗、Task Scheduler、ISP等组件的运行情况。

- **应用类日志**：AI应用程序运行产生的日志。主要包括：
    - Host侧AscendCL、GE、Runtime、HCCL等组件打印的日志。
    - Device侧AI CPU进程打印的日志。

如何查看日志、设置日志级别等描述请参见[《日志参考》](https://hiascend.com/document/redirect/CannCommunitylogref)。
