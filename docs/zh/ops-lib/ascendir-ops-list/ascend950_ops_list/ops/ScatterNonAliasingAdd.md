# ScatterNonAliasingAdd

```c
REG_OP(ScatterNonAliasingAdd)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ScatterNonAliasingAdd)
```

## Brief

Scatter non-aliasing add: copy x to y, then scatter-add updates into y at positions specified by indices.

## Inputs

Three inputs, including:
- x: A ND Tensor. Must be one of the following types: float32, float16, int32.
- indices: A ND Tensor. Must be one of the following types: int32, int64.
- updates: A ND Tensor. Must be one of the following types: float32, float16, int32.

## Outputs

y: A ND Tensor. Must be one of the following types: float32, float16, int32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- input1 indices: int32,int64
- input2 updates: float16,float32,int32
- output0 y: float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
