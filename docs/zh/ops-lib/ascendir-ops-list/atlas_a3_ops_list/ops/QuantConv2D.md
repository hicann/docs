# QuantConv2D

```c
REG_OP(QuantConv2D)
    .INPUT(x, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(filter, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(scale, TensorType({DT_UINT64, DT_INT64}))
    .OPTIONAL_INPUT(bias, TensorType({DT_INT32, DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .REQUIRED_ATTR(dtype, Int)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NHWC")
    .ATTR(offset_x, Int, 0)
    .ATTR(round_mode, String, "rint")
    .OP_END_FACTORY_REG(QuantConv2D)
```

## Brief

Computes a 2D convolution given 4D "x", "filter" and "bias" tensors
and then executes a per-channel dequant operation with "scale" tensors.
Like this, output = (CONV(x, filter) + bias) * scale.

## Inputs

- x: A required 4D tensor of input image. With the format "NHWC" which shape is
[n, h, w, in_channels] or the format "NCHW" which shape is [n, in_channels, h, w].
- filter: A required 4D tensor of convolution kernel.
With the format "HWCN" which shape is [kernel_h, kernel_w, in_channels / groups, out_channels]
or the format "NCHW" which shape is [out_channels, in_channels / groups, kernel_h, kernel_w].
- scale: A required 1D tensor of scaling factors. The data is stored in the order of: [out_channels].
- bias: An optional 1D tensor of additive biases to the outputs.
The data is stored in the order of: [out_channels].
- offset: An optional quantitative offset tensor. Reserved.
The following are the supported data types and data formats
(for Atlas Inference Series Product, Atlas Training Series Product,
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component and
Atlas A3 Training Series Product/Atlas A3 Inference Series Product)
| Tensor    | x       | filter  | scale         | bias    | offset  | y       |
| :-------: | :-----: | :-----: | :-----------: | :-----: | :-----: | :-----: |
| Data Type | int8    | int8    | uint64/int64  | int32   | float32 | float16 |
| Format    | NCHW    | NCHW    | ND            | ND      | ND      | NCHW    |
|           | NCHW    | HWCN    | ND            | ND      | ND      | NCHW    |
|           | NHWC    | HWCN    | ND            | ND      | ND      | NHWC    |
The following are the supported data types and data formats (for Ascend 950 AI Processor):
| Tensor    | x           | filter      | scale        | bias    | offset  | y                                   |
| :-------: | :---------: | :---------: | :----------: | :------:| :------:| :---------------------------------: |
| Data Type | int8        | int8        | uint64/int64 | int32   | float32 | float16                             |
|           | float8_e4m3 | float8_e4m3 | uint64/int64 | float32 | float32 | float32/float16/bfloat16/float8_e4m3|
|           | hifloat8    | hifloat8    | uint64/int64 | float32 | float32 | float32/float16/bfloat16/hifloat8   |
| Format    | NCHW        | NCHW        | ND           | ND      | ND      | NCHW                                |

## Outputs

y: A 4D tensor of output feature map.
With the format "NHWC" which shape is [n, out_height, out_width, out_channels]
or the format "NCHW" which shape is [n, out_channels, out_height, out_width].
    out_height = (h + pad_top + pad_bottom -
                  (dilation_h * (kernel_h - 1) + 1))
                 / stride_h + 1
    out_width = (w + pad_left + pad_right -
                 (dilation_w * (kernel_w - 1) + 1))
                / stride_w + 1

## Attributes

- dtype: Required. A integer of type int8. It means output's dtype.
- strides: Required. A list of 4 integers. The stride of the sliding window
for each dimension of input. The dimension order is determined by the data
format of "x". The n and in_channels dimensions must be set to 1.
When the format is "NHWC", its shape is [1, stride_h, stride_w, 1],
when the format is "NCHW", its shape is [1, 1, stride_h, stride_w].
- pads: Required. A list of 4 integers. The number of pixels to add to each
(pad_top, pad_bottom, pad_left, pad_right) side of the input.
- dilations: Optional. A list of 4 integers. The dilation factor for each
dimension of input. The dimension order is determined by the data format of
"x". The n and in_channels dimensions must be set to 1.
When the format is "NHWC", its shape is [1, dilation_h, dilation_w, 1],
when the format is "NCHW", its shape is [1, 1, dilation_h, dilation_w]. Defaults to [1, 1, 1, 1].
- groups: Optional. An integer of type int32. The number of groups
in group convolution. In_channels and out_channels must both be divisible by "groups". Defaults to 1.
- data_format: Optional. It is a string represents input's data format.
Defaults to "NHWC". Reserved.
- offset_x: Optional. An integer of type int32. It means offset in quantization algorithm
and is used for filling in pad values. Ensure that the output is within the
effective range. Defaults to 0. Reserved.
- round_mode: Optional. Defaults to "rint". It is rounding mode of calculation.
If output's dtype is hifloat8, round_mode can be set to 'round'. Otherwise, it can be set to 'rint'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int8
- input1 filter: int8
- input2 scale: int64,uint64
- input3 bias: int32
- input4 offset: float32
- output0 y: float16

## Attention Constraints

- The following value range restrictions must be met:
| Name             | Field      | Scope       |
| :--------------: | :--------: | :---------: |
| x size           | h          | [1, 100000] |
|                  | w          | [1, 4096]   |
| filter size      | kernel_h   | [1, 511]    |
|                  | kernel_w   | [1, 511]    |
| strides          | stride_h   | [1, 63]     |
|                  | stride_w   | [1, 63]     |
| pads             | pad_top    | [0, 255]    |
|                  | pad_bottom | [0, 255]    |
|                  | pad_left   | [0, 255]    |
|                  | pad_right  | [0, 255]    |
| dilations        | dilation_h | [1, 255]    |
|                  | dilation_w | [1, 255]    |
| offset_x         | -          | [-128, 127] |
- The w dimension of the input image supports cases exceeding 4096, but it may
cause compilation errors.
- If any dimension of x/filter/bias/scale/offset/y shape exceeds max
int32(2147483647), the product of each dimension of x/filter/bias/scale/offset/y
shape exceeds max int32(2147483647) or the value of strides/pads/dilations/offset_x
exceeds the range in the above table, the correctness of the operator cannot be guaranteed. 
In Ascend 950 AI Processor: If any dimension of x/filter/bias/scale/offset/y shape exceeds max
1000000, the product of each dimension of x/filter/bias/scale/offset/y
shape exceeds max int32(2147483647) or the value of strides/pads/dilations/offset_x
exceeds the range in the above table, the correctness of the operator cannot be guaranteed.

## Quantization supported or not

Yes


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
