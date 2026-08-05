# DynamicQuantV2

```c
REG_OP(DynamicQuantV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scales, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .OUTPUT(scale, TensorType({DT_FLOAT}))
    .OUTPUT(offset, TensorType({DT_FLOAT}))
    .ATTR(dst_type, Int, DT_INT8)
    .ATTR(is_symmetrical, Bool, false)
    .ATTR(quant_mode, String, "pertoken")
    .ATTR(dst_type_max, Float, 0.0)
    .OP_END_FACTORY_REG(DynamicQuantV2)
```

## Brief

Dynamic Quant V2. Performs pre-token/per-tensor asymmetric dynamic quantization on input tensors.

## Inputs

- x: A tensor. Type is:DT_FLOAT16 or DT_BF16. For Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
and Atlas A3 Training Series Product/Atlas A3 Inference Series Product.
Whose shape must be greater than 1. The data format support ND.
- smooth_scales: An optional tensor.
When group_index is null, shape is 1 Dims. Dim[0] is the last dimension of x.
When group_index is not null, shape is 2 Dims. Dim[0] is the expert num(E). E must be not greater than 1024. Dim[1] is the last dimension of x.
The data type can be FLOAT16 or BFLOAT16.
The data type must be the same as that of x. The data format support ND.
- group_index: An optional tensor. Specifying the index of group. 1-D with shape
[E, ].
The first dim of group_index shape is same as the first dim of smooth_scales shape.
Must be one of the following types: int32. The format support ND.
If group_index is not null, smooth_scales must be not null. 

## Outputs

- y: A tensor. Quantized output tensor, Shape is same as input x. If y dtype is int4, x last dim must be divisible by 2.
The format support ND. Type specified by dst_type, support INT4, INT8,
FLOAT8_E5M2, FLOAT8_E4M3FN, HIFLOAT8.
- scale: A tensor. Scale used for quantization.
When quant_mode is "pertoken", shape is the same as the shape of x after removing the last dimension.
When quant_mode is "pertensor", shape is (1,).
Type is DT_FLOAT32. The format support ND.
- offset: A tensor. Offset used for quantization. Shape is the same as the shape of scale.
Type is DT_FLOAT32. The format support ND. Shape is same as scale. 

## Attributes

- dst_type: An optional attribute of type int. Declare the output dtype.
Support DT_INT4, DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8.
Defaults to DT_INT8.
- is_symmetrical: An optional attribute of type bool. Select whether to be symmetrical.
Defaults to false.
- quant_mode: An optional attribute of type string. Specifies the mode of quantization.
Support "pertoken", "pertensor". Defaults to "pertoken".
- dst_type_max: An optional attribute of type float. Specifies the range of quantized output.
Only effective when dst_type is 34(hifloat8), supporting values 0, 15, 56, 224, 32768.
Defaults to 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 smooth_scales: bfloat16,float16
- input2 group_index: int32
- output0 y: int4,int8
- output1 scale: float32
- output2 offset: float32

## Attention Constraints

Warning: E should to be be not greater than multiplication result of x Dims after removing the last dimension(S).
The value of group_index should to be increasing, ranging from 0 to S. The last value is should to be S. Otherwise
the result is meaningless.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
