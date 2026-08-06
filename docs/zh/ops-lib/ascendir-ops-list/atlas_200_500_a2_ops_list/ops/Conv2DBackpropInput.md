# Conv2DBackpropInput

```c
REG_OP(Conv2DBackpropInput)
    .INPUT(input_size, TensorType({DT_INT32}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(Conv2DBackpropInput)
```

## Brief

Computes the gradients of convolution with respect to the input.
The feature map mentioned in this description refers to the output tensor y.

## Inputs

Three inputs:
- input_size: A Tensor of type int32.
An integer vector representing the shape of input, where
input is a 4D tensor [batch, height, width, channels]
or [batch, channels, height, width].
Any value of input_size must be in [1, 2147483647].
- filter: A Tensor. Must be one of the following types: float16/float32/bfloat16.
The format of the filter tensor must be one of the followings:
[out_channels, in_channels/groups, filter_height, filter_width] or
[filter_height, filter_width, in_channels/groups, out_channels].
In Ascend 950PR/Ascend 950DT, the filter_height and filter_width dimensions must be in [1, 2147483647],
for other products filter_height and filter_width dimensions must be in [1, 511].
The other dimensions must be in [1, 2147483647].
- out_backprop: A Tensor. Must have the same dtype as filter.
Must be one of the following types: float16/float32/bfloat16.
4D with shape [batch, out_height, out_width, out_channels]
or [batch, out_channels, out_height, out_width].
Any dimension of out_backprop shape must be in [1, 2147483647].
Gradients with respect to the output of the convolution.
In Ascend 950PR/Ascend 950DT, the following are the supported data types and data formats:
| Tensor    | out_bckprop | filter   | y       |
|-----------|-------------|----------|---------|
| Data Type | float16     | float16  | float16 |
| Data Type | float16     | float16  | float32 |
| Data Type | float32     | float32  | float32 |
| Data Type | bfloat16    | bfloat16 | bfloat16|
| Format    | NCHW        | NCHW     | NCHW    |
| Format    | NHWC        | HWCN     | NHWC    |
The following are the supported data types and data formats for other products:
| Tensor    | out_bckprop | filter   | y       |
|-----------|-------------|----------|---------|
| Data Type | float16     | float16  | float16 |
| Data Type | float32     | float32  | float32 |
| Data Type | bfloat16    | bfloat16 | bfloat16|
| Format    | NCHW        | NCHW     | NCHW    |
| Format    | NHWC        | HWCN     | NHWC    |

## Outputs

y: A Tensor. Has the same dtype as filter, and has the same format as out_backprop.
Any dimension of y shape must be in [1, 2147483647].
    out_backprop_height = (fmap_height + pad_top + pad_bottom -
                          (dilation_h * (filter_height - 1) + 1))
                          / stride_h + 1
    out_backprop_width = (fmap_width + pad_left + pad_right -
                         (dilation_w * (filter_width - 1) + 1))
                         / stride_w + 1

## Attributes

Five attributes:
- strides: A tuple/list of 4 integers. The stride of the sliding window
for H/W dimension. The index of H/W is the same as data_format. The value of
N/C dimensions must be 1.
The other values of strides must be in [1, 2147483647].
- pads: A tuple/list of 4 integers, [top, bottom, left, right] pads
on feature map.
In Ascend 950PR/Ascend 950DT, the top, bottom, left and right must be in [0, 2147483647],
for other products top, bottom, left and right must be in [0, 255].
- dilations: A optional tuple/list of 4 integers, The dilation factor for each
dimension of input, defaults to [1,1,1,1]. Must be with shape
[1, 1, dilation_height, dilation_width] or [1, dilation_height, dilation_width, 1].
The value of N/C dimensions must be 1.
In Ascend 950PR/Ascend 950DT, height (H) and width (W) dimensions must be in [1, 2147483647],
for other products height (H) and width (W) dimensions must be in [1, 255].
- groups: A optional integer of blocked connections
from input channels to output channels.
Defaults to 1 and the value must be in [1, 65535].
The in_channels and out_channels must be divisible by groups.
- data_format: An optional string from: "NHWC", "NCHW". Defaults to
"NHWC". Specify the data format of the out_backprop and output data.
In Atlas Training Series Product, fmap or out_backprop's H and W not support 1 when
fmap_h + pad_top + pad_bottom != (filter_height - 1) * dilation_h + 1
and filter_width > fmap_width.
If filter_h = 1 and filter_w = 1, out_backprop_w * stride_h *
 stride_w < 4096. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32
- input1 filter: float16
- input2 out_backprop: float16
- output0 y: float16

## Attention Constraints

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.

## Third-party framework compatibility

Compatible with Tensorflow's conv2d_backprop_input


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
