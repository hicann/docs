# DepthwiseConv2DBackpropInput

```c
REG_OP(DepthwiseConv2DBackpropInput)
    .INPUT(input_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(input_grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(DepthwiseConv2DBackpropInput)
```

## Brief

Computes the gradients of depthwise convolution with respect to the input.
The feature map mentioned in this description refers to the output tensor input_grad. 

## Inputs

Three inputs include:
- input_size: A tensor of input tensor [NCHW] or [NHWC],
support int32 and int64.
- filter: 4D filter tensor with shape of [NCHW] or [NHWC], support type float16, bfloat16 and float32.
- out_backprop: 4D tensor with shape [NCHW] or [NHWC].
Must be one of the following types: float16, bfloat16 and float32. 

## Outputs

input_grad: Gradient of the deep convolution relative to the input with shape
[N, C, H, W] or [N, H, W, C] Must be one of the following types:
float16, bfloat16 and float32. 

## Attributes

- strides: A required list or tuple of int32. The stride of the sliding
window for height and width of input "x" of the convolution.
The strides have the same axes sequence as feature map:
[1, 1, stride_height, stride_width] or [1, stride_height, stride_width, 1].
The batch(N) and channels(C) dimensions must be 1.
The other values of strides must be in [1, 2147483647].
- dilations: An optional list or tuple of int32.
Defaults to "[1, 1, 1, 1]".
If set to K > 1, there will be K-1 skipped cells between each filter element
on that dimension. The dilations has the same axes sequence as filter:
[1, 1, dilation_height, dilation_width] or [1, dilation_height, dilation_width, 1].
In Ascend 950PR/Ascend 950DT, height (H) and width (W) dimensions must be in [1, 2147483647],
for other products height (H) and width (W) dimensions must be in [1, 255].
- pads: A required list or tuple of int32. Padding added to each dimension
of the input.
In Ascend 950PR/Ascend 950DT, the top, bottom, left and right must be in [0, 2147483647],
for other products top, bottom, left and right must be in [0, 255].
- data_format: An optional string. Input data format, either "NHWC" or
"NCHW". Defaults to "NHWC" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32
- input1 filter: float16
- input2 out_backprop: float16
- output0 input_grad: float16,float32

## Third-party framework compatibility

- Compatible with the TensorFlow operator DepthwiseConv2DBackpropInput.
- Compatible with the Caffe operator DepthwiseConv2DBackpropInput.

## Attention Constraints:

The feature map is 4D with shape [N, C, Hi, Wi] or [N, Hi, Wi, C], but
the data is 5D with shape [N, C1, Hi, Wi, C0], where C0 is 16.
The filter is 4D with shape [Hf, Wf, C, K], but the data is 6D with shape
[C1, Hf, Wf, K, Co, C0],
where K is fixed at 1, and Co and C0 are 16.
Output backprop is 4D with shape [N, C, Ho, Wo] or [N, Ho, Wo, C], but the
data is 5D with shape [N, C1, Ho, Wo, C0],
where C is the same as that of the feature map and C0 is 16.
Limited by Tiling: max_h_in_l1 >= C0, where max_h_in_l1 = (l1_size - Hf *
Wf * C0 * C0 * 2) / (2 * Wo *C0). 
In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
