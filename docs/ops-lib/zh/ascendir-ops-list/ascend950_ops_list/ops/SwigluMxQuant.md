# SwigluMxQuant

```c
REG_OP(SwigluMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(activate_dim, Int, -1)
    .ATTR(activate_left, Bool, false)
    .ATTR(swiglu_mode, Int, 0)
    .ATTR(clamp_limit, Float, 7.0f)
    .ATTR(glu_alpha, Float, 1.702f)
    .ATTR(glu_bias, Float, 1.0f)
    .ATTR(group_mode, Int, 0)
    .ATTR(axis, Int, -1)
    .ATTR(dst_type, Int, DT_FLOAT4_E2M1)
    .ATTR(round_mode, String, "rint")
    .ATTR(scale_alg, Int, 0)
    .ATTR(max_dtype_value, Float, 0.0f)
    .OP_END_FACTORY_REG(SwigluMxQuant)
```

## Brief

Performs SwiGLU activation followed by dynamic MX quantization on input tensor.
This fused operator first computes SwiGLU activation by splitting input along activate_dim,
then applies block-wise quantization along the specified axis.

## Inputs

- x: An input tensor. Must be one of the following types: float16, bfloat16.
The size of the dimension specified by activate_dim must be divisible by 2.
Supports 2-7 dimensional tensors.
- group_index: An optional tensor. Must be one of the following types: int32, int64.
If provided, group_index must be 1-dimensional and its shape must be less than or equal to 256.

## Outputs

- y: Quantized output tensor after SwiGLU activation.
Shape is same as input except activate_dim dimension is halved.
Data type is one of: float4_e2m1, float4_e1m2, float8_e4m3fn, float8_e5m2.
- mxscale: Scale factors for each quantization block. Data type is float8_e8m0.
Shape calculation: 
- Let act_shape be the shape after SwiGLU (input shape with activate_dim halved) 
- axis_idx = axis if axis >= 0 else axis + rank(act_shape) 
- mxscale.shape = act_shape 
- mxscale.shape[axis_idx] = ceil(act_shape[axis_idx] / 32) 
- mxscale.shape[-1] = (mxscale.shape[-1] + 1) // 2  (packed storage) 
- mxscale.shape = mxscale.shape + [2]  (last dimension expanded to 2 for real/imaginary parts)

## Attributes

- activate_left: An optional bool. Reserved parameter for SwiGLU activation side. Defaults to false.
- activate_dim: An optional int. Dimension along which to split input for SwiGLU.
Must be last or second-to-last dimension. Defaults to -1.
- swiglu_mode: An optional int. Reserved parameter for SwiGLU variant mode. Defaults to 0. When swiglu_mode = 1,
clamp_limit must greater than 0
- clamp_limit: An optional float. Reserved parameter for clamp limit in SwiGLU variant. Defaults to 7.0.
- glu_alpha: An optional float. Reserved parameter for alpha value in SwiGLU variant. Defaults to 1.702.
- glu_bias: An optional float. Reserved parameter for bias value in SwiGLU variant. Defaults to 1.0.
- group_mode: An optional int. Group index mode. Effective when group_index is provided.
0=count mode, 1=cumsum mode. Defaults to 0.Currently only supports 0.
- axis: An optional int. Axis along which to perform block-wise quantization.
Must be last or second-to-last dimension. Defaults to -1.
- dst_type: An optional int. Target quantization data type.
40=FP4_E2M1, 41=FP4_E1M2, 36=FP8_E4M3FN, 35=FP8_E5M2. Defaults to 40 (FP4_E2M1).
- round_mode: An optional string. Rounding mode for quantization.
Supports "rint", "floor", "round". Defaults to "rint". When dst_type = 35 or 36, round_mode must be "rint".
- scale_alg: An optional int. Algorithm for computing scale factors.
0=OCP, 1=cuBLAS, 2=RNE. Defaults to 0.When dst_type = 40 or 41, scale_alg must be 0.
- max_dtype_value: An optional float. Reserved parameter for maximum dtype value. Used when scale_alg=2 and
dst_type=FP4_E1M2. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 group_index: int32,int64
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 mxscale: float8_e8m0

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.

## Constraints

- Input dimension specified by activate_dim must be divisible by 2.
- activate_dim and axis must be last or second-to-last dimension, example -1 or -2;
- When dst_type is FP4 (40 or 41), the last dimension of y shape must be an even number.
- When dst_type is FP8_E4M3FN (36) or FP8_E5M2 (35), round_mode supports "rint".
- When dst_type is FP4_E2M1 (40) or FP4_E1M2 (41), round_mode supports "rint", "floor", "round".
- When activate_dim or axis is not the last axis, if group_index is provided, input x shape must be 2-dimensional.
- If group_index is provided, it must be 1-dimensional and its shape must be less than or equal to 256.
- When dst_type is FP4 (40 or 41), scale_alg must be 0.
- When activate_dim is not the last axis, swiglu_mode must be 0.


---

[Back to Operator Specifications (Ascend950)](../README.md)
