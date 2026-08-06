# ExtendConvTranspose

```c
REG_OP(ExtendConvTranspose)
    .INPUT(input_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT32}))
    .OPTIONAL_INPUT(scale, TensorType({DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NDHWC")
    .ATTR(output_padding, ListInt, {0, 0, 0, 0, 0})
    .ATTR(offset_x, Int, 0)
    .ATTR(fusion_mode, Int, 0)
    .ATTR(y_quant_mode, Int, 0)
    .OP_END_FACTORY_REG(ExtendConvTranspose)
```

## Brief

Computes the transpose of convolution 3d with respect to the input.

## Inputs

- input_size: A tensor of type int32 or int64. An integer vector
representing the shape of input.
- x: A tensor of the following types, DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8. Only support DT_FLOAT16 and DT_INT8 right now.
The format is NCDHW.
- filter: A 5D tensor.
The format is NCDHW，and NDHWC.
The height (H), width (W) dimension must be in [1, 511].
- bias: Optional. An optional 1D tensor of type float16, float32 or int32.
The data is stored in the order of: [out_channels].
- scale: An optional 1D tensor. Quantization/dequantization/weighting parameter corresponding to
the first output, which is of the channelwise type. 

## Outputs

y: It has the same type and format as "x".

## Attributes

- strides: Required. A tuple/list of 5 integers. Specifies the stride of the sliding window
for each dimension of "x". The strides have the same axes sequence as "x":
[batch, stride_depth, stride_height, stride_width, channels] or
[batch, channels, stride_depth, stride_height, stride_width].
The N and C dimensions must be 1.
The height (H) and width (W) dimensions must be in [1, 63].
The depth (D) dimension must be in [1, 255].
- pads: Required. A tuple/list of 6 integers.
All dimensions must be in [0, 255].
- dilations: Optional. A tuple/list of 5 integers,
The dilation factor for each dimension of input. Defaults to [1, 1, 1, 1, 1]. 
The batch(N) and channels dimensions must be 1.
The width (W), height (H) and depth(D) dimensions must be in [1, 255].
The dilations have the same axes sequence "x":
[batch, channels, dilation_depth, dilation_height, dilation_width] or
[batch, dilation_depth, dilation_height, dilation_width, channels].
- groups: An optional integer within the effective range of [1, 65535]. Default to 1.
Number of blocked connections from in_channels to out_channels.
The in_channels and out_channels must be divisible by groups.
When the groups value differs, the supported data type may vary, specifically as follows: 
| groups |        dtype           |   x format  | filter format |    y format    |
|--------|------------------------|-------------|---------------|----------------|
|  =1    |int8                    |    NCDHW    |      NCDHW    |     NCDHW      |
|  =1    |int8                    |    NCDHW    |      NDHWC    |     NCDHW      |
|  =1    |float16                 |    NCDHW    |      NCDHW    |     NCDHW      |
|  =1    |float16                 |    NCDHW    |      NDHWC    |     NCDHW      |
|  >1    |int8                    |    NCDHW    |      NCDHW    |     NCDHW      |
|  >1    |float16                 |    NCDHW    |      NCDHW    |     NCDHW      |
|  >1    |float16                 |    NCDHW    |      NDHWC    |     NCDHW      |
- data_format:  An optional string. The value must be one of ["NDHWC", "NCDHW"]. Defaults to "NDHWC".
The correspondence is as follows: batch(N), depth(D), height(H), width(W), channels(C).
Specify the data format of the x and y.
- output_padding: Optional. The size will be added in the output shape.
Defaults to [0, 0, 0, 0, 0]. The N and C dimensions must be 0.
- offset_x: Optional. Defaults to 0. Reserved.
- fusion_mode: Optional. Only support 0 or 1, Indicates whether relu is enabled for the output. Defaults to 0.
If 0, relu is disable for the output.
- y_quant_mode: Optional. Defaults to 0. Reserved.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32,int64
- input1 x: int8
- input2 filter: int8
- input3 bias: int32
- input4 scale: uint64
- output0 y: float16,int8


---

[Back to Operator Specifications (Ascend950)](../README.md)
