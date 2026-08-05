# DynamicMxQuant

```c
REG_OP(DynamicMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT6_E3M2, DT_FLOAT6_E2M3, DT_FLOAT8_E4M3FN,
                           DT_FLOAT8_E5M2}))
    .OUTPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(axis, Int, -1)
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT4_E2M1)
    .ATTR(blocksize, Int, 32)
    .ATTR(scale_alg, Int, 0)
    .ATTR(dst_type_max, Float, 0.0)
    .ATTR(max_low_bound, Float, 0.0)
    .OP_END_FACTORY_REG(DynamicMxQuant)
```

## Brief

Performs dynamic MX quantization on input tensor.
Quantizes the input tensor along the specified axis using block-wise scaling factors.
Supports various 4-bit and 8-bit floating point output formats.

## Inputs

- x: An input tensor of type float16, bfloat16 or float.
The shape supports at least 1 dimensions, and at most 7 dimensions.

## Outputs

- y: Quantized output tensor. It has the same shape and rank as input x.
- mxscale: An output tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(mxscale) = rank(x) + 1.
- axis_change = axis if axis >= 0 else axis + rank(x).
- mxscale.shape[axis_change] = (ceil(x.shape[axis] / blocksize) + 2 - 1) / 2.
- mxscale.shape[rank(x)] = 2.
- Other dimensions match input x.
mxscale tensor is padded with zeros to ensure its size along the quantized axis is even.

## Attributes

- axis: An optional int. Axis along which to quantize. Defaults to -1.
must be in the range [-rank(input x), rank(input x)).
- round_mode: An optional string. Defaults to "rint".
- dst_type: An optional int. Declare the output y dtype. Support FLOAT4_E2M1, FLOAT4_E1M2,
FLOAT8_E4M3FN or FLOAT8_E5M2. Defaults to FLOAT4_E2M1.
- blocksize: An optional int. Block size for quantization scaling factors.Defaults to 32.
When scale_alg is 2, blocksize must be 32.
- scale_alg: An optional int.The algorithm for the scale in quantization.Default to 0.
Support MxFP8/MxFP4(OCP Microscaling Formats (Mx) Specification , count 0) or MxFP8(nvidia-cuBLAS , count 1) or
MxFP4(Dynamic Dtype Range , count 2).
- dst_type_max: An optional Float.Max_dtype takes the maximum value of the quant_data_type, or the provided
value.Defaults to 0.
Only support in FP4_E2M1 mode, with a valid range of 6.0 to 12.0.
- max_low_bound: An optional Float, indicates the maximum value limit for scale calculation. Defaults to 0. Only
support when scale_alg=1. Must be non-negative.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 mxscale: float8_e8m0

## Attention Constraints

- When dst_type is DT_FLOAT8_E5M2 or DT_FLOAT8_E4M3FN, round_mode only supports "rint".
- When dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, round_mode supports "rint", "floor" and "round".
- If dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, the input x last dimension of the shape must be divisible by 2.
- The blocksize must be a multiple of 32 (non-zero) and ≤ 1024.
When scale_alg is 2, blocksize must be 32.
- The value of dst_max_value only supports 0.0 or 6.0-12.0 and is effective when scale_alg=2.
The default value 0.0 means that maxType corresponds to the maximum value of the target data type.
If other values are provided, mxscale is calculated based on the provided value.
- When x's data type is float, blocksize must be 32.
- When x's data type is float, the size of the quantization axis must not be less than 32.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
