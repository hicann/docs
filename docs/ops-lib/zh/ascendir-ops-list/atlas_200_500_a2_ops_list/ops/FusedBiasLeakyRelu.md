# FusedBiasLeakyRelu

```c
REG_OP(FusedBiasLeakyRelu)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE}))
    .INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE}))
    .ATTR(negative_slope, Float, 0.2f)
    .ATTR(scale, Float, 1.414213562373f)
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE}))
    .OP_END_FACTORY_REG(FusedBiasLeakyRelu)
```

## Brief

Computes the output as scale * (x + bias) if x+bias > 0 and scale * negative_slope * (x+bias)
if x+bias <= 0 . 

## Inputs

Two input:
x: A Tensor. Must be one of the following types: float32, float16, double.
bias: A Tensor. Must be one of the following types: float32, float16, double.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

negative_slope: A float32. Defaults to "0.2".
sacle: A float32. Defaults to "2**0.5".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 bias: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the mmcv operator FusedBiasLeakyrelu.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
