# ThreeInterpolate

```c
REG_OP(ThreeInterpolate)
    .INPUT(features, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(idx, TensorType({DT_INT32, DT_INT64}))
    .INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ThreeInterpolate)
```

## Brief

three interpolate.

## Inputs

Two input:
features: The set of features points
idx: The set of index
weight : The set of weight points

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 features: float16,float32
- input1 idx: int32,int64
- input2 weight: float16,float32

## y

y: A Tensor, the interpolate point


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
