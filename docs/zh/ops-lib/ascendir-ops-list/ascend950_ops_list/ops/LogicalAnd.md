# LogicalAnd

```c
REG_OP(LogicalAnd)
    .INPUT(x1, TensorType({DT_BOOL}))
    .INPUT(x2, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(LogicalAnd)
```

## Brief

Returns the truth value of x1 AND x2 element-wise. Support broadcasting operations.

## Inputs

- x1: A tensor of type bool.
- x2: A tensor of the same dtype as "x1".

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

LogicalAnd supports broadcasting.

## Third-party framework compatibility

Compatible with the TensorFlow operator LogicalAnd.


---

[Back to Operator Specifications (Ascend950)](../README.md)
