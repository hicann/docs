# BroadcastGradientArgs

```c
REG_OP(BroadcastGradientArgs)
    .INPUT(x1, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x2, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y1, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y2, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(BroadcastGradientArgs)
```

## Brief

Returns the reduction indices for computing gradients of "x1" and "x2" with broadcast.

## Inputs

- x1: A tensor. The type support int32 and int64. Its shape must be 1D. Format: ND.
- x2: A tensor. Its type is consistent with x1. Its shape must be 1D. Format: ND.

## Outputs

- y1: A tensor. Reduction indices of x1. Its type is consistent with x1. Its shape must be 1D. Format: ND.
- y2: A tensor. Reduction indices of x2. Its type is consistent with x1. Its shape must be 1D. Format: ND.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: int32,int64
- input1 x2: int32,int64
- output0 y1: int32,int64
- output1 y2: int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator BroadcastGradientArgs.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
