# ThreeInterpolateBackward

```c
REG_OP(ThreeInterpolateBackward)
    .INPUT(grad_x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(idx, TensorType({DT_INT32, DT_INT64}))
    .INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(grad_y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(m, Int)
    .OP_END_FACTORY_REG(ThreeInterpolateBackward)
```

## Brief

three interpolate backward.

## Inputs

three input:
grad_x: The set of features points with dtype of float32 and float16 with shape [b,c,n]
idx: The set of index with dtype of int32 and int64 with shape [b,n,3]
weight : The set of weight points with dtype of float32 and float16 with shape[b,n,3]
m: The dims m of output with dtype int

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_x: float16,float32
- input1 idx: int32,int64
- input2 weight: float16,float32
- output0 grad_y: float16,float32

## y

grad_y: A Tensor, the interpolate backward output with dtype of float32 and float16 with shape[b,c,m]


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
