# 单线程单Stream

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......
ACL_MEMCPY_HOST_TO_DEVICE = 1

# 显式创建一个Stream。
stream, ret = acl.rt.create_stream()

# 调用触发任务的接口，传入stream参数。
ret = acl.rt.memcpy_async(dev_ptr, dev_size, host_ptr, host_size, ACL_MEMCPY_HOST_TO_DEVICE, stream)
# 调用acl.rt.synchronize_stream接口，阻塞应用程序运行，直到指定Stream中的所有任务都完成。
ret = acl.rt.synchronize_stream(stream)

# Stream使用结束后，显式销毁Stream。
ret = acl.rt.destroy_stream(stream)
# ......
```
