# MatrixDeterminant

```c
REG_OP(MatrixDeterminant)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(MatrixDeterminant)
```

## Brief

Computes the determinant of one or more square matrices . 

## Inputs

The input x is a tensor of shape [N, M, M] whose inner-most 2 dimensions
form square matrices. Inputs include:
x:A Tensor. Must be one of the following types: double, float32, complex64,
complex128. Shape is [..., M, M] . 

## Outputs

y:A Tensor. Has the same type as x . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float32
- output0 y: complex64,complex128,double,float32

## Attention Constraints

The input x is a tensor of shape [..., M, M] whose inner-most 2 dimensions
form square matrices.

## Third-party framework compatibility

Compatible with tensorflow MatrixDeterminant operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
