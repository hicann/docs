# Svd

```c
REG_OP(Svd)
    .INPUT(x, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(sigma, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(u, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(v, TensorType({ DT_DOUBLE, DT_FLOAT, DT_COMPLEX64, DT_COMPLEX128 }))
    .ATTR(compute_uv, Bool, true)
    .ATTR(full_matrices, Bool, false)
    .OP_END_FACTORY_REG(Svd)
```

## Brief

Computes the singular value decompositions of one or more matrices . 

## Inputs

The input shape of x must be [..., N, N]. Inputs include:
x:Tensor of shape [..., M, N]. Let P be the minimum of M and N . 

## Outputs

- sigma:Singular values. Shape is [..., P]. The values are sorted in
reverse order of magnitude, so s[..., 0] is the largest value, s[..., 1]
is the second largest, etc.
- u:Left singular vectors. If full_matrices is False (default) then shape
is [..., M, P]; if full_matrices is True then shape is [..., M, M]. Not
returned if compute_uv is False.
- v:Right singular vectors. If full_matrices is False (default) then shape
is [..., N, P]. If full_matrices is True then shape is [..., N, N]. Not
returned if compute_uv is False . 

## Attributes

- compute_uv: An optional bool. Defaults to True. If True then left and right singular vectors will be computed and
returned in u and v, respectively. Otherwise, only the singular values will
be computed, which can be significantly faster .
- full_matrices: An optional bool that param effect u,v. Defaults to False.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float32
- output0 sigma: complex64,complex128,double,float32
- output1 u: complex64,complex128,double,float32
- output2 v: complex64,complex128,double,float32

## Attention Constraints

The input x is a tensor of shape [..., N, N] whose inner-most 2 dimensions
form square matrices.  

## Third-party framework compatibility

Compatible with tensorflow Svd operator


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
