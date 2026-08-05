# IRFFT

```c
REG_OP(IRFFT)
    .INPUT(x, TensorType({DT_COMPLEX64}))
    .INPUT(fft_length, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(IRFFT)
```

## Brief

Inverse real-valued fast Fourier transform. 

## Inputs

- x: A complex64 tensor.
- fft_length: An int32 tensor of shape [1]. The FFT length.

## Outputs

y: A float32 tensor of the same rank as `input`. The inner-most
dimension of `input` is replaced with the `fft_length` samples of its inverse
1D Fourier transform. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input1 fft_length: int32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow IRFFT operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
