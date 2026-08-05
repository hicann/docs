# TridiagonalSolve

```c
REG_OP(TridiagonalSolve)
    .INPUT(diagonals, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(rhs, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(partial_pivoting, Bool, true)
    .OP_END_FACTORY_REG(TridiagonalSolve)
```

## Brief

Solves tridiagonal systems of equations. 

## Inputs

- diagonals: Tensor of shape `[..., 3, M]` whose innermost 2 dimensions represent the tridiagonal matrices with three rows being the superdiagonal, diagonals, and subdiagonals, in order. The last element of the superdiagonal and the first element of the subdiagonal is ignored.
- rhs: Tensor of shape `[..., M, K]`, representing K right-hand sides per each
left-hand side. 

## Outputs

y: Tensor of shape `[..., M, K]` containing the solutions. 

## Attributes

partial_pivoting: Whether to perform partial pivoting. `True` by default.
Partial pivoting makes the procedure more stable, but slower. Partial
pivoting is unnecessary in some cases, including diagonally dominant and
symmetric positive definite matrices.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 diagonals: complex64,complex128,double,float32
- input1 rhs: complex64,complex128,double,float32
- output0 y: complex64,complex128,double,float32

## Third-party framework compatibility

Compatible with TensorFlow TridiagonalSolve operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
