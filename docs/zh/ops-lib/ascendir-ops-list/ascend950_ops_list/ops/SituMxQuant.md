# SituMxQuant

```c
REG_OP(SituMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(y_scale, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(beta, Float, 1.0f)
    .ATTR(linear_beta, Float, 0.0f)
    .ATTR(activate_left, Bool, false)
    .ATTR(axis, Int, -1)
    .ATTR(dst_type, Int, DT_FLOAT4_E2M1)
    .ATTR(round_mode, String, "rint")
    .OP_END_FACTORY_REG(SituMxQuant)
```

## Brief

Performs Situ activation followed by dynamic MX quantization on input tensor.
This fused operator first computes Situ activation by splitting input along the last dimension,
then applies block-wise MX quantization along the specified axis.

## Inputs

- x: An input tensor of type float16 or bfloat16.
The size of the last dimension must be divisible by 2.
Supports 1-7 dimensional tensors.

## Outputs

- y: Quantized output tensor after Situ activation.
Shape is same as input except last dimension is halved.
Data type is float4_e2m1, float4_e1m2, float8_e4m3fn, or float8_e5m2.
- y_scale: Scale factors for each quantization block. Data type is float8_e8m0.
Shape: y_shape with axis dimension replaced by ceil(y_shape[axis] / 64), plus trailing dim of 2.

## Attributes

- beta: An optional float. Beta parameter for Situ activation. Must be greater than 0. Defaults to 1.0.
- linear_beta: An optional float. Linear beta parameter for Situ activation.
When <= 0, the linear_beta transformation is not applied. Defaults to 0.0.
- activate_left: An optional bool. When true, gate is the first half and up is the second half.
When false, gate is the second half and up is the first half. Defaults to false.
- axis: An optional int. Axis along which to perform block-wise quantization.
Currently only supports -1 (last axis). Defaults to -1.
- dst_type: An optional int. Target quantization data type.
40=FP4_E2M1, 41=FP4_E1M2, 36=FP8_E4M3FN, 35=FP8_E5M2. Defaults to 40 (FP4_E2M1).
- round_mode: An optional string. Rounding mode for quantization.
Supports "rint", "round", "floor". FP8 output only supports "rint". Defaults to "rint".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 y_scale: float8_e8m0

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.

## Constraints

- Input last dimension must be divisible by 2.
- axis must be -1 (last axis).
- beta must be greater than 0.
- dst_type must be 40 (FP4_E2M1), 41 (FP4_E1M2), 36 (FP8_E4M3FN), or 35 (FP8_E5M2).
- When dst_type is FP8, round_mode must be "rint".
- When dst_type is FP4, output last dim must be even.


---

[Back to Operator Specifications (Ascend950)](../README.md)
