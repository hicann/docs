# QuantConv3D

```c
REG_OP(QuantConv3D)
    .INPUT(x, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(filter, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(scale, TensorType({DT_UINT64, DT_INT64}))
    .OPTIONAL_INPUT(bias, TensorType({DT_INT32, DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .REQUIRED_ATTR(dtype, Int)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(pads, ListInt, {0, 0, 0, 0, 0, 0})
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NCDHW")
    .ATTR(offset_x, Int, 0)
    .ATTR(round_mode, String, "rint")
    .ATTR(pad_mode, String, "SPECIFIC")
    .OP_END_FACTORY_REG(QuantConv3D)
```

## Brief

Computes a 3D convolution with 5D "x", "filter" and "bias" tensors,
and then executes a per-channel dequant operation with "scale" tensors.
Like this, output = (CONV(x, filter) + bias) * scale.

## Inputs

- x: A required 5D tensor of input image. With the format "NDHWC" which shape is
[n, d, h, w, in_channels] or the format "NCDHW" which shape is [n, in_channels, d, h, w].
- filter: A required 5D tensor of convolution kernel.
With the format "DHWCN" which shape is [kernel_d, kernel_h, kernel_w, in_channels / groups, out_channels]
or the format "NCDHW" which shape is [out_channels, in_channels / groups, kernel_d, kernel_h, kernel_w].
- scale: A required 1D tensor of scaling factors. The data is stored in the order of: [out_channels].
- bias: An optional 1D tensor of additive biases to the outputs.
The data is stored in the order of: [out_channels].
- offset: An optional quantitative offset tensor. Reserved.
The following are the supported data types and data formats (for Ascend 950 AI Processor):
| Tensor    | x           | filter      | scale        | bias    | offset  | y                                   |
| :-------: | :---------: | :---------: | :----------: | :------:| :------:| :---------------------------------: |
| Data Type | int8        | int8        | uint64/int64 | int32   | float32 | float16                             |
|           | float8_e4m3 | float8_e4m3 | uint64/int64 | float32 | float32 | float32/float16/bfloat16/float8_e4m3|
|           | hifloat8    | hifloat8    | uint64/int64 | float32 | float32 | float32/float16/bfloat16/hifloat8   |
| Format    | NCDHW       | NCDHW       | ND           | ND      | ND      | NCDHW                               |

## Outputs

y: A 5D tensor of output feature map.
With the format "NDHWC", the data is stored in the order of: [n, out_depth, out_height, out_width, out_channels]
or the format "NCDHW", the data is stored in the order of: [n, out_channels, out_depth, out_height, out_width].
    out_depth  = (d + pad_head + pad_tail -
                  (dilation_d * (kernel_d - 1) + 1))
                 / stride_d + 1
    out_height = (h + pad_top + pad_bottom -
                  (dilation_h * (kernel_h - 1) + 1))
                 / stride_h + 1
    out_width = (w + pad_left + pad_right -
                 (dilation_w * (kernel_w - 1) + 1))
                / stride_w + 1

## Attributes

- dtype: Required. A integer of type int8. It means output's dtype.
- strides: Required. A list of 5 integers. The stride of the sliding window
for each dimension of input. The dimension order is determined by the data
format of "x". The n and in_channels dimensions must be set to 1.
When the format is "NDHWC", its shape is [1, stride_d, stride_h, stride_w, 1],
when the format is "NCDHW", its shape is [1, 1, stride_d, stride_h, stride_w].
- pads: Required. A list of 6 integers. The number of pixels to add to each
(pad_head, pad_tail, pad_top, pad_bottom, pad_left, pad_right) side of the input.
- dilations: Optional. A list of 5 integers. The dilation factor for each
dimension of input. The dimension order is determined by the data format of
"x". The n and in_channels dimensions must be set to 1.
When the format is "NDHWC", its shape is [1, dilation_d, dilation_h, dilation_w, 1],
when the format is "NCDHW", its shape is [1, 1, dilation_d, dilation_h, dilation_w]. Defaults to [1, 1, 1, 1].
- groups: Optional. An integer of type int32. The number of groups
in group convolution. In_channels and out_channels must both be divisible by "groups". Defaults to 1.
- data_format: Optional. It is a string represents input's data format.
Defaults to "NCDHW". Reserved.
- offset_x: Optional. An integer of type int32. It means offset in quantization algorithm
and is used for filling in pad values. Ensure that the output is within the
effective range. Defaults to 0. Reserved.
- round_mode: Optional. Defaults to "rint". It is rounding mode of calculation.
If output's data type is hifloat8, round_mode can be set to 'round'. Otherwise, it can be set to 'rint'.
- pad_mode: Optional. An optional string parameter, indicating the mode of pad.
It must be "SPECIFIC" or "SAME" or "VALID". Defaults to "SPECIFIC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float8_e4m3fn,hifloat8,int8
- input1 filter: float8_e4m3fn,hifloat8,int8
- input2 scale: int64,uint64
- input3 bias: float32,int32
- input4 offset: float32
- output0 y: bfloat16,float8_e4m3fn,float16,float32,hifloat8

## Attention Constraints

- The following value range restrictions must be met:
| Name             | Field                | Scope        |
| :--------------: | :------------------: | :----------: |
| x size           | n                    | [1, 1000000] |
|                  | in_channels          | [1, 1000000] |
|                  | d                    | [1, 1000000] |
|                  | h                    | [1, 100000]  |
|                  | w                    | [1, 4096]    |
| filter size      | out_channels         | [1, 1000000] |
|                  | in_channels / groups | [1, 1000000] |
|                  | kernel_d             | [1, 1000000] |
|                  | kernel_h             | [1, 511]     |
|                  | kernel_w             | [1, 511]     |
| scale size       | out_channels         | [1, 1000000] |
| bias size        | out_channels         | [1, 1000000] |
| offset size      | out_channels         | [1, 1000000] |
| strides          | stride_d             | [1, 1000000] |
|                  | stride_h             | [1, 63]      |
|                  | stride_w             | [1, 63]      |
| pads             | pad_head             | [0, 1000000] |
|                  | pad_tail             | [0, 1000000] |
|                  | pad_top              | [0, 255]     |
|                  | pad_bottom           | [0, 255]     |
|                  | pad_left             | [0, 255]     |
|                  | pad_right            | [0, 255]     |
| dilations        | dilation_d           | [1, 1000000] |
|                  | dilation_h           | [1, 255]     |
|                  | dilation_w           | [1, 255]     |
| groups           | -                    | [1, 65535]   |
| data_format      | -                    | ["NDHWC", "NCDHW"] |
| offset_x         | -                    | [-128, 127]  |
| pad_mode         | -                    | ["SPECIFIC", "SAME", "VALID"] |
| enable_hf32      | -                    | [true, false] |
- The W dimension of the input image supports cases exceeding 4096, but it may
cause compilation errors.
- If any dimension of x/filter/scale/bias/offset/y shape exceeds max int32 minus one (2147483646),
the product of each dimension of x/filter/scale/bias/offset/y shape exceeds max int32 minus one (2147483646) or
the value of strides/pads/dilations/groups/data_format/offset_x/pad_mode/enable_hf32 exceeds the range
in the above table, the correctness of the operator cannot be guaranteed.

## Quantization supported or not

Yes


---

[Back to Operator Specifications (Ascend950)](../README.md)
