# MatrixSolve

```c
REG_OP(MatrixSolve)
    .INPUT(matrix, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(rhs, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(adjoint, Bool, false)
    .OP_END_FACTORY_REG(MatrixSolve)
```

## Brief

Solves systems of linear equations . 

## Inputs

The input rhs must have the same type as matrix. Inputs include:
- matrix:A Tensor of input. Shape is [..., M, M].
- rhs:A Tensor. Must have the same type as matrix. Shape is [..., M, K] .

## Outputs

y:A Tensor. Has the same type as matrix . 

## Attributes

adjoint:An optional bool. Defaults to False.Boolean indicating whether to
solve with matrix or its (block-wise) adjoint . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 matrix: complex64,complex128,double,float32
- input1 rhs: complex64,complex128,double,float32
- output0 y: complex64,complex128,double,float32

## Attention Constraints

The input matrix is a tensor of shape [..., M, M] whose inner-most 2
dimensions form square matrices.  

## Third-party framework compatibility

Compatible with tensorflow MatrixSolve operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
