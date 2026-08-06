# DepthwiseConv2DBackpropFilter

```c
REG_OP(DepthwiseConv2DBackpropFilter)
    .INPUT(input, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(filter_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(out_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(filter_grad, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(DepthwiseConv2DBackpropFilter)
```

## Brief

Computes the gradients of depthwise convolution with respect to
the filter. 

## Inputs

Three inputs include:
- input "x": 4D origin shape of input tensor [N, C, H, W] or [N, H, W, C].
Support type float16, bfloat16 and float32.
- filter_size: A 4D tensor of with shape [filter_height, filter_width,
in_channels, out_channels] or [out_channels, filter_height, filter_width,
in_channels]. The dimensions of filter_height and filter_width.
support type int32 and int64.
- out_backprop: 4D tensor with shape [N, C, H, W] or [N, H, W, C].
Must be one of the following types: float16, bfloat16 and float32. 

## Outputs

filter_grad: Gradient of the deep convolution relative to the filter with
shape [H, W, C, K]. Must be one of the following types: float32. 

## Attributes

- strides: A required list or tuple. The stride of the sliding window
for height and width of input "x" of the convolution.
Must be with shape [1, 1, stride_height, stride_width] or
[1, stride_height, stride_width, 1].
- dilations: An optional list or tuple. The dilation factor for each
dimension of input "x".
If set to k > 1, there will be k-1 skipped cells between each filter element
on that dimension. Must be with shape [1, 1, dilation_height, dilation_width]
or [1, dilation_height, dilation_width, 1]. Defaults to [1, 1, 1, 1].
- pads: A required list or tuple. Padding added to each dimension of the
input.
- data_format: An optional string. Input data format, either "NHWC" or
"NCHW". Defaults to "NHWC". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input: float16
- input1 filter_size: int32
- input2 out_backprop: float16
- output0 filter_grad: float32

## Attention Constraints

The feature map "x" is 4D with shape [N, C, Hi, Wi] or [N, Hi, Wi, C], but
the data is 5D with shape [N, C1, Hi, Wi, C0], where C0 is 16.
The filter is 4D with shape [Hf, Wf, C, K], but the data is 6D with shape
[C1, Hf, Wf, K, Co, C0],
where K is fixed at 1, and Co and C0 are 16.
Output backprop is 4D with shape [N, C, Ho, Wo] or [N, Ho, Wo, C], but the
data is 5D with shape [N, C1, Ho, Wo, C0],
where C is the same as that of the feature map and C0 is 16.
In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.
Only 4-dimensional data is supported currently.

## Third-party framework compatibility

- Compatible with the TensorFlow operator DepthwiseConv2DBackpropFilter.
- Compatible with the Caffe operator DepthwiseConv2DBackpropFilter.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
