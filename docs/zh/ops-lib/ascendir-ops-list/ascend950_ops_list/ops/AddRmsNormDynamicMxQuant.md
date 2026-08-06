# AddRmsNormDynamicMxQuant

```c
REG_OP(AddRmsNormDynamicMxQuant)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1, DT_FLOAT4_E1M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2}))
    .OUTPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(mxscale, TensorType({DT_FLOAT8_E8M0}))
    .OUTPUT(rstd, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6)
    .ATTR(scale_alg, Int, 0)
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, 40)
    .ATTR(output_rstd, Bool, false)
    .OP_END_FACTORY_REG(AddRmsNormDynamicMxQuant)
```

## Brief

Fused Operator of AddRmsNorm and DynamicMxQuant.
Computes x = x1 + x2, applies RMS normalization with gamma/beta, then quantizes.
Supports various 4-bit and 8-bit floating point output formats.
Calculating process: 
 x = x1 + x2 
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) 
 rmsnorm_out = x * rstd * gamma 
 the normalized result using block-wise MX scaling factors along the last axis.

## Inputs

- x1: A tensor for add compute. Support dtype: float16, bfloat16, support format: ND.
- x2: A tensor for add compute. Support dtype: float16, bfloat16, support format: ND.
- gamma: A tensor for rms norm weight params. Support dtype: float32, float16, bfloat16, support format: ND.
- beta: An optional tensor for rms norm weight params. Support dtype: float32, float16, bfloat16, support format: ND.

## Outputs

- y: Quantize result.
    A tensor. Support dtype: Support FLOAT4_E2M1, FLOAT4_E1M2, FLOAT8_E4M3FN or FLOAT8_E5M2, support format: ND.
- x: Describing the result of x1 + x2.
    A tensor. Support dtype: float16, bfloat16, support format: ND.
- mxscale: An output tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
- rank(mxscale) = rank(x) + 1.
- axis_change = axis if axis >= 0 else axis + rank(x).
- mxscale.shape[axis_change] = (ceil(x.shape[axis] / blocksize) + 2 - 1) / 2.
- mxscale.shape[rank(x)] = 2.
- Other dimensions match input x.
- rstd: A tensor. Describing the reciprocal of (x1 + x2)'s standard deviation.
          Support dtype: float32, support format: ND.

## Attributes

- epsilon: An optional attribute for numerical stability in rms norm, the type is float32. Defaults to 1e-6.
- scale_alg: An optional int.The algorithm for the scale in quantization. Default to 0.
Support (OCP , count 0) or (nvidia-cuBLAS , count 1).
- round_mode: An optional string. Defaults to "rint".
- dst_type: An optional attribute. Declare the output y dtype. Support FLOAT4_E2M1, FLOAT4_E1M2,
FLOAT8_E4M3FN or FLOAT8_E5M2. Defaults to FLOAT4_E2M1 (40).
- output_rstd: An optional attribute. Defaults to "false". Whether to output Rstd.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 gamma: bfloat16,float16,float32
- input3 beta: bfloat16,float16,float32
- output0 y: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2
- output1 x: bfloat16,float16
- output2 mxscale: float8_e8m0
- output3 rstd: float32

## Attention Constraints

- When dst_type is DT_FLOAT8_E5M2 or DT_FLOAT8_E4M3FN, round_mode only supports "rint".
- When dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, round_mode supports "rint", "floor" and "round".
- If dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, the input x last dimension of the shape must be divisible by 2.
- If dst_type is DT_FLOAT4_E2M1 or DT_FLOAT4_E1M2, the scale_alg only support (OCP , count 0).


---

[Back to Operator Specifications (Ascend950)](../README.md)
