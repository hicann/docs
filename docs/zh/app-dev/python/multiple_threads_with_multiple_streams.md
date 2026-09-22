# 多线程多Stream

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......
def run_thread():
    device_id = 0

    # 指定运算的Device
    ret = acl.rt.set_device(device_id)
    # 显式创建一个Stream
    stream, ret = acl.rt.create_stream()

    # 调用触发任务的接口。
    # ....

    # 释放资源。
    ret = acl.rt.destroy_stream(stream)


# 创建2个线程，每个线程内部创建一个Stream。
thread_id1, ret = acl.util.start_thread(run_thread, None)
thread_id2, ret = acl.util.start_thread(run_thread, None)
# 显式调用stop_thread函数确保结束线程。
ret = acl.util.stop_thread(thread_id1)
ret = acl.util.stop_thread(thread_id2)
```
