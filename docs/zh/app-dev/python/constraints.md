# 使用约束

- 进入系统休眠前，需要确保将正在运行的AI推理业务、媒体数据处理业务等进程退出。等待唤醒成功后，再继续执行业务。
- 不支持使用fork函数创建多个进程，且在进程中调用pyacl接口的场景，否则进程运行时会报错或者卡死。
- 不支持在`acl.rt.memcpy_async`、`acl.rt.memset_async`接口等异步操作内存过程中使用fork以及封装了fork的函数，如system、posix\_spawnp等，否则会导致进程运行时会报错，甚至卡死等不可预期的错误。
- 对于创建类接口（例如：`acl.rt.create_stream`、`acl.rt.create_event`、`acl.create_data_buffer`等），用户调用该类接口创建对应的资源后，资源使用完成后，建议及时调用对应的销毁类接口（例如：`acl.rt.destroy_stream`、`acl.rt.destroy_event`、`acl.destroy_data_buffer`等），否则，程序可能会异常。
- 对于销毁类接口（例如：`acl.rt.destroy_stream`、`acl.rt.destroy_event`、`acl.rt.free`、`acl.destroy_data_buffer`等），用户调用该类接口后，不能继续使用已释放或销毁的资源，建议用户调用销毁类接口后，将相关资源设置为无效值（例如，设置为None）。
<!-- npu="910" id1 -->
- 对于**Atlas训练系列产品**，物理机场景下，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数\*64个进程；虚拟机场景下，一个Device上最多只能支持32个用户进程，Host最多只能支持Device个数\*32个进程。
<!-- end id1 -->
<!-- npu="310p" id2 -->
- 对于**Atlas推理系列产品**，物理机场景下，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数\*64个进程；虚拟机场景下，一个Device上最多只能支持32个用户进程，Host最多只能支持Device个数\*32个进程。
<!-- end id2 -->
<!-- npu="310b" id3 -->
- 对于**Atlas 200I/500 A2推理产品**，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数\*64个进程。
<!-- end id3 -->
<!-- npu="910b" id4 -->
- 对于**Atlas A2系列产品**，一个Device上最多只能支持63个用户进程，Host最多只能支持Device个数\*63个进程。
<!-- end id4 -->
<!-- npu="A3" id5 -->
- 对于**Atlas A3系列产品**，一个Device上最多只能支持63个用户进程，Host最多只能支持Device个数\*63个进程。
<!-- end id5 -->
<!-- npu="950" id6 -->
- 对于**Ascend 950PR&950DT系列产品**，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数\*64个进程。
<!-- end id6 -->
- 使用内存申请接口（例如`acl.rt.malloc`、`acl.media.dvpp_malloc`等）申请内存后，为确保内存中不会有脏数据，建议在使用内存前先调用`acl.rt.memset`或`acl.rt.memset_async`接口先清空内存，例如acl.rt.memset\(dev\_buffer\_ptr, dev\_buffer\_size, 0, dev\_buffer\_size\)。
- Ascend RC形态下，如果应用程序中涉及`acl.rt.malloc`、`acl.media.dvpp_malloc`、`hi_mpi_dvpp_malloc`等内存申请接口，应用程序在Device上运行时，当前默认在内存不足时，应用程序可能会挂起，等待内存资源，用户可以根据实际需求选择启用操作系统提供的一些配置（例如，`enable_oom_killer`），这样在内存不足时，应用程序会自动退出，不会一直等待。

    若启用`enable_oom_killer`，您需登录Device，在“/proc/sys/vm”目录下，以root用户启用`enable_oom_killer`，命令示例如下，1表示启用，0表示禁用：

    ```python
    echo 1 > enable_oom_killer
    ```
