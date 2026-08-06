# MatrixTriangularSolve

```c
REG_OP(MatrixTriangularSolve)
    .INPUT(matrix, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(rhs, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(lower, Bool, true)
    .ATTR(adjoint, Bool, false)
    .OP_END_FACTORY_REG(MatrixTriangularSolve)
```

## Brief

Solves systems of linear equations with upper or lower triangular
matrices by backsubstitution . 

## Inputs

The input rhs must have the same type as matrix. Inputs include:
- matrix: A Tensor. Shape is [..., M, M].
- rhs:A Tensor. Must have the same type as matrix. Shape is [..., M, K] .

## Outputs

y:A Tensor. Has the same type as matrix . 

## Attributes

- lower: An optional bool. Defaults to True. Boolean indicating whether
the innermost matrices in matrix are lower or upper triangular.
- adjoint: An optional bool. Defaults to False. Boolean indicating whether to solve
with matrix or its (block-wise) adjoint . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 matrix: double,float32
- input1 rhs: double,float32
- output0 y: double,float32

## Attention Constraints

The input matrix is a tensor of shape [..., M, M] whose inner-most 2
dimensions form square matrices.  

## Third-party framework compatibility

Compatible with tensorflow MatrixTriangularSolve operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
