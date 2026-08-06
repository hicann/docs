# FFT2D

```c
REG_OP(FFT2D)
    .INPUT(x, TensorType({DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(FFT2D)
```

## Brief

2D fast Fourier transform. 

## Inputs

x: A complex64 or complex128 tensor.

## Outputs

y: A complex64 or complex128 tensor of the same shape as x. The inner-most 2
dimensions of `input` are replaced with their 2D Fourier transform. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128
- output0 y: complex64,complex128

## Third-party framework compatibility

Compatible with TensorFlow FFT2D operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
