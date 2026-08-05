# DynamicMxQuantWithDualAxis

```c
REG_OP(DynamicMxQuantWithDualAxis)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(mxscale1, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(y2, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(mxscale2, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT4_E2M1)
    .ATTR(scale_alg, Int, 0)
    .ATTR(dst_type_max, Float, 0.0)
    .OP_END_FACTORY_REG(DynamicMxQuantWithDualAxis)
```

## Brief

Performs dynamic MX quantization on input tensor along -1 and -2 axes simultaneously.
Quantizes the input tensor along both -1 and -2 axes using block-wise scaling factors (blocksize=32).
Supports various 4-bit and 8-bit floating point output formats.

## Inputs

- x: An input tensor of type float16 or bfloat16.
The shape supports at least 2 dimensions, and at most 7 dimensions.

## Outputs

- y1: Quantized output tensor along -1 axis. It has the same shape and rank as input x.
- mxscale1: An output tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(mxscale1) = rank(x) + 1.
- axis = -1.
- axis_change = axis + rank(x).
- mxscale1.shape[axis_change] = (ceil(x.shape[axis] / 32) + 2 - 1) / 2.
- mxscale1.shape[rank(x)] = 2.
- Other dimensions match input x.
- y2: Quantized output tensor along -2 axis. It has the same shape and rank as input x.
- mxscale2: An output tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(mxscale2) = rank(x) + 1.
- axis = -2.
- axis_change = axis + rank(x).
- mxscale2.shape[axis_change] = (ceil(x.shape[axis] / 32) + 2 - 1) / 2.
- mxscale2.shape[rank(x)] = 2.
- Other dimensions match input x.
mxscale tensor is padded with zeros to ensure its size along the quantized axis is even.

## Attributes

- round_mode: An optional string. Defaults to "rint".
- dst_type: An optional int. Declare the output y dtype. Support FLOAT4_E2M1, FLOAT4_E1M2,
FLOAT8_E4M3FN or FLOAT8_E5M2. Defaults to FLOAT4_E2M1.
- scale_alg: An optional int. The algorithm for the scale in quantization. Default to 0.
Support MxFP8/MxFP4(OCP Microscaling Formats (Mx) Specification, count 0)
or MxFP8(nvidia-cuBLAS, count 1) or MxFP4(Dynamic Dtype Range, count 2).
- dst_type_max: An optional Float. Max_dtype takes the maximum value of the quant_data_type,
or the provided value. Defaults to 0.
Only support in FP4_E2M1 mode with scale_alg=2, with a valid range of 6.0 to 12.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- output0 y1: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 mxscale1: float8_e8m0
- output2 y2: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output3 mxscale2: float8_e8m0

## Attention Constraints

- When dst_type is DT_FLOAT8_E5M2 or DT_FLOAT8_E4M3FN, round_mode only supports "rint".
- When dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, round_mode supports "rint", "floor" and "round".
- If dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, the input x last dimension of the shape must be divisible by 2.
- When dst_type is DT_FLOAT4_E1M2, scale_alg must be 0.
- When dst_type is DT_FLOAT4_E2M1, scale_alg must be 0 or 2.
- When dst_type is DT_FLOAT8_E4M3FN or DT_FLOAT8_E5M2, scale_alg must be 0 or 1.
- The value of dst_type_max only supports 0.0 or 6.0-12.0 and is effective when scale_alg=2.
The default value 0.0 means that maxType corresponds to the maximum value of the target data type.
If other values are provided, mxscale is calculated based on the provided value.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
