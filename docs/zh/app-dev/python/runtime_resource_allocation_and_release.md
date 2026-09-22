# 运行时资源申请与释放

开发应用时，应用程序中必须包含运行时资源申请的代码逻辑，关于运行时资源申请的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的资源申请、释放流程说明。

## 基本原理

您需要按顺序**依次申请**如下运行时资源：Device、Stream，确保可以使用这些资源执行运算、管理任务。所有数据处理都结束后，需要按顺序依次**释放**Stream、Device等运行时资源。

其中，创建Stream的方式分为隐式创建和显式创建，其适用场景有所不同：

- **隐式创建**Stream：适合简单、无复杂交互逻辑的应用，但缺点在于，在多线程编程中，每个线程都使用默认Stream，默认Stream中任务的执行顺序取决于操作系统线程调度的顺序。
- **显式创建**Stream：适合大型、复杂交互逻辑的应用，且便于提高程序的可读性、可维护性。

关于单进程、单线程、单Stream场景如下所示：

- 单进程：一个应用程序对应一个进程。
- 单线程：不创建多个线程时，默认只有一个线程。
- 单Stream：整个开发的过程中使用同一个Stream。

    对于同一个Stream中的异步任务，会按照应用程序中任务的顺序执行任务，确保异步任务执行的顺序。

- 关于多线程、多Stream的场景请参见[Stream管理](stream_management.md)。

## 运行时资源申请流程

**图 1**  运行时资源申请流程
![](figures/runtime_resource_apply_process.png "运行时资源申请流程")

关键接口的说明如下：

**申请运行时资源**时，需按顺序依次申请：Device、Stream。

1. 调用`acl.rt.set_device`接口**指定用于运算的Device**，同时该接口也会隐式创建默认Context、默认Stream。但需遵循以下约束：
    - 一个Device对应一个默认Context，默认Context无需显式调用接口释放，会在调用`acl.rt.destroy_context`接口释放资源时一并释放。
    - 一个Device对应一个默认Stream，默认Stream无需显式调用接口释放，会在调用`acl.rt.destroy_stream`接口释放资源时一并释放。
    - 默认Context、默认Stream，是在调用`acl.rt.reset_device`接口后自动释放。

2. 若使用默认Stream作为接口入参时，直接传0，若不使用默认Stream，可调用`acl.rt.create_stream`接口显式创建Stream。
3. （可选）调用`acl.rt.get_run_mode`接口获取软件栈的运行模式，根据运行模式来判断后续的内存申请接口调用逻辑。
    <!-- npu="910b,910,310p,310b" id1 -->
    如果查询结果为ACL\_HOST，则数据传输时涉及申请Host上的内存。
    <!-- end id1 -->
    如果查询结果为ACL\_DEVICE，则数据传输时仅需申请Device上的内存。

## 运行时资源释放流程

**图 2**  运行时资源释放流程
![](figures/runtime_resource_release_process.png "运行时资源释放流程")

关键接口的说明如下：

释放运行时资源时，需按顺序依次释放：Stream、Device。

1. 若调用`acl.rt.create_stream`接口显式创建Stream，需调用`acl.rt.destroy_stream`接口释放Stream；否则，无需调用acl.rt.destroy\_stream接口。
2. 调用`acl.rt.reset_device`接口释放Device上的资源，同时该接口也会隐式释放默认Context、默认Stream，无需额外单独释放默认Context、默认Stream。

## 示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
#......

# ======运行时资源申请======
# 1.指定运算的Device。
ret = acl.rt.set_device(device_id)


# 2.显式创建一个Stream。
#用于维护一些异步操作的执行顺序，确保按照应用程序中的代码调用顺序执行任务。
stream, ret = acl.rt.create_stream()
# ======运行时资源申请======

#......

# ======运行时资源释放======
ret = acl.rt.destroy_stream(stream)
ret = acl.rt.reset_device(device_id)
# ======运行时资源释放======

#......
```
