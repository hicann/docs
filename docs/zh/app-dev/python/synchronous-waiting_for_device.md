# 关于Device的同步等待

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，示例代码中不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

device_id = 0

# 指定Device。
ret = acl.rt.set_device(device_id)

# 创建stream。
stream, ret = acl.rt.create_stream()

# 阻塞应用程序运行，直到正在运算中的Device完成运算。
ret = acl.rt.synchronize_device()

# 资源销毁。
ret = acl.rt.synchronize_stream(stream)
ret = acl.rt.reset_device(device_id)
```
