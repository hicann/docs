# SelfAdjointEig

```c
REG_OP(SelfAdjointEig)
    .INPUT(x, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(eigen_value, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(eigen_vector, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .ATTR(compute_v, Bool, true)
    .OP_END_FACTORY_REG(SelfAdjointEig)
```

## Brief

Computes the eigen decomposition of a batch of self-adjoint matrices . 

## Inputs

The input shape of x must be [..., N, N]. Inputs include:
x:Tensor of shape [..., N, N]. Only the lower triangular part of each inner
inner matrix is referenced . 

## Outputs

- eigen_value:Eigenvalues. Shape is [..., N]. Sorted in non-decreasing order.
- eigen_vector:Shape is [..., N, N]. The columns of the inner most matrices
contain eigenvectors of the corresponding matrices in tensor.

## Attributes

compute_v:bool. Defaults to True . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float32
- output0 eigen_value: complex64,complex128,double,float32
- output1 eigen_vector: complex64,complex128,double,float32

## Attention Constraints

The input x is a tensor of shape [..., N, N] whose inner-most 2 dimensions
form square matrices.   

## Third-party framework compatibility

Compatible with tensorflow SelfAdjointEig operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
