# Gcd

```c
REG_OP(Gcd)
    .INPUT(x1, "T")
    .INPUT(x2, "T")
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_UINT8, DT_INT8, DT_INT16, DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(Gcd)
```

## Brief

Returns x1 and x2 greatest common divisor element-wise. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types: uint8, int8, int32, int16, int64.
- x2: A ND Tensor of the same dtype as "x1".

## Outputs

y: A ND Tensor. Has the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int32
- input1 x2: int32
- output0 y: int32

## Third-party framework compatibility

Compatible with the PyTorch operator gcd.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
