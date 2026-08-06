# CholeskyGrad

```c
REG_OP(CholeskyGrad)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(grad, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(CholeskyGrad)
```

## Brief

Computes the reverse mode backpropagated gradient of the Cholesky
algorithm . 

## Inputs

The input x has to be symmetric and positive definite. Inputs include:
- x:A Tensor. Must be one of the following types: double, float32. Output
of batch Cholesky algorithm x = cholesky(A). Shape is [..., M, M]. Algorithm
depends only on lower triangular part of the innermost matrices of this tensor.
- grad:A Tensor. Must have the same type as l. df/dx where f is some
scalar function. Shape is [..., M, M]. Algorithm depends only on lower
triangular part of the innermost matrices of this tensor . 

## Outputs

y:A Tensor. Has the same type as x . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float32
- input1 grad: double,float32
- output0 y: double,float32

## Attention Constraints

The input x is a tensor of shape [..., M, M] whose inner-most 2 dimensions
form square matrices.

## Third-party framework compatibility

Compatible with tensorflow CholeskyGrad operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
