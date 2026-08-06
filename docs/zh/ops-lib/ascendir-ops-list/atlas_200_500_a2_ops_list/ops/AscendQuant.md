# AscendQuant

```c
REG_OP(AscendQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .REQUIRED_ATTR(scale, Float)
    .REQUIRED_ATTR(offset, Float)
    .ATTR(sqrt_mode, Bool, false)
    .ATTR(round_mode, String, "Round")
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(AscendQuant)
```

## Brief

Quantizes the input.

## Inputs

x: A tensor of type float16 or float32, specifying the input.
The format must be NC1HWC0, FRACTAL_NZ, NDC1HWC0 or ND. Shape supports 1D ~ 8D.
If "dst_type" is 29, the last dimension of the shape must be divisible by 2. 

## Outputs

y: The quantized output tensor of type int8, int4, hifloat8, float8_e5m2 or float8_e4m3fn.
The format must be NC1HWC0, FRACTAL_NZ, NDC1HWC0 or ND. Shape supports 1D ~ 8D.
Has the same format and shape as input "x". 

## Attributes

- scale: A required float32, specifying the scaling ratio.
- offset: A required float32, specifying the offset.
- sqrt_mode: An optional bool, specifying whether to perform square on "scale", either "True" or "False".
Defaults to "False".
- round_mode: An optional string, specifying the cast mode.
The value range is [Round, Floor, Ceil, Trunc, Hybrid]. Defaults to "Round".
- dst_type: An optional int32, specifying the output data type.
Defaults to "2", represents dtype "DT_INT8". "29" represents dtype "DT_INT4", "34" represents dtype "DT_HIFLOAT8",
"35" represents dtype "DT_FLOAT8_E5M2", "36" represents dtype "DT_FLOAT8_E4M3FN". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: int4,int8

## Attention Constraints

- round_mode value range is [Round, Floor, Ceil, Trunc, Hybrid].
Round: round to nearest, tie to even(c language rint). 
Floor: round to minus infinity(c language floor). 
Ceil: round to positive infinity(c language ceil). 
Trunc: round to zero(c language trunc). 
Hybrid: only valid when output dtype is hifloat8. 
The following constraints apply to products other than Ascend 950 AI Processor: 
- When format is FRACTAL_NZ, shape supports 4D ~ 8D.
- When "x" is dynamic shape, shape [-2] is not supported.
- When "x" is dynamic shape, the data type of output "y" does not support int4.
- When the format of "x" is ND, the data type of output "y" does not support int4.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
