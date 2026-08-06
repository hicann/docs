# RmsNormDynamicMxQuant

```c
REG_OP(RmsNormDynamicMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(rstd, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-06)
    .ATTR(scale_alg, Int, 0)
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, 40)
    .ATTR(output_rstd, Bool, false)
    .OP_END_FACTORY_REG(RmsNormDynamicMxQuant)
```

## Brief

Performs RMS normalization followed by dynamic MX quantization on input tensor.
Applies RMS normalization to the input tensor and then quantizes it using block-wise scaling factors.
Supports various 4-bit and 8-bit floating point output formats.

## Inputs

- x: An input tensor of type float16 or bfloat16.
The shape supports at least 1 dimension, and at most 7 dimensions.
- gamma: A scale tensor of type float16, bfloat16 or float32.
The shape must match the normalized dimension of x.
- beta: An optional bias tensor of type float16, bfloat16 or float32.
The shape must match the normalized dimension of x.

## Outputs

- y: Quantized output tensor. It has the same shape and rank as input x.
- mxscale: An output tensor of type FLOAT8_E8M0. The scale tensor for MX quantization.
- rstd: An output tensor of type FLOAT32. The reciprocal of standard deviation from RMS normalization.

## Attributes

- epsilon: An optional float. A small value added to the variance for numerical stability. Defaults to 1e-06.
- scale_alg: An optional int. The quantization algorithm. Defaults to 0.
Support OCP(0) or CUSTOM_NV(1).
- round_mode: An optional string. Defaults to "rint".
- dst_type: An optional int. Declare the output y dtype. Support FLOAT4_E2M1, FLOAT4_E1M2,
FLOAT8_E4M3FN or FLOAT8_E5M2. Defaults to FLOAT4_E2M1.
- output_rstd: An optional bool. Whether to output rstd. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 gamma: bfloat16,float16,float32
- input2 beta: bfloat16,float16,float32
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 mxscale: float8_e8m0
- output2 rstd: float32

## Attention Constraints

- When dst_type is DT_FLOAT8_E5M2 or DT_FLOAT8_E4M3FN, round_mode only supports "rint".
- When dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, round_mode supports "rint", "floor" and "round".
- If dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, the input x last dimension of the shape must be divisible by 2.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
