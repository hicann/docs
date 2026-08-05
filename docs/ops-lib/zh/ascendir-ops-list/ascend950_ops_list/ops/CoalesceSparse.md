# CoalesceSparse

```c
REG_OP(CoalesceSparse)
    .INPUT(unique_len, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(unique_indices, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(indices, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(values, TensorType({ DT_INT32, DT_FLOAT16, DT_FLOAT32 }))
    .OUTPUT(new_inidces, TensorType({ DT_INT32, DT_INT64 }))
    .OUTPUT(new_values, TensorType({ DT_INT32, DT_FLOAT16, DT_FLOAT32 }))
    .OP_END_FACTORY_REG(CoalesceSparse)
```

## Brief

Tutel combine function in moe.

## Inputs

- unique_len: A one-dimensional tensor of the type DT_INT32, DT_INT64.
- unique_indices:A one-dimensional tensor of the type DT_INT32, DT_INT64.
- indices: A two-dimensional tensor of the type DT_INT32, DT_INT64.
- values: A mutable Tensor of the type DT_INT32, DT_FLOAT16, DT_FLOAT32.

## Outputs

- new_inidces: A two-dimensional tensor of the type DT_INT32, DT_INT64.
- new_values: A mutable Tensor of the type DT_INT32, DT_FLOAT16, DT_FLOAT32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 unique_len: int32,int64
- input1 unique_indices: int32,int64
- input2 indices: int32,int64
- input3 values: float16,float32,int32
- output1 new_values: float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
