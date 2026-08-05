# IFFT

```c
REG_OP(IFFT)
    .INPUT(x, TensorType({DT_COMPLEX64,DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_COMPLEX64,DT_COMPLEX128}))
    .OP_END_FACTORY_REG(IFFT)
```

## Brief

Computes the inverse 1-dimensional discrete Fourier transform over the
inner-most dimension of `x`. 

## Inputs

x: A Tensor. Must be the following types: complex64, complex128. 

## Outputs

y: A complex tensor of the same rank as `x`. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128
- output0 y: complex64,complex128

## Third-party framework compatibility

Compatible with TensorFlow IFFT operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
