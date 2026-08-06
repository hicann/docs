# IFFT2D

```c
REG_OP(IFFT2D)
    .INPUT(x, TensorType({DT_COMPLEX64,DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_COMPLEX64,DT_COMPLEX128}))
    .OP_END_FACTORY_REG(IFFT2D)
```

## Brief

Calculate the inverse 1-dimensional discrete Fourier transform on the
innermost dimension of the input. 

## Inputs

x: A Tensor. Must be the following types: complex64, complex128. 

## Outputs

y: A complex tensor with the same shape as input. The innermost dimension
of the input is replaced by its inverse two-dimensional Fourier transform. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128
- output0 y: complex64,complex128

## Third-party framework compatibility

Compatible with TensorFlow IFFT2D operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
