# ForeachMulScalarInplace

```c
REG_OP(ForeachMulScalarInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(scalar, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachMulScalarInplace)
```

## Brief

multiply scalar foreach element in each tensor in tesnorlist, this is an in-place operation.

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors, can be float16, float, and int32.
- scalar: A scalar to be multiplied, the data type must be the same as tensors.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- input1 scalar: float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
