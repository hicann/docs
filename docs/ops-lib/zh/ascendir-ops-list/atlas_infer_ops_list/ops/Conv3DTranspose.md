# Conv3DTranspose

```c
REG_OP(Conv3DTranspose)
    .INPUT(input_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NDHWC")
    .ATTR(output_padding, ListInt, {0, 0, 0, 0, 0})
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(Conv3DTranspose)
```

## Brief

Computes the transpose of convolution 3d with respect to the input.

## Inputs

- input_size: A tensor of type int32 or int64. An integer vector
representing the shape of input.
Any value of input_size must be in [1, 2147483647].
- x: A tensor of type float16, bfloat16, float32. The format
is NDHWC or NCDHW.
- filter: A tensor of type float16, bfloat16, float32.
The format is NDHWC, NCDHW or DHWCN.
In Ascend 950PR/Ascend 950DT, the filter_height and filter_width dimensions must be in [1, 2147483647],
for other products filter_height and filter_width dimensions must be in [1, 511].
The other dimensions must be in [1, 2147483647].
- bias: Optional. An optional 1D tensor of type float16 and float32. When x
is float16, bias is float16. When x is bfloat16, bias is float32.
"in_channels" must equals to the "out_channels" of output y.
Currently bias is not supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component. Reserved.
- offset_w: Optional. An optional 1D tensor for quantized deconvolution.
Defaults to 0.
Currently offset_w is not supported on Atlas 200/500 A2 Inference Product,
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
and Ascend 950PR/Ascend 950DT. Reserved.

## Outputs

y: A tensor of type float16, float32, or bfloat16, and has
 same format as input_size.
Any dimension of y shape must be in [1, 2147483647].

## Attributes

- strides: Required. A tuple/list of 5 integers. Specifies the stride of
the sliding window for each dimension of "x".
The strides have the same axes sequence as "x":
[batch, stride_depth, stride_height, stride_width, channels] or
[batch, channels, stride_depth, stride_height, stride_width].
The batch(N) and channels(C) dimensions must be 1.
The other values of strides must be in [1, 2147483647].
- pads: Required. A tuple/list of 6 integers.
[front, back, top, bottom, left, right] pads on feature map.
All dimensions must be greater than or equal to 0.
The front and back must be in [0, 2147483647].
- dilations: Optional. A tuple/list of 5 integers,
The dilation factor for each dimension of input. Defaults to [1, 1, 1, 1, 1].
The dilations has the same axes sequence as filter:
[batch, channels, dilation_depth, dilation_height, dilation_width] or
[batch, dilation_depth, dilation_height, dilation_width, channels].
The batch(N) and channel(C) must be 1.
The width (W), height (H) and depth(D) dimensions must be greater than 0.
In Ascend 950PR/Ascend 950DT, depth (D), height (H) and width (W) dimensions must be in [1, 2147483647],
for other products depth (D), height (H) and width (W) dimensions must be in [1, 255].
In graph mode, Atlas 200/500 A2 Inference Product,
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component
only configuration to [1, 1, 1, 1, 1] is supported.
- groups: Optional. Number of blocked connections from input channels to
 output channels. Defaults to 1.
The in_channels and out_channels must be divisible by groups.
The value of groups must be in [1, 65535].
- data_format: Optional. A string from: "NDHWC", "NCDHW".
Defaults to "NDHWC". Specify the data format of the x and y.
- output_padding: Optional. The size will be added in the output shape.
Defaults to [0, 0, 0, 0, 0].
The N and C dimensions must be 0.
In Ascend 950PR/Ascend 950DT, D, H and W have the following restrictions:
D must be less than dilation_d or stride_d,
H must be less than dilation_h or stride_h,
C must be less than dilation_w or stride_w,
and D, H, W must be in [0, 2147483647].
Currently output_padding is not supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component.
In graph mode, only configuration to [0, 0, 0, 0, 0] is supported.
- offset_x: Optional. Input offset_x value. Defaults to 0.
Currently offset_x is not supported on Atlas 200/500 A2 Inference Product and
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component. Reserved.
Ensure offset_x within the effective range of int8 [-128, 127]. Defaults to "0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32,int64
- input1 x: float16
- input2 filter: float16
- input3 bias: float16,float32
- input4 offset_w: int8
- output0 y: float16,float32

## Attention Constraints:

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.
Due to hardware resource restrictions,
the operator fails to be executed in scenarios of some parameter value combinations.
Analyze and rectify the fault based on the log information.
If the fault persists, visit https://www.hiascend.com/support for technical support.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
