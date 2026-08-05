# Conv3DTransposeV2

```c
REG_OP(Conv3DTransposeV2)
    .INPUT(input_size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8, DT_FLOAT8_E4M3FN}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8, DT_FLOAT8_E4M3FN}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8, DT_FLOAT8_E4M3FN}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NDHWC")
    .ATTR(output_padding, ListInt, {0, 0, 0, 0, 0})
    .ATTR(offset_x, Int, 0)
    .ATTR(enable_hf32, Bool, false)
    .OP_END_FACTORY_REG(Conv3DTransposeV2)
```

## Brief

Computes the transpose of convolution 3d with respect to the input.

## Inputs

- input_size: A tensor of type int32 or int64. An integer vector
representing the shape of input.
- x: A tensor of the following types, float16, float32, bfloat16, hifloat8, float8_e4m3fn. The format
is NDHWC or NCDHW.
- filter: A 5D tensor.
The format is NCDHW，NDHWC, and DHWCN.
The NCDHW can be one of the following types: float16, bfloat16, float32, hifloat8, float8_e4m3fn.
The DHWCN and NDHWC can be one of the following types: float16, bfloat16, float32.
The height (H), width (W) dimension must be greater than 0.
- bias: Optional. An optional 1D tensor of type float16 or float32. Reserved.
- offset_w: Optional. An optional 1D tensor of type int8 for quantized deconvolution.
 Reserved. 

## Outputs

y: A tensor that has the type bfloat16, float16, float32, hifloat8, float8_e4m3fn. It has the same format as "x".

## Attributes

- strides: Required. A tuple/list of 5 integers. Specifies the stride of the sliding window
for each dimension of "x". The strides have the same axes sequence as "x":
[batch, stride_depth, stride_height, stride_width, channels] or
[batch, channels, stride_depth, stride_height, stride_width].
The N and C dimensions must be 1.
The depth (D), The height (H) and width (W) dimensions must be greater than 0.
- pads: Required. A tuple/list of 6 integers.
All dimensions must be greater than or equal to 0.
- dilations: Optional. A tuple/list of 5 integers,
The dilation factor for each dimension of input. Defaults to [1, 1, 1, 1, 1]. 
The batch(N) and channels dimensions must be 1.
The width (W), height (H) and depth(D) dimensions must be greater than 0.
The dilations have the same axes sequence "x":
[batch, channels, dilation_depth, dilation_height, dilation_width] or
[batch, dilation_depth, dilation_height, dilation_width, channels].
- groups: An optional integer within the effective range of [1, 65535]. Default to 1.
Number of blocked connections from in_channels to out_channels.
The in_channels and out_channels must be divisible by groups.
When the groups value differs, the supported data type may vary, specifically as follows: 
| groups |        dtype           |   x format  | filter format |    y format    |
|--------|------------------------|-------------|---------------|----------------|
|  =1    |hifloat8/float8_e4m3fn  |    NCDHW    |      NCDHW    |     NCDHW      |
|  =1    |hifloat8/float8_e4m3fn  |    NDHWC    |      NCDHW    |     NDHWC      |
|  =1    |float16/bfloat16/float32|    NCDHW    |      NCDHW    |     NCDHW      |
|  =1    |float16/bfloat16/float32|    NCDHW    |      NDHWC    |     NCDHW      |
|  =1    |float16/bfloat16/float32|    NCDHW    |      DHWCN    |     NCDHW      |
|  =1    |float16/bfloat16/float32|    NDHWC    |      NDHWC    |     NDHWC      |
|  =1    |float16/bfloat16/float32|    NDHWC    |      NCDHW    |     NDHWC      |
|  =1    |float16/bfloat16/float32|    NDHWC    |      DHWCN    |     NDHWC      |
|  >1    |hifloat8/float8_e4m3fn  |    NCDHW    |      NCDHW    |     NCDHW      |
|  >1    |float16/bfloat16/float32|    NCDHW    |      NCDHW    |     NCDHW      |
|  >1    |float16/bfloat16/float32|    NCDHW    |      NDHWC    |     NCDHW      |
|  >1    |float16/bfloat16/float32|    NCDHW    |      DHWCN    |     NCDHW      |
- data_format:  An optional string. The value must be one of ["NDHWC", "NCDHW"]. Defaults to "NDHWC".
The correspondence is as follows: batch(N), depth(D), height(H), width(W), channels(C).
Specify the data format of the x and y.
- output_padding: Optional. The size will be added in the output shape.
Defaults to [0, 0, 0, 0, 0]. The N and C dimensions must be 0.
- offset_x: Optional. Defaults to 0. Reserved.
- enable_hf32: Optional. An optional bool parameter. Used to enable hf32 computation.
If true, enable hf32 computation, otherwise, disable hf32 computation. Defaults to false. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_size: int32,int64
- input1 x: bfloat16,float8_e4m3fn,float16,float32,hifloat8
- input2 filter: bfloat16,float8_e4m3fn,float16,float32,hifloat8
- input3 bias: float32,hifloat8
- input4 offset_w: int8
- output0 y: bfloat16,float8_e4m3fn,float16,float32,hifloat8

## Attention Constraints

In Ascend 950PR/Ascend 950DT: The behavior of gradient computation in the padding region depends on the input shape.
Depending on the operator optimization strategy, the padding gradients may be directly set to 0.


---

[Back to Operator Specifications (Ascend950)](../README.md)
