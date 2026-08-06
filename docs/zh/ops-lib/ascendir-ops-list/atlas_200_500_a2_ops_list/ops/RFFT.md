# RFFT

```c
REG_OP(RFFT)
    .INPUT(input, TensorType({DT_FLOAT}))
    .INPUT(fft_length, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_COMPLEX64}))
    .OP_END_FACTORY_REG(RFFT)
```

## Brief

Real-valued fast Fourier transform . 

## Inputs

- input: A float32 tensor.
- fft_length: An int32 tensor of shape [1]. The FFT length .

## Outputs

y: A complex64 tensor of the same rank as `input`. The inner-most
dimension of `input` is replaced with the `fft_length / 2 + 1` unique
frequency components of its 1D Fourier transform . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: float32
- input1 fft_length: int32
- output0 y: complex64

## Third-party framework compatibility

Compatible with TensorFlow RFFT operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
