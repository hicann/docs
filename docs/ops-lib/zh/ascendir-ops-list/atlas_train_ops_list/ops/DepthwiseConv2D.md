# DepthwiseConv2D

```c
REG_OP(DepthwiseConv2D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8, DT_FLOAT}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_INT32, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_FLOAT16, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT32, DT_FLOAT, DT_BF16, DT_HIFLOAT8}))
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(data_format, String, "NHWC")
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(DepthwiseConv2D)
```

## Brief

Computes a 2D depth-wise convolution given 4D "x", "filter" and "bias" tensors.
Like this, output = DEPTHWISECONV(x, filter) + bias.

## Inputs

- x: A required 4D tensor of input image. With the format "NHWC" which shape is
[n, h, w, in_channels] or the format "NCHW" which shape is [n, in_channels, h, w].
- filter: A required 4D tensor of convolution kernel.
With the format "HWCN" which shape is [kernel_h, kernel_w, in_channels, channel_multiplier]
or the format "NCHW" which shape is [channel_multiplier, in_channels, kernel_h, kernel_w].
- bias: An optional 1D tensor of additive biases to the outputs.
The data is stored in the order of: [in_channels * channel_multiplier].
- offset_w: An optional quantitative offset tensor. Reserved.
The following are the supported data types and data formats (except IPV350 and Ascend 950 AI Processor):
| Tensor    | x        | filter   | bias     | y        |
| :-------: | :------: | :------: | :------: | :------: |
| Data Type | float16  | float16  | float16  | float16  |
|           | float16  | float16  | float16  | float32  |
|           | bfloat16 | bfloat16 | bfloat16 | bfloat16 |
|           | bfloat16 | bfloat16 | bfloat16 | float32  |
|           | float32  | float32  | float32  | float32  |
|           | int8     | int8     | int32    | int32    |
| Format    | NCHW     | NCHW     | ND       | NCHW     |
|           | NHWC     | HWCN     | ND       | NHWC     |
|           | NCHW     | HWCN     | ND       | NCHW     |
The following are the supported data types and data formats for IPV350:
| Tensor    | x       | filter  | bias    | y       |
| :-------: | :-----: | :-----: | :-----: | :-----: |
| Data Type | int16   | int8    | int32   | int32   |
|           | int8    | int8    | int32   | int32   |
| Format    | NCHW    | NCHW    | ND      | NCHW    |
|           | NHWC    | HWCN    | ND      | NHWC    |
The following are the supported data types and data formats for Ascend 950 AI Processor:
| Tensor    | x        | filter   | bias     | y        |
| :-------: | :------: | :------: | :------: | :------: |
| Data Type | float16  | float16  | float16  | float16  |
|           | bfloat16 | bfloat16 | bfloat16 | bfloat16 |
|           | float32  | float32  | float32  | float32  |
|           | hifloat8 | hifloat8 | float32  | hifloat8 |
| Format    | NCHW     | NCHW     | ND       | NCHW     |
|           | NHWC     | HWCN     | ND       | NHWC     |

## Outputs

y: A 4D tensor of output feature map.
With the format "NHWC" which shape is [n, out_height, out_width, in_channels * channel_multiplier]
or the format "NCHW" which shape is [n, in_channels * channel_multiplier, out_height, out_width].
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
When the format is "NHWC", its shape is [1, stride_h, stride_w, 1],
when the format is "NCHW", its shape is [1, 1, stride_h, stride_w].
- dilations: Optional. A list of 4 integers. The dilation factor for each
dimension of input. The dimension order is determined by the data format of
"x". The n and in_channels dimensions must be set to 1.
When the format is "NHWC", its shape is [1, dilation_h, dilation_w, 1],
when the format is "NCHW", its shape is [1, 1, dilation_h, dilation_w]. Defaults to [1, 1, 1, 1].
- pads: Required. A list of 4 integers. The number of pixels to add to each
(pad_top, pad_bottom, pad_left, pad_right) side of the input.
- data_format: Optional. It is a string represents input's data format.
Defaults to "NHWC". Reserved.
- offset_x: Optional. An integer of type int32. It means offset in quantization algorithm
and is used for filling in pad values. Ensure that the output is within the
effective range. Defaults to 0. Reserved.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,int8
- input1 filter: float16,int8
- input2 bias: float16,float32,int32
- input3 offset_w: float16,int8
- output0 y: float16,float32,int32

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
- If any dimension of x/filter/bias/y shape exceeds max
int32(2147483647), the product of each dimension of x/filter/bias/y
shape exceeds max int32(2147483647) or the value of strides/pads/dilations/offset_x
exceeds the range in the above table, the correctness of the operator cannot be guaranteed. 
In Ascend 950 AI Processor: If any dimension of x/filter/bias/y shape exceeds max
1000000, the product of each dimension of x/filter/bias/y
shape exceeds max int32(2147483647) or the value of strides/pads/dilations/offset_x
exceeds the range in the above table, the correctness of the operator cannot be guaranteed.
- When the specifications of the DepthwiseConv2D exceeds the constraints mentioned above,
a timeout AI Core error may be reported.

## Quantization supported or not

Yes

## Third-party framework compatibility

- Compatible with the TensorFlow operator "depthwise_conv2d".
- Compatible with the Caffe operator "DepthwiseConvolution".


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
