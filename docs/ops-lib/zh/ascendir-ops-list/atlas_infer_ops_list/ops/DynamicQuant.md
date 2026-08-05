# DynamicQuant

```c
REG_OP(DynamicQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scales, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .OUTPUT(scale, TensorType({DT_FLOAT}))
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(DynamicQuant)
```

## Brief

Dynamic Quant. Performs pre-token symmetric dynamic quantization on input tensors.

## Inputs

- x: A Tensor. Type is:DT_FLOAT16 or DT_BF16. For Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product.
Whose shape must be greater than 1. The data format support ND.
- smooth_scales: An optional Tensor. Shape is the last dimension of x.
The data type can be FLOAT16 or BFLOAT16.
- group_index: An optional Tensor. Specifying the index of group. 1-D with shape
[E, ], the first dim of scale shape is same as the first dim of scale shape.
Must be one of the following types: int32. The format support ND. 

## Outputs

- y: A Tensor. Quantized output tensor, Shape is same as input x.
The format support ND. Type specified by dst_type, support INT4, INT8,
FLOAT8_E5M2, FLOAT8_E4M3FN, HIFLOAT8.
- scale: A Tensor. Scale used for quantization.
Type is DT_FLOAT32. The format support ND.

## Attributes

dst_type: An optional int32. Output y data type enum value.
Support DT_INT4, DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8.
Defaults to DT_INT8. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 smooth_scales: float16
- input2 group_index: int32
- output0 y: int8
- output1 scale: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
