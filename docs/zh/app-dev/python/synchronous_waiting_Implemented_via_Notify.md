# 关于Stream间任务的同步等待（通过Notify实现）

多Stream之间任务的同步等待可以利用Notify实现，例如，若stream2的任务依赖stream1的任务，想保证stream1中的任务先完成，这时可创建一个Notify，调用`acl.rt.record_notify`接口将Notify插入到stream1中（通常称为Record Notify任务），调用`acl.rt.wait_and_reset_notify`接口在stream2中插入一个等待Notify完成的任务（通常称为Wait Notify任务）。

**图 1**  同步等待流程\_多Stream场景
![](figures/asynchronous_much_stream_1.png "同步等待流程_多Stream场景-1")

上图中的模型加载与执行的流程请参见[模型管理](model_management.md)，算子加载与执行的流程请参见[单算子调用](single_operator_invoke.md)。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝编译运行，仅供参考。

```python
import acl
# ......
# 创建一个notify
notify, ret = acl.rt.create_notify(0)

# 创建stream_1、stream_2
stream_1, ret = acl.rt.create_stream()
stream_2, ret = acl.rt.create_stream()

# 在stream_1末尾添加了一个notify
ret = acl.rt.record_notify(notify, stream_1)

# 阻塞stream_2运行，直到指定notify发生，也就是stream_1执行完成
# stream_1完成后，唤醒stream_2，继续执行stream_2的任务
ret = acl.rt.wait_and_reset_notify(notify, stream_2, 0)

ret = acl.rt.synchronize_stream(stream_1)
ret = acl.rt.synchronize_stream(stream_2)

# 显式销毁资源
ret = acl.rt.destroy_stream(stream_2)
ret = acl.rt.destroy_stream(stream_1)
ret = acl.rt.destroy_notify(notify)
# ......
```
