# MatrixSolveLs

```c
REG_OP(MatrixSolveLs)
    .INPUT(matrix, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(rhs, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(l2, TensorType({DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE}))
    .ATTR(fast, Bool, true)
    .OP_END_FACTORY_REG(MatrixSolveLs)
```

## Brief

Solves systems of linear equations . 

## Inputs

The input rhs must have the same type as matrix. Inputs include:
- matrix:A Tensor. Shape is [..., M, M].
- rhs:A Tensor. Must have the same type as matrix. Shape is [..., M, K].
- l2:0-D double Tensor. Ignored if fast=False .

## Outputs

y:Tensor of shape [..., N, K] whose inner-most 2 dimensions form M-by-K
matrices that solve the equations matrix[..., :, :] * output[..., :, :] =
rhs[..., :, :] in the least squares sense . 

## Attributes

fast:bool. Defaults to True . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 matrix: complex64,complex128,double,float32
- input1 rhs: complex64,complex128,double,float32
- input2 l2: double
- output0 y: complex64,complex128,double,float32

## Attention Constraints

The input matrix matrix is a tensor of shape [..., M, M] whose inner-most 2
dimensions form square matrices.  

## Third-party framework compatibility

Compatible with tensorflow MatrixSolveLs operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
