# BandedTriangularSolve

```c
REG_OP(BandedTriangularSolve)
    .INPUT(bands, TensorType({DT_FLOAT, DT_DOUBLE, \
        DT_FLOAT16, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(rhs, TensorType({DT_FLOAT, DT_DOUBLE, \
        DT_FLOAT16, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(output,TensorType({DT_FLOAT, DT_DOUBLE, \
        DT_FLOAT16, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(lower, Bool, true)
    .ATTR(adjoint, Bool, false)
    .OP_END_FACTORY_REG(BandedTriangularSolve)
```

## Brief

Solution of banded triangular matrix. 

## Inputs

The input bands has to be symmetric and positive definite.
- bands:A Tensor. Must be one of the following types: double, float32,
float16,complex64, complex128. Shape is  [... K,M], K corresponds to the
number of bands (actually stored diagonals), and M is the data of the
diagonals.
- rhs:shape is [...M] or [...M, N]. Has the same type as bands.

## Outputs

- output:A Tensor. Has the same type as bands.

## Attributes

- lower:An optional bool. Defaults to True.True: indicates the lower
triangular matrix. False: indicates the upper triangular matrix.
- adjoint:An optional bool. Defaults to False.Boolean indicating whether to
solve with matrix or its (block-wise) adjoint. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 bands: complex64,complex128,double,float16,float32
- input1 rhs: complex64,complex128,double,float16,float32
- output0 output: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with tensorflow BandedTriangularSolve operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
