# Execution Timeout Error of the AI CPU Operator

## Symptom

Any of the timeout errors is reported during operator execution.

- **Symptom 1**

    1. Error code  **E39999**  is reported during Runtime execution. Runtime error message "PrintAicpuErrorInfo", along with "ErrCode=507018, desc=\[aicpu exception\]", is printed in the plog file on the host.
    2. In addition, the device log of the AI CPU contains error message "HandleTaskTimeout".

    This symptom is the same as the error message in  [Possible Cause \> Example 3](ai_cpu_kernel_execution_error.md)  in  [Kernel Execution Error of the AI CPU Operator](ai_cpu_kernel_execution_error.md).

- **Symptom 2**

    An error is reported during Runtime execution. Runtime error message "PrintAicpuErrorInfo", along with "ErrCode=507017, desc=\[aicpu timeout\]", is printed in the application log.

    In  Ascend EP  form, the application run logs,  **plog-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/plog**  by default.

    In  Ascend RC  form, the application run logs,  **device-app-_pid_\__\*_.log**, are stored in  **_$HOME_/ascend/log/\[run|debug\]/device-app-_pid_**  by default.

    ```text
    [ERROR] RUNTIME(16243,msame):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:661]16243 rtStreamSynchronize:[EXEC][DEFAULT]ErrCode=507017, desc=[aicpu timeout], InnerCode=0x715002a
    ```

## Possible Cause

- The operator input/output shape is too large, resulting in slow operator execution.
- The hardware performance is insufficient to support complex computation of a large number of operators

## Solution

Call the  **aclrtSetOpExecuteTimeOut**  API to increase the operator execution timeout interval.

The API prototype is defined as follows:

```c
aclError aclrtSetOpExecuteTimeOut(uint32_t timeout)      // timeout, in seconds.
```

After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the fault persists.
