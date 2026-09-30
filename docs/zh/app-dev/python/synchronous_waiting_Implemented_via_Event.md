# 关于Stream间任务的同步等待（通过Event实现）

多Stream之间任务的同步等待可以利用Event实现，调用`acl.rt.stream_wait_event`接口阻塞指定Stream的运行，直到指定的Event完成。需在调用`acl.rt.stream_wait_event`接口前，先调用`acl.rt.record_event`接口。

模型加载与执行的流程请参见[模型管理](model_management.md)。

算子加载与执行的流程请参见[单算子调用](single_operator_invoke.md)。

**图 1**  同步等待流程\_多Stream场景
![](figures/asynchronous_much_stream.png "同步等待流程_多Stream场景")

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......
# 创建一个Event。
event, ret = acl.rt.create_event()

# 创建两个Stream。
s1, ret = acl.rt.create_stream()
s2, ret = acl.rt.create_stream()

# 在s1末尾添加了一个event。
ret = acl.rt.record_event(event, s1)

# 阻塞s2运行，直到指定Event发生，也就是s1执行完成。
# s1完成后，唤醒s2，继续执行s2的任务。
ret = acl.rt.stream_wait_event(s2, event)

ret = acl.rt.synchronize_stream(s1)
ret = acl.rt.synchronize_stream(s2)

# 显式销毁资源。
ret = acl.rt.destroy_stream(s2)
ret = acl.rt.destroy_stream(s1)
ret = acl.rt.destroy_event(event)
# ......
```
