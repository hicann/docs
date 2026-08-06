# ChamferDistanceGrad

```c
REG_OP(ChamferDistanceGrad)
    .INPUT(xyz1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(xyz2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(idx1, TensorType({DT_INT32}))
    .INPUT(idx2, TensorType({DT_INT32}))
    .INPUT(grad_dist1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(grad_dist2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(grad_xyz1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(grad_xyz2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ChamferDistanceGrad)
```

## Brief

Applies set operation along last dimension of 6 Tensor inputs. 

## Inputs

- xyz1: A Tensor. Must be one of the following types: float16, float32. Point set with shape (B, N, 2).
- xyz2: A Tensor. Must have the same type and shape as xyz1.
- idx1: A Tensor. Must be one of the following types: int32. min indices with set one with shape (B, N).
- idx2: A Tensor. Must be one of the following types: int32. min indices with set two with shape (B, N).
- grad_dist1: A Tensor. Must have the same type as xyz1. Grad of dist1 with shape (B, N).
- grad_dist2: A Tensor. Must have the same type as xyz1. Grad of dist2 with shape (B, N).

## Outputs

- grad_xyz1: A Tensor. Must be one of the following types: float16, bfloat16, float32. grad of xyz1 with shape (B, N, 2).
- grad_xyz2: A Tensor. Must be one of the following types: float16, bfloat16, float32. grad of xyz2 with shape (B, N, 2).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 xyz1: float32
- input1 xyz2: float32
- input2 idx1: int32
- input3 idx2: int32
- input4 grad_dist1: float32
- input5 grad_dist2: float32
- output0 grad_xyz1: float32
- output1 grad_xyz2: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
