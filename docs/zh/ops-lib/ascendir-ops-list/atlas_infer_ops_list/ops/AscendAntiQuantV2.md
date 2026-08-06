# AscendAntiQuantV2

```c
REG_OP(AscendAntiQuantV2)
    .INPUT(x, TensorType({DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(scale, TensorType({DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .ATTR(dst_type, Int, DT_FLOAT16)
    .ATTR(sqrt_mode, Bool, false)
    .OP_END_FACTORY_REG(AscendAntiQuantV2)
```

## Brief

Anti quantizes the input. 

## Inputs

- x: A required Tensor. Must be one of the following types: int8, int4, hifloat8, float8_e5m2, float8_e4m3.
The format support ND. Shape support 1D ~ 8D. Specifying the input.
- scale: A required Tensor. Must be one of the following types: float32, bfloat16.
The format support ND. Shape support 1D ~ 8D. Specifying the scaling ratio.
- offset: An optional Tensor. Must be one of the following types: float32, bfloat16.
The format support ND. Shape support 1D ~ 8D. Shape and dataType is same as "scale". Specifying the offset. 

## Outputs

y: The dequantized output tensor of type float16 or bfloat16. The format support ND.
Shape support 1D ~ 8D. Has the same shape as input "x". Dtype should be the same as the attribute dst_type. 

## Attributes

- dst_type: An optional int32, specifying the output data type. Defaults to "DT_FLOAT16".
- sqrt_mode: An optional bool, specifying whether to perform square root on "scale", either "true" or "false".
Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int8
- input1 scale: float32
- input2 offset: float32
- output0 y: float16

## Attention Constraints

- When dst_type of x is DT_INT4, the last axis of its shape is even.
# @li When the data type of x is DT_HIFLOAT8, DT_FLOAT8_E5M2, or DT_FLOAT8_E4M3, scale is only supported for DT_FLOAT.
# @li When the data type of x is DT_HIFLOAT8, DT_FLOAT8_E5M2, or DT_FLOAT8_E4M3, sqrt_mode must be "false".
- The dimensionality of scale must match that of x, or be 1-dimensional. The shape of scale must satisfy the
following constraints: 
- If x is one-dimensional, the shape of scale must be [1] or the same as x.
- If scale is one-dimensional, its size must be either 1, x[-1] or x[-2].
# - If scale is multi-dimensional, it can have at most one axis that is not 1, and that axis must be the -1 or -2 axis
of x.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
