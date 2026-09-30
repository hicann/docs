# 关于Event的同步等待

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......
# 创建一个Event。
event, ret = acl.rt.create_event()

# 创建一个Stream。
stream, ret = acl.rt.create_stream()

# stream末尾添加了一个event。
ret = acl.rt.record_event(event, stream)

# 阻塞应用程序运行，等待event发生，也就是stream执行完成。
# stream完成后产生event，唤醒执行应用程序的控制流，开始执行程序。
ret = acl.rt.synchronize_event(event)

# 显式销毁资源。
ret = acl.rt.destroy_stream(stream)
ret = acl.rt.destroy_event(event)
# ......
```
