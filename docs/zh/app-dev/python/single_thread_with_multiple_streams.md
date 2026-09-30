# 单线程多Stream

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

device_id = 0
model_id_1 = 0
model_id_2 = 1

stream1, ret = acl.rt.create_stream()
# 调用触发任务的接口，例如异步模型推理，任务下发在stream1。
ret = acl.mdl.execute_async(model_id_1, dataset_in_1, dataset_out_1, stream1)

stream2, ret = acl.rt.create_stream()
# 调用触发任务的接口，例如异步模型推理， 任务下发在stream2。
ret = acl.mdl.execute_async(model_id_2, dataset_in_2, dataset_out_2, stream2)

# 流同步。
ret = acl.rt.synchronize_stream(stream1)
ret = acl.rt.synchronize_stream(stream2)

# 释放资源。
ret = acl.rt.destroy_stream(stream2)
ret = acl.rt.destroy_stream(stream1)

# ....
```
