# ChamferDistance

```c
REG_OP(ChamferDistance)
    .INPUT(xyz1, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .INPUT(xyz2, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(dist1, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(dist2, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(idx1, TensorType({DT_INT32}))
    .OUTPUT(idx2, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(ChamferDistance)
```

## Brief

Applies set operation along last dimension of 2 Tensor inputs. 

## Inputs

- xyz1: A Tensor. Must be one of the following types: float16, bfloat16, float32. Point set with shape (B, 2, N)
- xyz2: A Tensor. Must have the same type and shape as x1.

## Outputs

- dist1: A Tensor. Must be one of the following types: float16, bfloat16, float32. with shape (B, N)
- dist2: A Tensor. Must have the same type and shape as dist1.
- idx1: A Tensor of type int32. with shape (B, N)
- idx2: A Tensor. Must have the same type and shape as idx1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 xyz1: float16,float32
- input1 xyz2: float16,float32
- output0 dist1: float16,float32
- output1 dist2: float16,float32
- output2 idx1: int32
- output3 idx2: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
