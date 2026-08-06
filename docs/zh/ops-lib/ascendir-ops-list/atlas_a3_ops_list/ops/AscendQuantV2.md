# AscendQuantV2

```c
REG_OP(AscendQuantV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .ATTR(sqrt_mode, Bool, false)
    .ATTR(round_mode, String, "round")
    .ATTR(dst_type, Int, DT_INT8)
    .ATTR(axis, Int, -1)
    .OP_END_FACTORY_REG(AscendQuantV2)
```

## Brief

Quantizes the input, scale/offset support broadcasting operations. 

## Inputs

- x: A required Tensor. Must be one of the following types: float16,
float32, bfloat16. The format support ND. Shape support 1D ~ 8D. Specifying the input.
- scale: A required Tensor. Must be one of the following types: float16,
float32, bfloat16. The format support ND. Shape support 1D ~ 8D. Specifying the scaling ratio.
- offset: An optional Tensor. Must be one of the following types: float16,
float32, bfloat16. The format support ND. Shape support 1D ~ 8D. Shape is same as "scale". Specifying the offset. 

## Outputs

y: The quantized output tensor of type int8, int4, hifloat8, float8_e5m2 or float8_e4m3fn. The format support ND.
Shape support 1D ~ 8D. Has the same shape as input "x". Dtype should be the same as the attribute dst_type. 

## Attributes

- sqrt_mode: An optional bool, specifying whether to perform square
on "scale", either "True" or "False". Defaults to "False".
- round_mode: An optional string, specifying the cast type.
The value range is ["round", "floor", "ceil", "trunc", "hybrid"]. Defaults to "round".
- dst_type: An optional int32, specifying the output data type.
The value range is [DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN]. Defaults to DT_INT8.
- axis: An optional int32, describes which dimension of the input tensor x to be processed. Default is -1.
Suppose x's dim number is D, axis should be in [-D, D - 1].
if D > 2, axis should be -1, -2, D-2 or D-1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 scale: bfloat16,float16,float32
- input2 offset: bfloat16,float16,float32
- output0 y: int4,int8

## Attention Constraints

- When dst_type is DT_FLOAT8_E5M2 or DT_FLOAT8_E4M3FN, round_mode only supports "round".
- When dst_type is DT_HIFLOAT8, round_mode supports "round" and "hybrid".
- When dst_type is other value, round_mode supports "round", "floor", "ceil" and "trunc".
- If dst_type is DT_INT4, the last dimension of the shape must be divisible by 2.
- The dtype of x, scale and offset must be same.
- scale and offset's shape should be the same.
- scale and offset's dimension number should be 1 or the same with x.
- When scale's dimension number is 1, it should be 1 or the same with the dimension specified by attributes[axis] of
input x.
- When scale's dimension number is the same with x, the dimension specified by attributes[axis] shoule be 1 or the
same with x's, others should be 1. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
