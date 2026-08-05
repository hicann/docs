# AddLayerNormQuantV2

```c
REG_OP(AddLayerNormQuantV2)
    .INPUT(x1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(gamma, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(beta, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(scales1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(scales2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(zero_points1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(zero_points2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y1, ge::TensorType({DT_INT8}))
    .OUTPUT(y2, ge::TensorType({DT_INT8}))
    .OUTPUT(x, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(layernorm_res, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(out_scales1, ge::TensorType({DT_FLOAT}))
    .OUTPUT(out_scales2, ge::TensorType({DT_FLOAT}))
    .ATTR(quant_mode, String, "dynamic")
    .ATTR(epsilon, Float, 1e-5f)
    .ATTR(additional_output, Bool, false)
    .ATTR(div_mode, Bool, true)
    .OP_END_FACTORY_REG(AddLayerNormQuantV2)
```

## Brief

Fused Operator of AddLayerNorm and Quantize/DynamicQuant/AscendQuantV2. 
 calculating: x1, x2, gamma, beta, bias, scales1, scales2, zero_points1, zero_points2 
 x = x1 + x2 + bias 
 rstd = 1 / (sqrt(Var(x) + eps)) 
 layernorm_res = (x - E(x)) * rstd * gamma + beta 
 when quant_mode = "static" and div_mode=true, output out_scales1 and out_scales2 are invalid: 
 y1 = round(y / scales1) + zero_points1 
 y2 = round(y / scales2) + zero_points2 
 when quant_mode = "static" and div_mode=false, output out_scales1 and out_scales2 are invalid: 
 y1 = round(y * scales1) + zero_points1 
 y2 = round(y * scales2) + zero_points2 
 when quant_mode = "dynamic": 
 tmp1 = y * scales1 
 tmp2 = y * scales2 
 out_scales1 = reduce_max(abs(tmp1))/127 
 out_scales2 = reduce_max(abs(tmp2))/127 
 y1 = round(tmp1 / out_scales1) 
 y2 = round(tmp2 / out_scales2) 

## Inputs

- x1: A tensor for add compute. Support dtype: float32, float16, bfloat16, support format: ND.
- x2: A tensor for add compute. Support dtype: float32, float16, bfloat16, support format: ND.
- gamma: A tensor for layer norm weight params. Support dtype: float32, float16, bfloat16, support format: ND.
- beta: A tensor for layer norm weight params. Support dtype: float32, float16, bfloat16, support format: ND.
- bias: An optional input tensor for add compute. Support dtype: float32, float16, bfloat16, support format: ND.
- scales1: An optional input tensor for one of quant scale. Support dtype: float32, float16, bfloat16, support
format: ND.
- scales2: An optional input tensor for another quant scale. Support dtype: float32, float16, bfloat16, support
format: ND.
- zero_points1: An optional input tensor for one of quant offset. Support dtype: float32, float16, bfloat16,
support format: ND.
- zero_points2: An optional input tensor for another quant offset. Support dtype: float32, float16, bfloat16,
support format: ND.

## Outputs

- y1: Quantize result 1.
    A tensor. Support dtype: int8, support format: ND.
- y2: Quantize result 2.
    A tensor. Support dtype: int8, support format: ND.
- x: Describing the result of x1 + x2 + bias.
    A tensor. Support dtype: float32, float16, bfloat16, support format: ND.
- layernorm_res: Describing the result of layernorm.
    A tensor. Support dtype: float32, float16, bfloat16, support format: ND.
- out_scales1: Describing the result of dynamic quantize scales computed via scales1.
    A tensor. Support dtype: float32, support format: ND.
- out_scales2: Describing the result of dynamic quantize scales computed via scales2.
    A tensor. Support dtype: float32, support format: ND.

## Attributes

- quant_mode: An optional attribute utilized to select quant mode, can be "dynamic" or "static", the type is
string. Defaults to "dynamic".
- epsilon: An optional attribute for layer norm compute, the type is float. Defaults to 1e-5.
- additional_output: An optional attribute control whether output x valid or invalid, the type is bool. Defaults
to false, which means x output is invalid.
- div_mode: An optional attribute control static quant algorithm, the type is bool. Defaults
to true, which means scales while be divided by normlization output.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 gamma: bfloat16,float16,float32
- input3 beta: bfloat16,float16,float32
- input4 bias: bfloat16,float16,float32
- input5 scales1: bfloat16,float16,float32
- input6 scales2: bfloat16,float16,float32
- input7 zero_points1: bfloat16,float16,float32
- input8 zero_points2: bfloat16,float16,float32
- output0 y1: int8
- output1 y2: int8
- output2 x: bfloat16,float16,float32
- output3 layernorm_res: bfloat16,float16,float32
- output4 out_scales1: float32
- output5 out_scales2: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
