# BroadcastArgs

```c
REG_OP(BroadcastArgs)
    .INPUT(x1, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x2, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(BroadcastArgs)
```

## Brief

Returns the target shape for broadcasting shapes "x1" and "x2". 

## Inputs

- x1: A tensor of type int32 or int64. A shape.
- x2: A tensor of the same type as "x1". The other shape.

## Outputs

y: A tensor. The broadcasted shape. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: int32,int64
- input1 x2: int32,int64
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator BroadcastArgs.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
