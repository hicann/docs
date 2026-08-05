# Conv2DBackpropFilter

```c
REG_OP(Conv2DBackpropFilter)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(filter_size, TensorType({DT_INT32}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(Conv2DBackpropFilter)
```

## Brief

Computes the gradients of convolution with respect to the filter

## Inputs

Three inputs:
- x: A 4D Tensor of input image. With the format "NHWC" which shape is
[batch, in_height, in_width, in_channels] or the format "NCHW" which shape
is [batch, in_channels, in_height, in_width].
Support type float16, bfloat16 and float32.
- filter: A Tensor of type int32. Currently does not support
data tensor. An integer vector representing the tensor shape of filter,
where filter is a 4-D tensor [filter_height, filter_width, in_channels,
out_channels] or [out_channels, filter_height, filter_width, in_channels]
or [out_channels, in_channels, filter_height, filter_width].
- out_backprop: A Tensor. Must have the same type as x and format as x. 4-D with shape
[batch, out_height, out_width, out_channels] or [batch, out_channels,
out_height, out_width]. Gradients with respect to the output of the
convolution.
Support type float16, bfloat16 and float32.
The following are the supported data types and data formats:
| Tensor    | x        | out_backprop | y       |
|-----------|--------- |--------------|---------|
| Data Type | float16  |    float16   | float32 |
|           | bfloat16 |    bfloat16  | float32 |
|           | float32  |    float32   | float32 |
| Format    | NCHW     |     NCHW     | NCHW    |
|           | NHWC     |     NHWC     | HWCN    |
|           |          |              | NHWC    |

## Outputs

y: A Tensor. Support type float32.
    out_backprop_height = (in_height + pad_top + pad_bottom -
                          (dilation_h * (filter_height - 1) + 1))
                          / stride_h + 1
    out_backprop_width = (in_width + pad_left + pad_right -
                         (dilation_w * (filter_width - 1) + 1))
                         / stride_w + 1

## Attributes

Five attributes:
- strides: A tuple/list of 4 integers. The stride of the sliding window
for H/W dimension. The index of H/W is the same as data_format.
- pads: A tuple/list of 4 integers, [top, bottom, left, right] pads on
x.
- dilations: An optional tuple/list of 4 integers, The dilation factor for each
dimension of input, defaults to [1,1,1,1].
- groups: An optional integer of blocked connections from input channels to output
channels.
- data_format: An optional string from: "NHWC", "NCHW". Defaults to
"NHWC". Specify the data format of the input and output data.
The following value range restrictions must be met, except for Ascend 950PR/Ascend 950DT:
| Name             | Field    | Scope        |
|------------------|----------|--------------|
| x(fmap)          | H        | [1, 4096]  |
|                  | W        | [1, 4096]    |
| Filter Size      | H        | [1, 255]     |
|                  | W        | [1, 255]     |
| out_backprop     | H        | [1, 4096]  |
|                  | W        | [1, 4096]    |
| y                | H        | [1, 4096]  |
|                  | W        | [1, 4096]    |
| strides          | H        | [1, 63]      |
|                  | W        | [1, 63]      |
| pads             | Top      | [0, 255]     |
|                  | Bottom   | [0, 255]     |
|                  | Left     | [0, 255]     |
|                  | Right    | [0, 255]     |
| dilations        | H        | [1, 255]     |
|                  | W        | [1, 255]     |
| groups           | H        | [1, 4096]    |
The following are supported value range restrictions for Ascend 950PR/Ascend 950DT:
| Name             | Field    | Scope           |
|------------------|----------|-----------------|
| x(fmap)          | H        | [1, 4096]       |
|                  | W        | [1, 4096]       |
| Filter Size      | H        | [1, 2147483646] |
|                  | W        | [1, 2147483646] |
| out_backprop     | H        | [1, 4096]       |
|                  | W        | [1, 4096]       |
| y                | H        | [1, 4096]       |
|                  | W        | [1, 4096]       |
| strides          | H        | [1, 2147483646] |
|                  | W        | [1, 2147483646] |
| pads             | Top      | [0, 2147483646] |
|                  | Bottom   | [0, 2147483646] |
|                  | Left     | [0, 2147483646] |
|                  | Right    | [0, 2147483646] |
| dilations        | H        | [1, 2147483646] |
|                  | W        | [1, 2147483646] |
| groups           | H        | [1, 4096]       |

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 filter_size: int32
- input2 out_backprop: float16
- output0 y: float32

## Attention Constraints

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.

## Third-party framework compatibility

Compatible with Tensorflow's conv2d_backprop_filter


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
