# E30008 Execution\_Error\_AICPU\_Operator\_Timeout

## Symptom

The following is error format. The placeholder %s indicates the extended information.

```text
AI CPU operator execution timed out. %s
```

Error example:

```text
AI CPU operator execution timed out. The AI CPU operator RunAicpuRpcSrvLaunchV2_receive that times out is on device 0 stream 181. The task ID is 543, the so name is libccl_kernel.so, and the entry function for executing this AI CPU operator is RunAicpuRpcSrvLaunchV2.
```

## Possible Cause

1. For a GetNext operator, its preprocessing time may be too long.
2. For a custom operator, it contains an ultra-large loop in the implementation logic or its input and output shapes are too large.
3. The input and output shapes of a built-in operator are too large.

## Solution

1. For a GetNext operator, check its preprocessing or use the aclrtSetOpExecuteTimeOut interface to adjust the timeout.
2. For a custom operator, ensure that the logic design is proper or modify the shape.
3. If the input and output shapes are too large, modify the shape or use the aclrtSetOpExecuteTimeOut interface to adjust the timeout.
