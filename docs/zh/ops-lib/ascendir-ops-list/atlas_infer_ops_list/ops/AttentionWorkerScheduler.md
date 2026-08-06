# AttentionWorkerScheduler

```c
REG_OP(AttentionWorkerScheduler)
    .INPUT(schedule_context, TensorType({DT_INT8}))
    .OUTPUT(schedule_context, TensorType({DT_INT8}))
    .OP_END_FACTORY_REG(AttentionWorkerScheduler)
```

## Brief

Data Scanning Operator for the Attention Side in Decoupled Attention-FFN Deployment Scenarios. This operator
polls data from FFNToAttention to confirm its readiness state.

## Inputs

- schedule_context: A tensor. The type support int8. Its shape must be 1D (1024). Format: ND

## Outputs

schedule_context: A ND Tensor that holds the new value of schedule_context after the value has been assigned.
Has the same shape and dtype and format as the input "schedule_context". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 schedule_context: int8
- output0 schedule_context: int8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
