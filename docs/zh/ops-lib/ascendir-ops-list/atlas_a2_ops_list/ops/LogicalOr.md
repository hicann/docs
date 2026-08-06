# LogicalOr

```c
REG_OP(LogicalOr)
    .INPUT(x1, TensorType({DT_BOOL}))
    .INPUT(x2, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(LogicalOr)
```

## Brief

Returns the truth value of x1 OR x2 element-wise. Support broadcasting operations.

## Inputs

- x1: A ND tensor of type bool.
- x2: A ND tensor of the same dtype as "x1".

## Outputs

y: A tensor of the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bool
- input1 x2: bool
- output0 y: bool
### AI CPU
- input0 x1: bool
- input1 x2: bool
- output0 y: bool

## Attention Constraints

LogicalOr supports broadcasting.

## Third-party framework compatibility

Compatible with the TensorFlow operator LogicalOr.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
