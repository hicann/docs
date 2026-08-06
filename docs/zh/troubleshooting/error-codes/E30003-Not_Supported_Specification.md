# E30003 Not\_Supported\_Specification

## 错误信息

```text
The number of started user processes on the device exceeds the limit.
```

## 可能原因

调度队列中拉起的进程数超过产品使用约束，具体约束参考[Link](https://hiascend.com/document/redirect/CannCommercialCppAppendix)中“关于进程”描述。

## 解决方法

在上次训练任务退出10秒后进行重试。
