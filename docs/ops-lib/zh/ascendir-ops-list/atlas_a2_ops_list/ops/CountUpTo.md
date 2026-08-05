# CountUpTo

```c
REG_OP(CountUpTo)
    .INPUT(ref, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(limit, Int, 0)
    .OP_END_FACTORY_REG(CountUpTo)
```

## Brief

Increments 'ref' until it reaches 'limit' . 

## Inputs

Inputs include:
ref: A mutable Tensor. Must be one of the following types: int32, int64 . 

## Outputs

y: A Tensor. Has the same type as ref . 

## Attributes

limit: An int. If incrementing ref would bring it above limit, instead
generates an 'OutOfRange' error . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 ref: int32,int64
- output0 y: int32,int64

## Attention Constraints

The implementation for CountUpTo on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

compatible with tensorflow CountUpTo operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
