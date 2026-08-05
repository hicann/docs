# Conv3DBackpropFilterV2

```c
REG_OP(Conv3DBackpropFilterV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(filter_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NDHWC")
    .ATTR(enable_hf32, Bool, false)
    .OP_END_FACTORY_REG(Conv3DBackpropFilterV2)
```

## Brief

Computes the gradients of convolution3D with respect to the filter

## Inputs

- x: A 5D tensor. Must be one of the following types: float16, float32, bfloat16.
The format of the x tensor must be one of the followings:
[batch, in_depth, in_height, in_width, in_channels]
or [batch, in_channels, in_depth, in_height, in_width]. 
- filter_size: A 1D tensor of type int32 or int64. The tensor representing the
shape of filter, where filter is a 5D tensor.
The order of integers in the tensor is determined by filter format,
and integers represent the length of each dimension of filter.
The axes sequence that can be entered are as follows:
[out_channels, in_channels, filter_depth, filter_height, filter_width]
or [out_channels, filter_depth, filter_height, filter_width, in_channels].
- out_backprop: A 5D tensor. Must have the same type and format as x.
The format of the out_backprop tensor must be one of the followings:
[batch, out_depth, out_height, out_width, out_channels] or
[batch, out_channels, out_depth, out_height, out_width].
Gradients with respect to the "output" of the convolution. 

## Outputs

y: A Tensor that has the type float32. The format is NCDHW or NDHWC or DHWCN.

## Attributes

- strides: Required. A tuple/list of 5 integers. Specifies the stride
of the sliding window for each dimension of feature map.
The strides have the same axes sequence as feature map:
[batch, stride_depth, stride_height, stride_width, channels] or
[batch, channels, stride_depth, stride_height, stride_width].
The batch(N) and channels(C) dimensions must be 1.
The height (H) and width (W) dimensions must be in [1, 63].
The depth (D) dimension must be in [1, 255]. 
- pads: Required. A tuple/list of 6 integers. Specifies the pads factor of
feature map in each directions. Supports only pads along the depth(D),
height(H) and width(W) dimensions.
The pads sequence is as follows: [front, back, top, bottom, left, right].
The height (H), width (W) and depth (D) dimensions must be in [0, 255].
Modes "SAME" and "VAILD" padding can be achieved with appropriate values of each direction in pads. 
- dilations: Optional. A tuple/list of 5 integers. The dilation factor
for each dimension of input. Defaults to [1, 1, 1, 1, 1]
The dilations have the same axes sequence feature map:
[batch, dilation_depth, dilation_height, dilation_width, channels] or
[batch, channels, dilation_depth, dilation_height, dilation_width].
The batch(N) and channels dimensions must be 1.
- groups: An optional integer within the effective range of [1, 65535]. Default to 1.
Number of blocked connections from in_channels to out_channels.
Currently in_channels and out_channels must be divisible by groups
and x data type must be one of the following types: float16, bfloat16, float32.
- data_format: An optional string. The value must be one of ["NDHWC", "NCDHW"]. Defaults to "NDHWC".
The correspondence is as follows: batch(N), depth(D), height(H), width(W), channels(C).
Specify the data format of the x and out_backprop. 
- enable_hf32: Optional. An optional bool parameter. Used to enable hf32 computation.
If true, enable hf32 computation, otherwise, disable hf32 computation. Defaults to false. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 filter_size: int32
- input2 out_backprop: bfloat16,float16,float32
- output0 y: float32

## Attention Constraints

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.

## Third-party framework compatibility

Compatible with Tensorflow's conv3d_backprop_filter


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
