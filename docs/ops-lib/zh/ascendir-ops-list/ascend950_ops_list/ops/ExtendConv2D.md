# ExtendConv2D

```c
REG_OP(ExtendConv2D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OPTIONAL_INPUT(scale0, TensorType({DT_INT64, DT_UINT64}))
    .OPTIONAL_INPUT(relu_weight0, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(clip_value0, TensorType({DT_FLOAT16, DT_INT8, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(scale1, TensorType({DT_INT64, DT_UINT64}))
    .OPTIONAL_INPUT(relu_weight1, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(clip_value1, TensorType({DT_FLOAT16, DT_INT8, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .OUTPUT(y0, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .OUTPUT(y1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(pads, ListInt, {0, 0, 0, 0})
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NCHW")
    .ATTR(offset_x, Int, 0)
    .ATTR(round_mode, String, "rint")
    .ATTR(pad_mode, String, "SPECIFIC")
    .ATTR(enable_hf32, Bool, false)
    .ATTR(enable_relu0, Bool, false)
    .ATTR(enable_relu1, Bool, false)
    .ATTR(dual_output, Bool, false)
    .ATTR(dtype0, Int, -1)
    .ATTR(dtype1, Int, -1)
    .OP_END_FACTORY_REG(ExtendConv2D)
```

## Brief

ExtendConv2D computes a 2D convolution + fixpipe fused operator.

## Inputs

- x: A required 4D tensor of input image. With the format "NCHW" which shape is
[n, in_channels, h, w].
- filter: A required 4D tensor of convolution kernel.
With the format "NCHW" which shape is [out_channels, in_channels / groups, kernel_h, kernel_w].
- bias: An optional 1D tensor of additive biases to the outputs.
The data is stored in the order of: [out_channels].
- offset_w: An optional quantitative offset tensor. Reserved.
- scale0: An optional 1D tensor. Quantization/dequantization/weighting parameter corresponding to
the first output, which is of the channelwise type.
- relu_weight0: An optional 1D tensor. Indicates the relu slope parameter corresponding to the
first output, which is of the scalar type or channelwise type.
- clip_value0: An optional 1D tensor. Truncated value of clip relu corresponding to the first output.
The value is of the scalar type.
- scale1: An optional 1D tensor. Quantization/dequantization/weighting parameter corresponding to
the second output, which is of the scalar type or channelwise type.
- relu_weight1: An optional 1D tensor. Quantization/dequantization/weighting parameter corresponding to
the second output, which is of the scalar type or channelwise type.
- clip_value1: An optional 1D tensor. Truncated value of clip relu corresponding to the second output.
The value is of the scalar type.
The following are the supported data types and data formats:
| Tensor    | x        | filter   | bias    | scale0, scale1  | relu_weight0, relu_weight1 | clip_value0, clip_value1 | y0, y1                             |
| :-------: | :------: | :------: | :-----: | :-------------: | :------------------------: | :----------------------: | :--------------------------------: |
| Data Type | int8     | int8     | int32   | uint64 or int64 | float32                    | int8                     | float16 or int8                    |
|           | hifloat8 | hifloat8 | float32 | uint64 or int64 | float32                    | hifloat8                 | float32, float16, bfloat16 or hifloat8|
|           | float8   | float8   | float32 | uint64 or int64 | float32                    | float8                   | float32, float16, bfloat16 or float8_e4m3|
| Format    | NCHW     | NCHW     | ND      | ND              | ND                         | ND                       | NCHW                               |
| Tensor    | x        | filter   | bias    | scale0, scale1  | relu_weight0, relu_weight1 | clip_value0, clip_value1 | y0, y1             |
| :-------: | :------: | :------: | :-----: | :-------------: | :------------------------: | :----------------------: | :---------------: |
| Data Type | int8     | int8     | int32   | uint64 or int64 | float32                    | int8                     | float16 or int8    |
| Format    | NHWC     | HWCN     | ND      | ND              | ND                         | ND                       | NHWC               |
The following are the supported data types and data formats for MC62:
| Tensor    | x        | filter                   | bias    | scale0, scale1  | relu_weight0, relu_weight1 | clip_value0, clip_value1 | y0, y1          |
| :-------: | :------: | :----------------------: | :-----: | :-------------: | :------------------------: | :----------------------: | :-------------: |
| Data Type | int8     | int8                     | int32   | uint64 or int64 | float32                    | float16 or int8          | float16 or int8 |
|           | float16  | int8                     | int32   | uint64 or int64 | float32                    | float16 or int8          | float16 or int8 |
|           | float16  | float16                  | float16 | uint64 or int64 | float32                    | float16                  | float16         |
| Format    | NCHW     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | ND              | ND                         | ND                       | NCHW            |
|           | NCHW     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | ND              | ND                         | ND                       | NHWC            |
|           | NHWC     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | ND              | ND                         | ND                       | NCHW            |
|           | NHWC     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | ND              | ND                         | ND                       | NHWC            |
Note: When filter format is FZ_C04, only x, filter and bias dtype all being float16 is supported.
Note: clip_value0 and y0 must have the same dtype, clip_value1 and y1 must have the same dtype.

## Outputs

- y0: The first output of ExtendConv2D. A 4D Tensor of output feature map. Has the same type as "x".
With the format "NCHW", the data is stored in the order of: [n, out_channels, out_height, out_width].
- y1: The second output of ExtendConv2D. A 4D Tensor of output feature map. Has the same type as "x".
With the format "NCHW", the data is stored in the order of: [n, out_channels, out_height, out_width].
    out_height = (h + pad_top + pad_bottom -
                  (dilation_h * (kernel_h - 1) + 1))
                 / stride_h + 1
    out_width = (w + pad_left + pad_right -
                 (dilation_w * (kernel_w - 1) + 1))
                / stride_w + 1

## Attributes

- strides: Required. A list of 4 integers. The stride of the sliding window
for each dimension of input. The dimension order is determined by the data
format of "x". The n and in_channels dimensions must be set to 1.
When the format is "NCHW", its shape is [1, 1, stride_h, stride_w].
- pads: Optional. A list of 4 integers. The number of pixels to add to each
(pad_top, pad_bottom, pad_left, pad_right). Defaults to [0, 0, 0, 0].
- dilations: Optional. A list of 4 integers. The dilation factor for each
dimension of input. The dimension order is determined by the data format of
"x". The n and in_channels dimensions must be set to 1.
When the format is "NCHW", its shape is [1, 1, dilation_h, dilation_w]. Defaults to [1, 1, 1, 1].
- groups: Optional. An integer of type int32. The number of groups
in group convolution. In_channels and out_channels must both be divisible by "groups". Defaults to 1.
- data_format: Optional. It is a string representing x's data format.
Defaults to "NCHW".
- offset_x: Optional. An integer of type int32. It means offset in quantization algorithm
and is used for filling in pad values. Ensure that the output is within the
effective range. Defaults to 0.
- round_mode: Rounding mode used in quantization.
If output's dtype is hifloat8, round_mode can be set to "round". Otherwise, it can be set to "rint".
Defaults to "rint".
- pad_mode: Optional. A string parameter, indicating the mode of pad.
It must be "SPECIFIC" or "SAME" or "VALID" or "SAME_UPPER" or "SAME_LOWER". Defaults to "SPECIFIC".
- enable_hf32: Optional. A bool for ExtendConv2D. If True, enable hf32 calculation. Defaults to false.
If False, disable hf32 calculation.
- enable_relu0: Optional. Indicates whether relu is enabled for the first output. Defaults to false.
If False, relu is disabled for the first output.
- enable_relu1: Optional. Indicates whether relu is enabled for the second output. Defaults to false.
If False, relu is disabled for the second output.
- dual_output: Optional. Indicates whether dual outputs are used. Defaults to false.
When dual_output is false, ExtendConv2D only has output y0. When dual_output is true,
ExtendConv2D has output y0 and y1.
- dtype0: Optional. An integer of type int8. It means the dtype of output y0.
Support list is [-1(Default), 0(DT_FLOAT), 1(DT_FLOAT16), 2(DT_INT8), 27(DT_BF16),
34(DT_HIFLOAT8), 36(DT_FLOAT8_E4M3FN)]. Defaults to -1, means the dtype is the same as x.
- dtype1: Optional. An integer of type int8. It means the dtype of output y1.
Support list is [-1(Default), 0(DT_FLOAT), 1(DT_FLOAT16), 2(DT_INT8), 27(DT_BF16),
34(DT_HIFLOAT8), 36(DT_FLOAT8_E4M3FN)]. Defaults to -1, means the dtype is the same as x. Must be -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float8_e4m3fn,float16,hifloat8,int8
- input1 filter: float8_e4m3fn,float16,hifloat8,int8
- input2 bias: float16,float32,int32
- input3 offset_w: int8
- input4 scale0: int64,uint64
- input5 relu_weight0: float32
- input6 clip_value0: bfloat16,float8_e4m3fn,float16,float32,hifloat8,int8
- input7 scale1: int64,uint64
- input8 relu_weight1: float32
- input9 clip_value1: bfloat16,float8_e4m3fn,float16,float32,hifloat8,int8
- output0 y0: bfloat16,float8_e4m3fn,float16,float32,hifloat8,int8
- output1 y1: bfloat16,float8_e4m3fn,float16,float32,hifloat8,int8

## Attention Constraints

- The following value range restrictions must be met:
| Name              | Field                | Scope        |
| :---------------: | :------------------: | :----------: |
| x size            | n                    | [1, 1000000] |
|                   | in_channels          | [1, 1000000] |
|                   | h                    | [1, 100000]  |
|                   | w                    | [1, 4096]    |
| filter size       | out_channels         | [1, 1000000] |
|                   | in_channels / groups | [1, 1000000] |
|                   | kernel_h             | [1, 511]     |
|                   | kernel_w             | [1, 511]     |
| bias size         | out_channels         | [1, 1000000] |
| offset_w size     | out_channels or 1    | [1, 1000000] |
| scale0 size       | out_channels or 1    | [1, 1000000] |
| relu_weight0 size | out_channels or 1    | [1, 1000000] |
| clip_value0 size  | out_channels or 1    | [1, 1000000] |
| scale1 size       | out_channels or 1    | [1, 1000000] |
| relu_weight1 size | out_channels or 1    | [1, 1000000] |
| clip_value1 size  | out_channels or 1    | [1, 1000000] |
| strides           | stride_h             | [1, 63]      |
|                   | stride_w             | [1, 63]      |
| pads              | pad_top              | [0, 255]     |
|                   | pad_bottom           | [0, 255]     |
|                   | pad_left             | [0, 255]     |
|                   | pad_right            | [0, 255]     |
| dilations         | dilation_h           | [1, 255]     |
|                   | dilation_w           | [1, 255]     |
| groups            | -                    | [1, 65535]   |
| data_format       | -                    | ["NCHW"] |
| offset_x          | -                    | [-128, 127]  |
| round_mode        | -                    | ["rint", "round"] |
| pad_mode          | -                    | ["SPECIFIC", "SAME", "VALID", "SAME_UPPER", "SAME_LOWER"] |
| enable_hf32       | -                    | [true, false] |
| enable_relu0      | -                    | [true, false] |
| enable_relu1      | -                    | [true, false] |
| dual_output       | -                    | [true, false] |
- The w dimension of the input image supports cases exceeding 4096, but it may
cause compilation errors.
- If any dimension of x/filter/bias/offset_w/scale0/relu_weight0/clip_value0/scale1/relu_weight1/clip_value1/y
shape exceeds max 1000000, the product of each dimension of x/filter/bias/offset_w/y
shape exceeds max int32(2147483647) or the value of
strides/pads/dilations/groups/data_format/offset_x/pad_mode/enable_hf32
exceeds the range in the above table, the correctness of the operator cannot be guaranteed.


---

[Back to Operator Specifications (Ascend950)](../README.md)
