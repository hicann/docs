# AI CPU算子执行超时报错

## 问题现象

算子执行过程中，如果遇到下面任意一种报错，均属于算子执行超时报错。

- **现象1**

    1. 当Runtime执行报错E39999，Host侧plog日志中Runtime打印了PrintAicpuErrorInfo错误信息，且提示“**ErrCode=507018, desc=\[aicpu exception\]**”.
    2. 进一步查看AI CPU的Device日志发现提示**HandleTaskTimeout**错误信息。

    该现象与[AI CPU算子Kernel执行报错](ai_cpu_kernel_execution_error.md)中“[可能原因 \> 样例3](ai_cpu_kernel_execution_error.md)”日志报错信息一样。

- **现象2**

    当Runtime执行报错，在应用程序日志中Runtime打印了PrintAicpuErrorInfo的错误信息，且提示“**ErrCode=507017, desc=\[aicpu timeout\]**”。

    Ascend EP形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/plog路径下，日志文件为plog-_pid\_\*_.log。

    Ascend RC形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/device-app-_pid_路径下，日志文件为device-app-_pid_\_\*.log。

    ```bash
    [ERROR] RUNTIME(16243,msame):2022-09-22-11:27:01.794.510 [api_c.cc:661]16243 rtStreamSynchronize:[EXEC][DEFAULT]ErrCode=507017, desc=[aicpu timeout], InnerCode=0x715002a
    ```

## 可能原因

- 算子的输入/输出Shape太大导致算子执行缓慢。
- 硬件性能不足导致无法支持大量复杂算子的计算。

## 解决方法

该类型的错误，可尝试使用**aclrtSetOpExecuteTimeOut**接口，适当调大算子执行的超时时间。

接口原型定义如下:

```c
aclError aclrtSetOpExecuteTimeOut(uint32_t timeout)      // timeout单位为秒
```

若仍无法解决，  您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
