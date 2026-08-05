# Conv3DBackpropFilter

```c
REG_OP(Conv3DBackpropFilter)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(filter_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(Conv3DBackpropFilter)
```

## Brief

Computes the gradients of convolution3D with respect to the filter

## Inputs

- x: A Tensor. Must be one of the following types: float16, bfloat16 or float32.
The format of the x tensor must be one of the followings:
[batch, in_depth, in_height, in_width, in_channels]
or [batch, in_channels, in_depth, in_height, in_width].
Any dimension of x shape must be in [1, 2147483646].
- filter_size: A Tensor of type int32 or int64. An integer vector representing the
tensor shape of filter, where filter is a 5-D tensor.
The order of integers in the tensor is determined by filter format,
and integers represent the length of each dimension of filter.
The axes sequence that can be entered are as follows:
[filter_depth, filter_height, filter_width, in_channels, out_channels]
[out_channels, in_channels, filter_depth, filter_height, filter_width]
or [out_channels, filter_depth, filter_height, filter_width, in_channels].
The height (H) and width (W) dimensions must be in [1, 2147483646].
Additionally, Atlas Training Series Product required Depth (D) dimension must be in [1, 255]
The other values of filter_size must be in [1, 2147483646].
- out_backprop: Gradients with respect to the output of the convolution.
A 5-D tensor. Must have the same type and format as x.
The format of the out_backprop tensor must be one of the followings:
[batch, out_depth, out_height, out_width, out_channels]
or [batch, out_channels, out_depth, out_height, out_width].
Any dimension of out_backprop shape must be in [1, 2147483646]. 

## Outputs

y: A Tensor that has the type float32,
Must have the same format as filter_size.

## Attributes

- strides: Required. A tuple/list of 5 integers. Specifies the stride
of the sliding window for each dimension of "x".
The strides have the same axes sequence as "x".
The batch(N) and channels(C) dimensions must be 1.
The stride_height(H) and stride_width(W) dimensions must be in [1, 63].
The stride_depth(D) dimension must be in [1, 2147483646].
In Ascend 950PR/Ascend 950DT, the stride_depth(D), stride_height(H) and stride_depth(W) must be in [1, 2147483646].
- pads: Required. A tuple/list of 6 integers, [front, back, top, bottom,
left, right] pads on x.
The top, bottom, left and right must be in [0, 255].
The front and back must be in [0, 2147483646].
In Ascend 950PR/Ascend 950DT, the top, bottom, left, right, front and back must be in [0, 2147483646].
Modes "SAME" and "VALID" padding can be achieved with appropriate values of each direction in pads.
- dilations: Optional. A tuple/list of 5 integers, The dilation factor
for each dimension of input. Defaults to [1, 1, 1, 1, 1].
The N and C dimensions must be 1,
height (H) and width (W) dimensions must be in [1, 255],
depth(D) dimension must be in [1, 2147483646].
The dilations have the same axes sequence "x":
[batch, dilation_depth, dilation_height, dilation_width, channels] or
[batch, channels, dilation_depth, dilation_height, dilation_width].
In graph mode, only configuration to [1, 1, 1, 1, 1] is supported.
In Ascend 950PR/Ascend 950DT, the depth(D), height(H) and width(W) dimensions must be in [1, 2147483646].
- groups: Optional. Number of blocked connections from input channels
to output channels. Defaults to 1.
Currently in_channels and out_channels must be divisible by groups.
The value of groups must be in [1, 65535].
- data_format: Optional. A string from: "NDHWC", "NCDHW".
Defaults to "NDHWC". Specify the data format of the x and out_backprop. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 filter_size: int32
- input2 out_backprop: float16
- output0 y: float32

## Third-party framework compatibility

Compatible with Tensorflow's conv3d_backprop_filter

## Attention Constraints:

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.
Due to hardware resource restrictions,
the operator fails to be executed in scenarios of some parameter value combinations.
Analyze and rectify the fault based on the log information.
If the fault persists, visit https://www.hiascend.com/support for technical support.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
