# STFT

```c
REG_OP(STFT)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OPTIONAL_INPUT(window, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(hop_length, Int, 0)
    .ATTR(win_length, Int, 0)
    .ATTR(normalized, Bool, false)
    .ATTR(onesided, Bool, true)
    .ATTR(return_complex, Bool, true)
    .REQUIRED_ATTR(n_fft, Int)
    .OP_END_FACTORY_REG(STFT)
```

## Brief

Computes the Fourier transform of short overlapping windows of the input. 

## Inputs

- x: A 1-D or 2-D tensor. Must be one of the following types:
float32, double, complex64, complex128.
- window: An optional tensor. The optional window function.
Must be one of the following types: float32, double, complex64, complex128.
Default: None (treated as window of all 1 s) 

## Outputs

y: A tensor containing the STFT result with shape described above. Must be
one of the following types: float32, double, complex64, complex128. 

## Attributes

- n_fft: A required int. Size of Fourier transform
- hop_length: An optional int. The distance between neighboring sliding window frames.
Default: 0 (treated as equal to floor(n_fft/4))
- win_length: An optional int. The size of window frame and STFT filter.
Default: 0 (treated as equal to n_fft)
- normalized: An optional bool. Controls whether to return the normalized STFT results Default: False
- onesided: An optional bool. Controls whether to return half of results to avoid redundancy for real inputs.
Default: True for real input and window, False otherwise.
- return_complex: An optional bool. Whether to return a complex tensor, or a real tensor
with an extra last dimension for the real and imaginary components. Default: True. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float32
- input1 window: complex64,complex128,double,float32
- output0 y: complex64,complex128,double,float32

## Third-party framework compatibility

Compatible with pytorch STFT operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
