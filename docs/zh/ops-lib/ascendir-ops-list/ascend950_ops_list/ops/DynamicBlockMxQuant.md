# DynamicBlockMxQuant

```c
REG_OP(DynamicBlockMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(scale1, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(scale2, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT4_E2M1)
    .ATTR(scale_alg, Int, 0)
    .ATTR(dst_type_max, Float, 0.0)
    .OP_END_FACTORY_REG(DynamicBlockMxQuant)
```

## Brief

Performs dynamic BLOCK MX quantization on input tensor.
Quantizes the input tensor along the specified axis using block-wise scaling factors.
Supports various 4-bit and 8-bit floating point output formats.

## Inputs

- x: An input tensor of type float16 or bfloat16.
The shape supports at least 2 dimensions, and at most 3 dimensions.

## Outputs

- y: Quantized output tensor. It has the same shape and rank as input x.
- scale1: An output tensor of type DT_FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(scale1) = rank(x) + 1.
- axis= -1.
- axis_change = axis if axis >= 0 else axis + rank(x).
- scale1.shape[axis_change] = (ceil(x.shape[axis] / 32) + 2 -1) / 2.
- scale1.shape[rank(x)] = 2.
- Other dimensions match input x.
- scale2: An output tensor of type DT_FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(scale2) = rank(x) + 1.
- axis= -2.
- axis_change = axis if axis >= 0 else axis + rank(x).
- scale2.shape[axis_change] = (ceil(x.shape[axis] / 32) + 2 -1) / 2.
- scale2.shape[rank(x)] = 2.
- Other dimensions match input x.
- scale2 tensor is padded with zeros to ensure its size along the quantized axis is even.

## Attributes

- round_mode: An optional string. Defaults to "rint".
Support "rint", "round", "floor".
- dst_type: An optional int. Declare the output y dtype.
Support DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN or DT_FLOAT8_E5M2. Defaults to DT_FLOAT4_E2M1.
- scale_alg: An optional int. The algorithm for the scale in quantization. Default to 0.
Support DT_FLOAT4_E2M1/DT_FLOAT4_E1M2/DT_FLOAT8_E4M3FN/DT_FLOAT8_E5M2(OCP Microscaling Formats (Mx) Specification,
count 0)
or DT_FLOAT4_E2M1(Dynamic Dtype Range, count 2).
- dst_type_max: Takes effect when scale_alg=2, with a default value of 0.0, where 0.0 presents max_type as the
maximum value of the dst_type.
If other numeric values are provides, the scale must be computed based on the input value.
Currently supported valid values are 0.0/6.0/7.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 scale1: float8_e8m0
- output2 scale2: float8_e8m0

## Attention Constraints

- When dst_type is DT_FLOAT8_E5M2 or DT_FLOAT8_E4M3FN, round_mode only supports "rint".
- When dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, round_mode supports "rint", "floor" and "round".
- If dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, the input x last dimension of the shape must be divisible by 2.
- When scale_alg=2, dst_type_max can only be set in DT_FLOAT4_E2M1 scenarios.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
