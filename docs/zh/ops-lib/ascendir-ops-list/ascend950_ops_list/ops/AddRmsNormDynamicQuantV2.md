# AddRmsNormDynamicQuantV2

```c
REG_OP(AddRmsNormDynamicQuantV2)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale1, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale2, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_INT4}))
    .OUTPUT(y2, TensorType({DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_INT4}))
    .OUTPUT(y3, TensorType({DT_FLOAT}))
    .OUTPUT(y4, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(scale1, TensorType({DT_FLOAT}))
    .OUTPUT(scale2, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6)
    .ATTR(output_mask, ListBool, {})
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(AddRmsNormDynamicQuantV2)
```

## Brief

Fused Operator of AddRmsNorm and DynamicQuant . 

## Inputs

- x1: A tensor of type float16/bfloat16. Supported format "ND".
- x2: A tensor of type float16/bfloat16. Has the same dtype and shape as x1. Supported format "ND".
- gamma: A tensor of type float16/bfloat16. Supported format "ND".
The dtype is the same as x1, and the shape matches the last axis of x1. 
- smooth_scale1: Optional Input. A tensor of type float16/bfloat16. Supported format "ND".
The dtype is the same as x1, and the shape matches the last axis of x1. 
- smooth_scale2: Optional Input. A tensor of type float16/bfloat16. Supported format "ND".
The dtype is the same as x1, and the shape matches the last axis of x1. 

## Outputs

- y1: A tensor of type int8/hifloat8/float8_e5m2/float8_e4m3fn/int4, quantize result for rmsnorm(x1+x2)*smooth1+beta. Supported format "ND".
Has the same shape as x1. 
- y2: A tensor of type int8/hifloat8/float8_e5m2/float8_e4m3fn/int4, quantize result for rmsnorm(x1+x2)*smooth2+beta. Supported format "ND".
Has the same shape as x1. 
- y3: A tensor of type float32, cast result for rmsnorm(x1+x2). Supported format "ND".
Has the same shape as x1. 
- y4: A tensor of type float16/bfloat16, describe the result for rmsnorm(x1+x2). Supported format "ND".
Has the same dtype and shape as x1. 
- x: A tensor of type float16/bfloat16, describing the result of x1 + x2. Supported format "ND".
Has the same dtype and shape as x1. 
- scale1: A tensor of type float32, describing the result of dynamic quantize scales. Supported format "ND".
Consistent with x1 except for the last axis, with one less dimension than x1. 
- scale2: A tensor of type float32, describing the result of dynamic quantize scales. Supported format "ND".
Consistent with x1 except for the last axis, with one less dimension than x1. 

## Attributes

epsilon: An optional float, default value is 1e-6.
output_mask: An optional listbool, default value is 1e-6.
dst_type: An optional int, default value is DT_INT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 gamma: bfloat16,float16
- input3 smooth_scale1: bfloat16,float16
- input4 smooth_scale2: bfloat16,float16
- input5 beta: bfloat16,float16
- output0 y1: float8_e4m3fn,float8_e5m2,hifloat8,int4,int8
- output1 y2: float8_e4m3fn,float8_e5m2,hifloat8,int4,int8
- output2 y3: float32
- output3 y4: bfloat16,float16
- output4 x: bfloat16,float16
- output5 scale1: float32
- output6 scale2: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
