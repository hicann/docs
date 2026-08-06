# Qr

```c
REG_OP(Qr)
    .INPUT(x, TensorType({ DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(q, TensorType({ DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128 }))
    .OUTPUT(r, TensorType({ DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128 }))
    .ATTR(full_matrices, Bool, false)
    .OP_END_FACTORY_REG(Qr)
```

## Brief

Computes the QR decompositions of one or more matrices . 

## Inputs

The input shape of x must be [..., M, N]. Inputs include:
x:A Tensor whose shape is [..., M, N]. 

## Outputs

- q: A Tensor. Has the same type as x.
- r: A Tensor. Has the same type as x .

## Attributes

full_matrices: An optional bool. Defaults to False. If true, compute
full-sized q and r. If false (the default), compute only the leading P
columns of q . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 q: complex64,complex128,double,float16,float32
- output1 r: complex64,complex128,double,float16,float32

## Attention Constraints

The input matrix x is a tensor of shape [..., M, N] whose inner-most 2
dimensions form matrices of size [M, N].  

## Third-party framework compatibility

Compatible with tensorflow Qr operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
