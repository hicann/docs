# 使用约束

## 关于低功耗

进入系统休眠前，需要确保不下发AI推理、媒体数据处理等相关业务，或者退出业务进程。等待系统唤醒成功后，再继续下发业务或重启业务进程。

## 关于进程

- 不支持使用fork函数以及封装了fork的函数（如system、posix_spawnp等）创建多个子进程，且在进程中调用acl接口的场景，否则进程运行时会报错或者卡死。
<!-- npu="910" id7 -->
- 对于Atlas 训练系列产品，物理机场景下，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数*64个进程；虚拟机场景下，一个Device上最多只能支持32个用户进程，Host最多只能支持Device个数*32个进程。
<!-- end id7 -->
<!-- npu="310p" id6 -->
- 对于Atlas 推理系列产品，物理机场景下，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数*64个进程；虚拟机场景下，一个Device上最多只能支持32个用户进程，Host最多只能支持Device个数*32个进程。
<!-- end id6 -->
<!-- npu="310b" id5 -->
- 对于Atlas 200I/500 A2 推理产品，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数*64个进程。
<!-- end id5 -->
<!-- npu="910b" id4 -->
- 对于Atlas A2 训练系列产品/Atlas A2 推理系列产品，一个Device上最多只能支持63个用户进程，Host最多只能支持Device个数*63个进程。
<!-- end id4 -->
<!-- npu="A3" id3 -->
- 对于Atlas A3 训练系列产品/Atlas A3 推理系列产品，一个Device上最多只能支持63个用户进程，Host最多只能支持Device个数*63个进程。
<!-- end id3 -->
<!-- npu="950" id2 -->
- 对于Ascend 950PR/Ascend 950DT，一个Device上最多只能支持64个用户进程，Host最多只能支持Device个数*64个进程。
<!-- end id2 -->

## 关于创建类和销毁类接口

- 对于创建类接口（例如：aclrtCreateStream、aclrtCreateEvent、aclCreateDataBuffer等），用户调用该类接口创建对应的资源后，资源使用完成后，建议及时调用对应的销毁类接口（例如：aclrtDestroyStream、aclrtDestroyEvent、aclDestroyDataBuffer等），否则，程序可能会异常。
- 对于销毁类接口（例如：aclrtDestroyStream、aclrtDestroyEvent、aclrtFree、aclDestroyDataBuffer等），用户调用该类接口后，不能继续使用已释放或销毁的资源，建议用户调用销毁类接口后，将相关资源设置为无效值（例如，置为NULL）。

## 关于内存

<!-- npu="310p" id8 -->
- 在Atlas 推理系列产品上开发业务应用时，需避免多个操作向同一个内存地址写数据，否则可能导致硬件异常。
<!-- end id8 -->
- 不支持在aclrtMemcpyAsync、aclrtMemsetAsync接口等异步操作内存过程中使用fork以及封装了fork的函数，如system、posix_spawnp等，否则会导致进程运行时报错，甚至卡死等不可预期的错误。
- 使用内存申请接口（例如aclrtMalloc）申请内存后，为确保内存中不会有脏数据，建议在使用内存前先调用aclrtMemset或aclrtMemsetAsync接口先清空内存，例如aclrtMemset(devBufferPtr, devBufferSize, 0, devBufferSize)。
  <!-- npu="310p" id9 -->
- Ascend RC形态下，如果应用程序中涉及aclrtMalloc、acldvppMalloc、hi_mpi_dvpp_malloc等内存申请接口，应用程序在Device上运行时，当前默认在内存不足时，应用程序可能会挂起，等待内存资源，用户可以根据实际需求选择启用操作系统提供的一些配置（例如，enable_oom_killer），这样在内存不足时，应用程序会自动退出，不会一直等待。若启用enable_oom_killer，您需登录Device，在“/proc/sys/vm”目录下，以root用户启用enable_oom_killer，命令示例如下，1表示启用，0表示禁用：

  ```bash
  echo 1 > enable_oom_killer
  ```
  <!-- end id9 -->

<!-- npu="950,A3,910b,910,310p,310b" id1 -->
## 旧版本AI处理器->新版本AI处理器的应用迁移

需在迁移后的AI处理器版本上重新转换模型、编译应用程序，否则可能存在应用执行异常的情况。
<!-- end id1 -->
