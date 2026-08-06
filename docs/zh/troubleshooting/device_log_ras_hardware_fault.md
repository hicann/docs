# 通过Device日志获取故障ID并排查RAS硬件故障

RAS硬件故障是指与硬件的可靠性（Reliability）、可用性（Availability）和可服务性（Serviceability）有关的故障。此处可通过日志中的“event\_id”的值（即RAS硬件故障码），在对应版本的故障码手册中查找解决方法。

**图 1**  排查流程  
![](figures/RAS_faults_obtaining_event_id.png "排查流程")

1. 在Host侧服务器上，通过msnpureport工具导出Device侧系统类日志和其他维测信息，包括slog日志、syslog日志、event日志、黑匣子等。

    在某个有读、写、执行权限的目录（如“/var/log/npu/report”，下文以此路径为例）下执行msnpureport工具。

    msnpureport工具命令示例如下：

    ```bash
    msnpureport -f
    ```

    导出的日志和文件默认存放在/var/log/npu/report目录下。

2. 从第1步中收集的event日志（slog/dev-os-_id_/run/event/event\_\*.log）中找到**发生问题附近时间**、**对应Device**的日志内容，检查日志中是否存在“event\_id”关键字，若不存在，则跳转到第3步继续排查；若存在，则单击《[健康管理故障定义](https://support.huawei.com/enterprise/zh/ascend-computing/ascend-hdk-pid-252764743)》获取对应版本的手册并查阅其中的解决方法。

    如果slog日志中的时间与发生问题的时间相距较远，则旧日志可能已经被覆盖或清理，这种场景也会导致搜不到问题相关的“event\_id”。

    此时，还可以使用npu-smi命令查询指定芯片健康状态，若存在RAS故障，则最多可以查询到最近8次故障的event id，可作为定位问题时参考：

    npu-smi命令示例如下（_id_表示设备ID，_chip\_id_表示芯片ID，可以先使用**npu-smi info**命令获取设备ID和芯片ID）：

    ```bash
    npu-smi info -t health -i id -c chip_id
    ```

    查询结果示例如下：

    ![](figures/zh-cn_image_0000001937528841.png)

3. 从第1步中收集的黑匣子日志中，在hisi\_logs/device-_id_/\*/bbox目录下找到发生问题附近时间、对应Device的黑匣子日志，检查日志中是否存在“Hardware Error”关键字，若不存在，则表示暂未识别到硬件故障；若存在，表示未知硬件问题，需联系技术支持进一步定位处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
