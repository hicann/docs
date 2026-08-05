# Conv2DTranspose

```c
REG_OP(Conv2DTranspose)
    .INPUT(input_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_INT8, DT_FLOAT, DT_BF16}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_INT8, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_INT32, DT_FLOAT}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT32, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NHWC")
    .ATTR(output_padding, ListInt, {0, 0, 0, 0})
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(Conv2DTranspose)
```

## Brief

Computes the transpose of convolution 2D with respect to the input.

## Inputs

Five inputs:
- input_size: A tensor of type int32 or int64. An integer vector
representing the shape of input, where input is a 4-D tensor
[batch, height, width, channels] or [batch, channels, height, width].
Any value of input_size must be in [1, 2147483647].
- x: A tensor of type int8, float16, bfloat16, float32. 4-D with shape [batch,
out_height, out_width, out_channels] or [batch, out_channels, out_height,
out_width].
- filter: A tensor of type int8, float16, bfloat16, float32. Must have the same
type as "x".
4-D with shape [filter_height, filter_width, in_channels, out_channels].
or [out_channels, filter_height, filter_width, in_channels].
or [out_channels, in_channel, filter_height, filter_width].
In Ascend 950PR/Ascend 950DT, the filter_height and filter_width dimensions must be in [1, 2147483647],
for other products filter_height and filter_width dimensions must be in [1, 511].
The other dimensions must be in [1, 2147483647].
- bias: An optional 1D tensor of type float16, float32, int32.
 Format is "ND".
- offset_w: An optional 1D tensor of type int8 for quantized inference. Reserved.
Defaults to 0.
Currently offset_w is not supported on Atlas 200/500 A2 Inference Product,
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
and Ascend 950PR/Ascend 950DT. Reserved.
In Ascend 950PR/Ascend 950DT, the following are the supported data types and data formats:
| Tensor    | x       | filter  | bias    | y      |
|-----------|---------|---------|---------|--------|
| Data Type | float16 | float16 | float16 | float16 |
|           | float16 | float16 | float32 | float32 |
|           | bfloat16| bfloat16| float32 | bfloat16|
|           | bfloat16| bfloat16| bfloat16 | bfloat16|
|           | float32 | float32 | float32 | float32 |
|           | int8    | int8    | int32    | float16   |
| Format    | NCHW    | NCHW    | ND      | NCHW    |
|           | NHWC    | HWCN    | ND      | NHWC    |
The following are the supported data types and data formats for other products:s
| Tensor    | x       | filter  | bias    | y      |
|-----------|---------|---------|---------|--------|
| Data Type | float16 | float16 | float16 | float16 |
|           | bfloat16| bfloat16| float32 | bfloat16|
|           | float16 | float16 | float32 | float32 |
|           | float32 | float32 | float32 | float32 |
|           | int8    | int8    | int32    | int32   |
| Format    | NCHW    | NCHW    | ND      | NCHW    |
|           | NHWC    | HWCN    | ND      | NHWC    |
int8 for x and filter is not supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component.
When input x and filter is int8, a dequant or requant operator must be followed.

## Outputs

y: A tensor. A tensor of type float16, bfloat16, float32, int32, and has
 same format as input_size.
Any dimension of y shape must be in [1, 2147483647].
    out_backprop_height = (fmap_height + pad_top + pad_bottom -
                          (dilation_h * (filter_height - 1) + 1) - output_padding_height)
                          / stride_h + 1
    out_backprop_width = (fmap_width + pad_left + pad_right -
                         (dilation_w * (filter_width - 1) + 1) - output_padding_width)
                         / stride_w + 1

## Attributes

- strides: A required tuple/list of 4 integers. The stride of the sliding
window for H/W dimension. The index of H/W is the same as data_format.
The batch(N) and channels(C) dimensions must be 1.
The other values of strides must be in [1, 2147483647].
- pads: A required tuple/list of 4 integers, [top, bottom, left, right]
pads on feature map.
All dimensions must be greater than or equal to 0.
The value of groups must be in [1, 65535].
- dilations: An optional tuple/list of 4 integers, The dilation factor for each
dimension of input. Defaults to [1, 1, 1, 1]. Must be with shape
[1, 1, dilation_height, dilation_width] or [1, dilation_height, dilation_width, 1].
The value of N/C dimensions must be 1.
The width (W) and height (H) dimensions must be greater than 0.
- groups: An optional integer of blocked connections from input channels to output
channels. Defaults to 1.
The in_channels and out_channels must be divisible by groups.
The value of groups must be in [1, 65535].
- data_format: An optional string from: "NHWC", "NCHW".
Defaults to "NHWC". Specify the data format of the x and y.
- output_padding: Optional. The size will be added in the output shape.
Defaults to [0, 0, 0, 0]. The N and C dimensions must be 0.
In Ascend 950PR/Ascend 950DT, H and W have the following restrictions:
H must be less than dilation_h or stride_h,
C must be less than dilation_w or stride_w,
and H, W must be in [0, 2147483647].
Currently output_padding is not supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component.
In graph mode, only configuration to [0, 0, 0, 0] is supported.
- offset_x: Optional. Input offset_x value. Defaults to 0.
Currently offset_x is not supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component. Reserved.
Ensure offset_x within the effective range of int8 [-128, 127].
In Atlas Training Series Product, fmap or out_backprop's H and W not support 1 when
fmap_h + pad_top + pad_bottom != (filter_height - 1) * dilation_h + 1
and filter_width > fmap_width.
If filter_h = 1 and filter_w = 1, out_backprop_w * stride_h * stride_w
 < 4096. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32,int64
- input1 x: bfloat16,float8_e4m3fn,float16,float32,hifloat8
- input2 filter: bfloat16,float8_e4m3fn,float16,float32,hifloat8
- input3 bias: float32
- input4 offset_w: int8
- output0 y: bfloat16,float8_e4m3fn,float16,float32,hifloat8

## Attention Constraints

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.
Due to hardware resource restrictions,
the operator fails to be executed in scenarios of some parameter value combinations.
Analyze and rectify the fault based on the log information.
If the fault persists, visit https://www.hiascend.com/support for technical support.


---

[Back to Operator Specifications (Ascend950)](../README.md)
