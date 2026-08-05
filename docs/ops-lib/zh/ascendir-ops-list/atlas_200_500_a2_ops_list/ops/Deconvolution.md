# Deconvolution

```c
REG_OP(Deconvolution)
    .INPUT(x, TensorType({DT_FLOAT16, DT_INT8}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_INT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT32}))
    .ATTR(strides, ListInt, {1, 1})
    .ATTR(pads, ListInt, {0, 0, 0, 0})
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NCHW")
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(Deconvolution)
```

## Brief

Computes the Deconvolution with respect to the input.

## Inputs

Two required inputs:
- x: A Tensor of type float16 or int8. 4D with shape
[batch, out_channels, out_height, out_width]. Gradients with respect
to the output of the convolution.
- filter: A Tensor. Must have the same type as "x".
4D with shape [out_channels, in_channel, filter_height, filter_width].
Two optional inputs:
- bias: An optional tensor. Must have the same type as "y".
- offset_w: An optional 1D tensor for quantized deconvolution.
Type is int8. Reserved.
The following are the supported data types and data formats:
| Tensor    | x       | filter  | bias    | y      |
|-----------|---------|---------|---------|--------|
| Data Type | float16 | float16 | float16 | float16|
|           | int8    | int8    | int32   | int32  |
| Format    | NCHW    | NCHW    | ND      | NCHW   |
For int8, a dequant or requant operator must be followed.

## Outputs

y: A Tensor. 4D tensor with shape [batch, channels, height, width].
    out_backprop_height = (fmap_height + pad_top + pad_bottom -
                          (dilation_h * (filter_height - 1) + 1))
                          / stride_h + 1
    out_backprop_width = (fmap_width + pad_left + pad_right -
                         (dilation_w * (filter_width - 1) + 1))
                         / stride_w + 1
When type of x is float16, the type of y must be float16.
When type of x is int8, the type of y must be int32.

## Attributes

Six attributes:
- strides: A tuple or list of 2 integers. The stride of the sliding window
for H/W dimension, defaults to [1,1].
- pads: A tuple or list of 4 integers. The [top, bottom, left, right]
padding on the feature map, defaults to [0,0,0,0].
- dilations: A tuple or list of 4 integers. The dilation factor for each
dimension of input, defaults to [1,1,1,1].
- groups: Number of blocked connections from input channels to
output channels. Defaults to "1".
- data_format: An optional string from: "NCHW". Defaults to "NCHW".
Specify the data format of the input and output data.
- offset_x: An optional integer for quantized deconvolution.
The negative offset added to the input image for int8 type. Ensure offset_x
within the effective range of int8 [-128, 127]. Defaults to "0".
The following value range restrictions must be met:
| Name             | Field    | Scope        |
|------------------|----------|--------------|
| x (out_backprop) | H*strideH| [1, 4096]    |
|                  | W*strideW| [1, 4096]    |
| Filter           | H        | [1, 255]     |
|                  | W        | [1, 255]     |
| y (fmap)         | H        | [1, 4096]    |
|                  | W        | [1, 4096]    |
| Stride           | H        | [1, 63]      |
|                  | W        | [1, 63]      |
| Padding          | Top      | [0, 255]     |
|                  | Bottom   | [0, 255]     |
|                  | Left     | [0, 255]     |
|                  | Right    | [0, 255]     |
| Dilation         | H        | [1, 255]     |
|                  | W        | [1, 255]     |
| Offset_x         |          | [-128, 127]  |
In Atlas Training Series Product, fmap or out_backprop's H and W not support 1 when
fmap_h + pad_top + pad_bottom != (filter_height - 1) * dilation_h + 1
and filter_width > fmap_width
If filter_h = 1 and filter_w = 1,
 out_backprop_w * stride_h * stride_w < 4096

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8
- input1 filter: float16,float32,int8
- input2 bias: float16,float32,int32
- input3 offset_w: int8
- output0 y: float16,float32,int32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
