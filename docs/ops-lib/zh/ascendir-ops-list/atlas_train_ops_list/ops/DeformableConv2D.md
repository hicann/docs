# DeformableConv2D

```c
REG_OP(DeformableConv2D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(offsets, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NHWC")
    .ATTR(deformable_groups, Int, 1)
    .ATTR(modulated, Bool, true)
    .OP_END_FACTORY_REG(DeformableConv2D)
```

## Brief

Computes a 2D deformable convolution given 4D "x", "filter" and
 "offsets" tensors.

## Inputs

- x: A 4D tensor of input image. With the format "NCHW", the data is
stored in the order of: [batch, in_channels, in_height, in_width].
- filter: A 4D tensor of learnable filters. Must have the same type as
"x". With the format "NCHW" , the data is stored in the order of:
[out_channels, in_channels / groups, filter_height, filter_width].
- offsets: A 4D tensor of x-y coordinates offset and mask. With the format
"NCHW", the data is stored in the order of: [batch, deformable_groups *
filter_height * filter_width * 3, out_height, out_width].
- bias: An optional 1D tensor of additive biases to the filter outputs.
 The data is stored in the order of: [out_channels].
 The following are the supported data types and data formats:
|  Tensor    | x       | filter  | offsets | bias    | y       |
|  :-------: | :-----: | :-----: | :-----: | :-----: | :-----: |
|  Data Type | float16 | float16 | float16 | float16 | float16 |
|            | float32 | float32 | float32 | float32 | float32 |
|  Format    | NCHW    | NCHW    | NCHW    | ND      | NCHW    |
 For float32 type, the actual convolution calculation part on the chip is
 based on float16.

## Outputs

 y:  A 4D Tensor of output feature map. Has the same type as "x". With the
 format "NCHW", the data is stored in the order of: [batch, out_channels,
 out_height, out_width].
     out_height = (in_height + pad_top + pad_bottom -
                   (dilation_h * (filter_height - 1) + 1))
                  / stride_h + 1
     out_width = (in_width + pad_left + pad_right -
                  (dilation_w * (filter_width - 1) + 1))
                 / stride_w + 1

## Attributes

- strides: Required. A list of 4 integers. The stride of the sliding
window for each dimension of input. The dimension order is interpreted
according to the data format of "x". The N and C dimensions must be
set to 1.
- pads: Required. A list of 4 integers. The number of pixels to add to
each (top, bottom, left, right) side of the input.
- dilations: Optional. A list of 4 integers. The dilation factor for each
dimension of input. The dimension order is interpreted according to the
data format of "x". The N and C dimensions must be set to 1. Defaults to
[1, 1, 1, 1].
- groups: Optional. An integer of type int32. The number of blocked
connections from input channels to output channels. In_channels and
out_channels must both be divisible by "groups". Defaults to 1.
- data_format: Reserved.
- deformable_groups: Optional. An integer of type int32. The number of
deformable group partitions. In_channels must be divisible by
"deformable_groups". Defaults to 1.
- modulated: Optional. Specify version of DeformableConv2D, true means v2,
false means v1, currently only support v2.
 The following value range restrictions must be met:
|  Name             | Field    | Scope                       |
|  :--------------: | :------: | :-------------------------: |
|  Input Image Size | H        | [1, 100000 / filter_height] |
|                   | W        | [1, 4096 / filter_width]    |
|  Filter Size      | H        | [1, 63]                     |
|                   | W        | [1, 63]                     |
|  Strides          | H        | [1, 63]                     |
|                   | W        | [1, 63]                     |
|  Pads             | Top      | [0, 255]                    |
|                   | Bottom   | [0, 255]                    |
|                   | Left     | [0, 255]                    |
|                   | Right    | [0, 255]                    |
|  Dilations        | H        | [1, 255]                    |
|                   | W        | [1, 255]                    |

## Quantization supported or not

- No


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
