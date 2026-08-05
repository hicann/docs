# AddRmsNormDynamicQuant

```c
REG_OP(AddRmsNormDynamicQuant)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale1, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale2, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_INT8, DT_HIFLOAT8, DT_FP8_E5M2, DT_FP8_E4M3FN}))
    .OUTPUT(y2, TensorType({DT_INT8, DT_HIFLOAT8, DT_FP8_E5M2, DT_FP8_E4M3FN}))
    .OUTPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(scale1, TensorType({DT_FLOAT, DT_FLOAT}))
    .OUTPUT(scale2, TensorType({DT_FLOAT, DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6)
    .ATTR(output_mask, ListBool, {})
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(AddRmsNormDynamicQuant)
```

```c
 x = x1 + x2 \n
 rstd = np.rsqrt(np.mean(np.power(x, 2), reduce_axis, keepdims=True) + epsilon)) \n
 rmsnorm_out = x * rstd * gamma + beta \n
 if output_mask is null:
   if smooth_scales1 exist: \n
     scale1 = row_max(abs(rmsnorm_out * smooth_scale1)) / 127 \n
   else smooth_scales1 not exist: \n
     scale1 = row_max(abs(rmsnorm_out)) / 127 \n
   y1 = round(rmsnorm_out / scale1) \n
   if smooth_scales1 exist && smooth_scales2 exist: \n
     scale2 = row_max(abs(rmsnorm_out * smooth_scale2)) / 127 \n
     y2 = round(rmsnorm_out / scale2) \n
   if smooth_scales2 not exist:  \n
     not calculate scale2 and y2. \n
 if output_mask[0] is true: \n
   if smooth_scales1 exist
     scale1 = row_max(abs(rmsnorm_out * smooth_scale1)) / 127 \n
   else smooth_scales1 not exist: \n
     scale1 = row_max(abs(rmsnorm_out)) / 127 \n
   y1 = round(rmsnorm_out / scale1) \n
 if output_mask[1] is true: \n
   if smooth_scales2 exist
     scale2 = row_max(abs(rmsnorm_out * smooth_scale2)) / 127 \n
   else smooth_scales2 not exist: \n
     scale2 = row_max(abs(rmsnorm_out)) / 127 \n
   y2 = round(rmsnorm_out / scale2) \n
 if output_mask[0] is false:  \n
   not calculate scale1 and y1. \n
 if output_mask[1] is false:  \n
   not calculate scale2 and y2. \n
```

## Brief

Fused Operator of Add, RmsNorm and DynamicQuant.
Calculating input: x1, x2, gamma, smooth_scale1, smooth_scale2 
Calculating process: 

## Inputs

- x1: A tensor. Input x1 for the add operation.
Support dtype: float16/bfloat16, support format: ND. Support 2-8 dimensions.
- x2: A tensor. Input x2 for the add operation.
Support dtype: float16/bfloat16, support format: ND. Has the same dtype and shape as "x1".
- gamma: A tensor. Describing the weight of the rmsnorm operation.
Support dtype: float16/bfloat16, support format: ND. Has the same dtype as "x1". The shape must be same with the last dimension of x1.
- smooth_scale1: A tensor. Describing the weight of the first dynamic quantization.
Support dtype: float16/bfloat16, support format: ND. Has the same dtype and shape as "gamma".
- smooth_scale2: An optional input tensor. Describing the weight of the secend dynamic quantization.
Support dtype: float16/bfloat16, support format: ND. Has the same dtype and shape as "gamma".
- beta: An optional input tensor. Describing the offset value of dynamic quantization.
Support dtype: float16/bfloat16, support format: ND. Has the same dtype and shape as "gamma".

## Outputs

- y1: A tensor. Describing the output of the first dynamic quantization.
Support dtype: int8/hifloat8/float8e5m2/float8e4m3fn, support format: ND. Has the same shape as "x1".
- y2: A tensor. Describing the output of the second dynamic quantization.
Support dtype: int8/hifloat8/float8e5m2/float8e4m3fn, support format: ND. Has the same shape as "x1".
- x: A tensor. Describing the output of the x1+x2 add operation.
Support dtype: float16/bfloat16, support format: ND. Has the same dtype and shape as "x1".
- scale1: A tensor. Describing of the factor for the first dynamic quantization.
Support dtype: float32, support format: ND. Has the same shape as "gamma".
- scale2: A tensor. Describing of the factor for the second dynamic quantization.
Support dtype: float32, support format: ND. Has the same shape as "gamma".

## Attributes

- epsilon: An optional attribute. Describing the epsilon of the rmsnorm operation.
             The type is float. Defaults to 1e-6.
- dst_type: An optional int32. Output y data type enum value. Support DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2,
              DT_FLOAT8_E4M3FN. Defaults to DT_INT8.
- output_mask: An optional attribute, a list composed of bool. Defaults value is {}. Support length of 2.
The output_mask[0] is false, y1 and scale1 is meaningless.
The output_mask[1] is false, y2 and scale2 is meaningless.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 gamma: bfloat16,float16
- input3 smooth_scale1: bfloat16,float16
- input4 smooth_scale2: bfloat16,float16
- input5 beta: bfloat16,float16
- output0 y1: int4,int8
- output1 y2: int4,int8
- output2 x: bfloat16,float16
- output3 scale1: float32
- output4 scale2: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
