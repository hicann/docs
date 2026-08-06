# E30008 Execution\_Error\_AICPU\_Operator\_Timeout

## 错误信息

报错格式如下，占位符%s表示扩展信息：

```text
AI CPU operator execution timed out. %s
```

报错示例如下：

```text
AI CPU operator execution timed out. The AI CPU operator RunAicpuRpcSrvLaunchV2_receive that times out is on device 0 stream 181. The task ID is 543, the so name is libccl_kernel.so, and the entry function for executing this AI CPU operator is RunAicpuRpcSrvLaunchV2.
```

## 可能原因

1. 对于GetNext算子，其预处理时间可能过长。
2. 对于自定义算子，实现逻辑中有超大循环，或者输入输出Shape过大。
3. 内置算子输入输出Shape过大。

## 解决方法

1. 针对GetNext算子，检查其预处理流程或通过aclrtSetOpExecuteTimeOut接口调整超时时间。
2. 对于自定义算子，确保其逻辑设计合理或者尝试修改Shape。
3. 针对输入输出Shape过大，可尝试修改shape或通过aclrtSetOpExecuteTimeOut接口调整超时时间。
