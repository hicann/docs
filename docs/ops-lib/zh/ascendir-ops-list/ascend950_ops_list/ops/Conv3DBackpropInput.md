# Conv3DBackpropInput

```c
REG_OP(Conv3DBackpropInput)
    .INPUT(input_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(Conv3DBackpropInput)
```

## Brief

Computes the gradients of convolution 3D with respect to the input.

## Inputs

- input_size: A 1-D Tensor of type int32 or int64.
The tensor representing the shape of feature map (the input of the convolution),
where feature map is a 5-D tensor with the format "NDCHW" or "NCDHW".
The order of integers in the tensor is determined by feature map format,
and integers represent the length of each dimension of feature map.
The axes sequence that can be entered are as follows:
[batch, in_depth, in_height, in_width, in_channels] or
[batch, in_channels, in_depth, in_height, in_width].
Any value of input_size must be in [1, 2147483647].
- filter: A 5-D Tensor. Must be one of the following types: float16, bfloat16, float32.
The format of the filter tensor must be one of the followings:
[out_channels, in_channels/groups, filter_depth, filter_height, filter_width] or
[filter_depth, filter_height, filter_width, in_channels/groups, out_channels].
In short, the filter tensor supports format NCDHW, NDHWC and DHWCN.
In Ascend 950PR/Ascend 950DT, the filter_height and filter_width dimensions must be in [1, 2147483647],
for other products filter_height and filter_width dimensions must be in [1, 511].
The other dimensions must be in [1, 2147483647].
- out_backprop: A 5-D Tensor. Must have the same type as filter.
The format of the out_backprop tensor must be one of the followings:
[batch, out_depth, out_height, out_width, out_channels] or
[batch, out_channels, out_depth, out_height, out_width].
Any dimension of out_backprop shape must be in [1, 2147483647].
Gradients with respect to the "output" of the convolution.

## Outputs

y: A tensor. It has the same format as out_backprop.
The type is float16, bfloat16, float32.
The gradients of feature map.
Any dimension of y shape must be in [1, 2147483647].

## Attributes

- strides: Required. A tuple/list of 5 integers. Specifies the stride of the sliding window
for each dimension of feature map. The strides have the same axes sequence as feature map:
[batch, stride_depth, stride_height, stride_width, channels] or
[batch, channels, stride_depth, stride_height, stride_width].
The batch(N) and channels(C) dimensions must be 1.
The other values of strides must be in [1, 2147483647].
- pads: Required. A tuple/list of 6 integers. Specifies the pads factor of
feature map in each directions. Supports only pads along the depth(D),
height(H) and width(W) dimensions.
The pads sequence is as follows: [front, back, top, bottom, left, right].
In Ascend 950PR/Ascend 950DT, the top, bottom, left and right must be in [0, 2147483647],
for other products top, bottom, left and right must be in [0, 255].
The front and back must be in [0, 2147483647].
Modes "SAME" and "VALID" padding can be achieved with appropriate values of each direction in pads.
- dilations: Optional. Defaults to [1, 1, 1, 1, 1].
A tuple/list of 5 integers, The dilation factor for each dimension of filter.
The dilations has the same axes sequence as filter:
[out_channels, in_channels/groups, depth, dilation_height, dilation_width] or
[depth, dilation_height, dilation_width, in_channels/groups, out_channels].
The batch(N), in_channels/groups(C) dimensions must be 1.
In Ascend 950PR/Ascend 950DT, depth (D), height (H) and width (W) dimensions must be in [1, 2147483647],
for other products depth (D), height (H) and width (W) dimensions must be in [1, 255].
- groups: Optional. Defaults to 1 and the value must be in [1, 65535].
Number of blocked connections from in_channels to out_channels.
The in_channels and out_channels must be divisible by groups.
When the groups value differs, it is supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component as follows: 
| groups |        dtype           | out_backprop format | filter format |     y format   |
|--------|------------------------|---------------------|---------------|----------------|
|  =1    |float16/bfloat16/float32|       NCDHW         |      NCDHW    |     NCDHW      |
|  =1    |float16/bfloat16/float32|       NCDHW         |      NDHWC    |     NCDHW      |
|  =1    |float16/bfloat16/float32|       NCDHW         |      DHWCN    |     NCDHW      |
|  =1    |float16/bfloat16/float32|       NDHWC         |      NDHWC    |     NDHWC      |
|  =1    |float16/bfloat16/float32|       NDHWC         |      NCDHW    |     NDHWC      |
|  =1    |float16/bfloat16/float32|       NDHWC         |      DHWCN    |     NDHWC      |
|  >1    |float16/bfloat16/float32|       NCDHW         |      NCDHW    |     NCDHW      |
|  >1    |float16/bfloat16/float32|       NCDHW         |      NDHWC    |     NCDHW      |
|  >1    |float16/bfloat16/float32|       NCDHW         |      DHWCN    |     NCDHW      |
- data_format: Optional. Defaults to "NDHWC". A string from: "NDHWC", "NCDHW".
The correspondence is as follows: batch(N), depth(D), height(H), width(W), channels(C).
Specify the data format of the feature map, out_backprop and y.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32,int64
- input1 filter: bfloat16,float16,float32
- input2 out_backprop: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with Tensorflow's conv3d_backprop_input

## Attention Constraints:

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.
Due to hardware resource restrictions,
the operator fails to be executed in scenarios of some parameter value combinations.
Analyze and rectify the fault based on the log information.
If the fault persists, visit https://www.hiascend.com/support for technical support.


---

[Back to Operator Specifications (Ascend950)](../README.md)
