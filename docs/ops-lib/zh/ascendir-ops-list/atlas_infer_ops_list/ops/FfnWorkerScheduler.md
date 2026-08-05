# FfnWorkerScheduler

```c
REG_OP(FfnWorkerScheduler)
    .INPUT(schedule_context, TensorType({DT_INT8}))
    .OUTPUT(schedule_context, TensorType({DT_INT8}))
    .ATTR(sync_group_size, Int, 1)
    .ATTR(execute_mode, Int, 0) // 1: loop, 0: once
    .OP_END_FACTORY_REG(FfnWorkerScheduler)
```

## Brief

Data Scanning Operator for the FFN Side in Decoupled Attention-FFN Deployment Scenarios，This operator polls data from AttentionToFFN to confirm its readiness state.

## Inputs

- schedule_context: A tensor. The type support int8. Its shape must be 1D (1024). Format: ND

## Outputs

schedule_context: A ND Tensor that holds the new value of schedule_context after the value has been assigned.
Has the same shape and dtype and format as the input "schedule_context". 

## Attributes

- sync_group_size: Sessions handled per group, with a default value of 1. The type support int32.
- execute_mode: Kernel execution mode. Currently only supports value 0. The type support int32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 schedule_context: int8
- output0 schedule_context: int8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
