# Cholesky

```c
REG_OP(Cholesky)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, \
        DT_FLOAT16, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, \
        DT_FLOAT16, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Cholesky)
```

## Brief

Computes the Cholesky decomposition of one or more square matrices . 

## Inputs

The input x has to be symmetric and positive definite.Inputs include:
x:A Tensor. Must be one of the following types: double, float32, float16,
complex64, complex128. Shape is [..., M, M] . 

## Outputs

y:A Tensor. Has the same type as x . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Attention Constraints

The input x is a tensor of shape [..., M, M] whose inner-most 2 dimensions
form square matrices.

## Third-party framework compatibility

Compatible with tensorflow Cholesky operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
