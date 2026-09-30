# 编程模型

## 主机、设备编程模式

**主机（或称Host）**：指X86服务器CPU、ARM服务器CPU，通过总线与一个或多个设备互联，利用设备提供的NN（Neural-Network）等计算能力完成业务。

**设备（或称Device、NPU**）：指安装了AI处理器的硬件，通过总线（例如PCIe、HCCS等）与主机相连，提供NN等计算能力。HCCS是Huawei Cache Coherence System，表示华为缓存一致性系统。

主机与设备的关系如下图所示：

![](figures/logic_structure_image.png)

总结如下：

1. **主机和设备各自拥有独立的内存空间**Runtime提供了主机侧和设备侧的内存申请接口，以及主机与设备之间的内存复制接口。在编程时，需要区分主机和设备的内存申请，并显式调用内存复制接口，将数据从主机侧复制到设备侧，以使设备硬件加速器在访问本地内存时达到最佳性能。
2. **主机与设备之间采用异步并行的执行方式。**

    主机将任务（或称Task）下发到设备后，**不会等待设备任务执行完成**就立即返回；设备随即开始调度并执行下发的任务；主机侧的CPU可以与设备侧的加速器并行工作。异步任务下发的接口通常会带有Stream参数，表示将任务下发到对应的Stream中执行。

    当主机需要获取设备的计算结果时，必须发起显式的同步API调用，同步API会阻塞主机CPU，直到设备侧任务执行完成才返回。

    通过这种异步并行执行机制，可以有效隐藏主机处理时间或主机与设备间的数据传输延迟，提高吞吐量，缩短端到端的执行时间。

3. **异步任务下发到Stream中任务的执行方式**

    Stream中的任务保序执行，Stream间的任务并行执行。例如下图中主机侧顺序启动Kernel1、Kernel2和Kernel3任务，具体执行顺序如下：

    - Kernel1和Kernel3位于同一个Stream中，因此Kernel3需要等待Kernel1执行完毕才能开始执行。
    - Kernel2与Kernel1、Kernel3不在同一个Stream中，因此Kernel2可以与Kernel1、Kernel3并行执行。

    ![](figures/relationship_among_Device-Context-Stream_0.png)

## Runtime主要编程概念

- **Host**，是Runtime对主机的抽象。
- **Device**，是对AI处理器所属设备的抽象，通常Host与Device关系为1：N。用户APP可以调用acl接口，例如aclrtSetDevice，指定当前用于运算的硬件设备。
- **Context**，是Device的逻辑运行环境，Context与Device的关系为N：1，即每个Context必定隶属于一个唯一的Device。Context负责管理运行资源对象（包括Stream、Event和Notify，但不包括内存）的生命周期；不同Context中的对象是完全隔离的，例如，不同Context的Stream和Event是完全隔离的，无法建立同步等待关系；运行出错同样按Context隔离。
- **Stream**，是Device提供的逻辑任务执行队列，可以异步地向Stream中添加任务，在同一个Stream中的任务会严格按FIFO方式执行。Stream与Context的关系是N：1，某条Stream一定属于唯一的Context。
- **Task**，可被添加到Stream中的执行任务，可以分计算类任务、内存拷贝、事件同步类任务。Task与Stream的关系是N：1，某个Task会被加入到唯一的Stream。

Device、Context、Stream之间的关系如下图所示：

![](figures/relationship_among_Device-Context-Stream.png)

## 线程关联Context

Runtime的大多数API接口没有device id参数，因为这些API接口所作用的Device是从调用线程关联的Context中获取的。因此，当主机线程调用Runtime API时，要遵循如下要求：

- 线程（主机侧的CPU线程）要关联Context后，才能正确调用Runtime API。
- 线程同一时刻只能关联一个Context。
- 应用程序可以显式创建Context来达成运行资源隔离的业务诉求。此场景中，同一进程内Context可被所有线程可见，线程可以通过aclrtGetCurrentContext，aclrtSetCurrentContext进行切换Context。

以下示例说明了线程在调用Context相关接口时，线程与Context之间的关联和切换过程，仅供参考，不可以直接拷贝运行。

```Python
# 初始时，线程未关联任何Context
acl.init()
acl.rt.set_device(0)  # acl.rt.set_device会创建默认Context，同时将线程关联默认Context
# 线程关联的Context: 默认context

ctx1, _ = acl.rt.create_context(0)  # Device 0显式创建ctx1, 会将线程关联ctx1
# 线程关联的Context: ctx1
current_ctx, _ = acl.rt.get_context()  # 获取当前线程关联的Context, 此时返回的current_ctx==ctx1
# 线程关联的Context: ctx1

ctx2, _ = acl.rt.create_context(0)  # Device 0又显式创建ctx2, 会将线程关联ctx2
# 线程关联的Context: ctx2

acl.rt.set_context(current_ctx)  # 切换Context，由于current_ctx=ctx1，线程关联ctx1
# 线程关联的context: ctx1

acl.rt.set_context(current_ctx)  # 切换Context
# 线程关联的context: ctx2
.....

acl.rt.destroy_context(ctx2)  # 当前线程正关联ctx2，销毁ctx2时会同时将线程也ctx2去关联
# 线程关联的context: NA

# ctx2已销毁，应该切换到其他ctx(如ctx1)
acl.rt.set_context(ctx1)
# 线程关联的context: ctx1
.....

acl.rt.destroy_context(ctx1)  # 当前线程正关联ctx1，销毁ctx1时会同时将线程也ctx1去关联
# 线程关联的context: NA
acl.rt.reset_device_force(0)
acl.finalize()
```

## 默认Context和默认Stream的使用场景

- Device上执行操作下发前，必须有Context和Stream，这个Context、Stream可以显式创建，也可以隐式创建。**隐式创建**的Context、Stream就是默认Context、默认Stream。

    默认Stream作为接口入参时，直接传0。

- **默认Context**不允许用户执行`acl.rt.get_context`或`acl.rt.set_context`操作，也不允许执行`acl.rt.destroy_context`操作。
- **默认Context**、**默认Stream**一般适用于简单应用，用户仅需要一个Device的计算场景。多线程应用程序建议全部使用显式创建的Context和Stream。

示例代码如下，仅供参考，不可以直接拷贝运行：

```python
# …
ret = acl.init(config_path)
ret = acl.rt.set_device(device_id)

# 已经创建了一个default ctx，在default ctx中创建了一个default stream，并且在当前线程可用。
# …
ret = acl.op.execute_v2(op1, input_desc, inputs, output_desc, outputs, attr, 0)  # 最后一个0表示在default stream上执行算子op1。
ret = acl.op.execute_v2(op2, input_desc, inputs, output_desc, outputs, attr, 0)  # 最后一个0表示在default stream上执行算子op2。
ret = acl.rt.synchronize_stream(0)

# 等待计算任务全部完成（op1、op2执行结束），用户根据需要获取计算任务的输出结果。
# …
ret = acl.rt.reset_device(device_id)  # 释放计算设备0，对应的default ctx及default stream生命周期也终止。
```
