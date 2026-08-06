# MatrixInverse

```c
REG_OP(MatrixInverse)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(adjoint, Bool, false)
    .OP_END_FACTORY_REG(MatrixInverse)
```

## Brief

Computes the inverse of one or more square invertible matrices or
their adjoints (conjugate transposes) . 

## Inputs

The input x is a tensor of shape [..., M, M] whose inner-most 2 dimensions
form square matrices. Inputs include:
x:A Tensor of input. Shape is [..., M, M] . 

## Outputs

y:A Tensor. Has the same type as x . 

## Attributes

adjoint:An optional bool. Defaults to False.Boolean indicating whether to
deal with matrix or its (block-wise) adjoint . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float32
- output0 y: complex64,complex128,double,float32

## Attention Constraints

The input x is a tensor of shape [..., M, M] whose inner-most 2 dimensions
form square matrices.  

## Third-party framework compatibility

Compatible with tensorflow MatrixInverse operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
