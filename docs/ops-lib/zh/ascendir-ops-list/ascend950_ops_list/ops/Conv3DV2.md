# Conv3DV2

```c
REG_OP(Conv3DV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8, DT_HIFLOAT8}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8}))
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(pads, ListInt, {0, 0, 0, 0, 0, 0})
    .ATTR(dilations, ListInt, {1, 1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NCDHW")
    .ATTR(offset_x, Int, 0)
    .ATTR(pad_mode, String, "SPECIFIC")
    .ATTR(enable_hf32, Bool, false)
    .OP_END_FACTORY_REG(Conv3DV2)
```

## Brief

Computes a 3D convolution with 5D "x", "filter" and "bias" tensors.
Like this, output = CONV(x, filter) + bias. 
If case with 'int8' dtype appears in Atlas A3 Training Series Product/Atlas A3 Inference Series Product or
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component,
like this: output = CONV(x, filter) * scale + bias.

## Inputs

- x: A required 5D tensor of input image.
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
a tensor with data type bfloat16, float16, float32, int8 and format "NCDHW" is supported. 
In Ascend 950 AI Processor, a tensor of type bfloat16, float16, float32 or hifloat8 and format "NCDHW" or
"NDHWC" can be supported.
- filter: A required 5D tensor of convolution kernel.
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
a tensor with data type bfloat16, float16, float32, int8 and format "NCDHW" is supported.
Kernel_h and kernel_w should be both less than 512. 
In Ascend 950 AI Processor, a tensor with data type bfloat16, float16, float32 or hifloat8 and format "NCDHW" or
"DHWCN" can be supported. Kernel_h and kernel_w should be both less than 256.
- bias: An optional 1D tensor of additive biases to the outputs.
The data is stored in the order of: [out_channels]. 
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
a tensor with data type float16, float32 and format "ND" is supported. 
In Ascend 950 AI Processor, a tensor with data type bfloat16, float16 or float32 and format "ND" can be supported.
- scale: A optional 1D tensor of scaling factors.
The data is stored in the order of: [out_channels]. 
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
a tensor with data type float32 and format "ND" is supported. 
In Ascend 950 AI Processor, this parameter is not supported.
- offset: An optional 1D tensor of bias.
The data is stored in the order of: [out_channels].
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
a tensor with data type float32 and format "ND" is supported. 
In Ascend 950 AI Processor, this parameter is not supported.
- offset_w: An optional quantitative offset tensor. A tensor of type int8. Reserved.
- The following are the supported data types and data formats for
(Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component and
Atlas A3 Training Series Product/Atlas A3 Inference Series Product):
| Tensor    | x        | filter   | bias     | scale   | offset  |    y     |
| :-------: | :------: | :------: | :------: | :-----: | :-----: | :------: |
| Data Type | float16  | float16  | float16  | float32 | float32 | float16  |
|           | bfloat16 | bfloat16 | float32  | float32 | float32 | bfloat16 |
|           | float32  | float32  | float32  | float32 | float32 | float32  |
|           | int8     | int8     | float32  | float32 | float32 | bfloat16 |
| Format    | NCDHW    | NCDHW    | ND       | ND      | ND      | NCDHW    |
The following are the supported data types and data formats for Ascend 950 AI Processor:
| Tensor    | x        | filter   | bias     |    y     |
| :-------: | :------: | :------: | :------: | :------: |
| Data Type | float16  | float16  | float16  | float16  |
|           | bfloat16 | bfloat16 | bfloat16 | bfloat16 |
|           | float32  | float32  | float32  | float32  |
|           | hifloat8 | hifloat8 | float32  | hifloat8 |
| Format    | NCDHW    | NCDHW    | ND       | NCDHW    |
|           | NDHWC    | DHWCN    | ND       | NDHWC    |

## Outputs

y: A 5D tensor of output. 
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
a tensor with data type bfloat16,float32,float16 and format "NCDHW" is supported,
which the data is stored in [n, out_channels, out_depth, out_height, out_width]. 
In Ascend 950 AI Processor, a tensor with data type bfloat16, float16, float32 or hifloat8 and
format "NCDHW" or "NDHWC" can be supported. which the data is stored in
[n, out_channels, out_depth, out_height, out_width] or [n, out_depth, out_height, out_width, out_channels].
    out_depth  = (d + pad_head + pad_tail -
                  (dilation_d * (kernel_d - 1) + 1))
                 / stride_d + 1
    out_height = (h + pad_top + pad_bottom -
                  (dilation_h * (kernel_h - 1) + 1))
                 / stride_h + 1
    out_width = (w + pad_left + pad_right -
                 (dilation_w * (kernel_w - 1) + 1))
                / stride_w + 1

## Attributes

- strides: Required. A list of 5 integers. The stride of the sliding window
for each dimension of input. The dimension order is determined by the data
format of "x". The n and in_channels dimensions must be set to 1.
When the format is "NDHWC", its shape is [1, stride_d, stride_h, stride_w, 1],
when the format is "NCDHW", its shape is [1, 1, stride_d, stride_h, stride_w].
- pads: Optional. A list of 6 integers. The number of pixels to add to each
(pad_head, pad_tail, pad_top, pad_bottom, pad_left, pad_right) side of the input. Defaults to [0, 0, 0, 0, 0, 0].
- dilations: Optional. A list of 5 integers. The dilation factor for each
dimension of input. The dimension order is determined by the data format of
"x". The n and in_channels dimensions must be set to 1.
When the format is "NDHWC", its shape is [1, dilation_d, dilation_h, dilation_w, 1],
when the format is "NCDHW", its shape is [1, 1, dilation_d, dilation_h, dilation_w]. Defaults to [1, 1, 1, 1].
- groups: Optional. An integer of type int32. The number of groups
in group convolution. In_channels and out_channels must both be divisible by "groups". Defaults to 1.
In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product, groups can only be equal to 1.
- data_format: Optional. It is a string represents input's data format. Defaults to "NCDHW". Reserved.
- offset_x: Optional. An integer of type int32. It means offset in quantization algorithm
and is used for filling in pad values. Defaults to 0. It can only be supported in
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component or
Atlas A3 Training Series Product/Atlas A3 Inference Series Product.
- pad_mode: Optional. An optional string parameter, indicating the mode of pad.
It must be "SPECIFIC" or "SAME" or "VALID". Defaults to "SPECIFIC".
- enable_hf32: Optional. An optional bool parameter. Used to enable hf32 computation.
If true, enable hf32 computation, otherwise, disable hf32 computation. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,hifloat8,int8
- input1 filter: bfloat16,float16,float32,hifloat8,int8
- input2 bias: bfloat16,float16,float32
- input3 scale: float32
- input4 offset: float32
- input5 offset_w: int8
- output0 y: bfloat16,float16,float32,hifloat8

## Attention Constraints

- The following value range restrictions must be met:
| Name             | Field                | Scope        |
| :--------------: | :------------------: | :----------: |
| x size           | n                    | [1, 1000000] |
|                  | in_channels          | [1, 1000000] |
|                  | d                    | [1, 1000000] |
|                  | h                    | [1, 100000]  |
|                  | w                    | [1, 4096]    |
| filter size      | out_channels         | [1, 1000000] |
|                  | in_channels / groups | [1, 1000000] |
|                  | kernel_d             | [1, 1000000] |
|                  | kernel_h             | [1, 511]     |
|                  | kernel_w             | [1, 511]     |
| bias size        | out_channels         | [1, 1000000] |
| scale size       | out_channels         | [1, 1000000] |
| offset size      | out_channels         | [1, 1000000] |
| strides          | stride_d             | [1, 1000000] |
|                  | stride_h             | [1, 63]      |
|                  | stride_w             | [1, 63]      |
| pads             | pad_head             | [0, 1000000] |
|                  | pad_tail             | [0, 1000000] |
|                  | pad_top              | [0, 255]     |
|                  | pad_bottom           | [0, 255]     |
|                  | pad_left             | [0, 255]     |
|                  | pad_right            | [0, 255]     |
| dilations        | dilation_d           | [1, 1000000] |
|                  | dilation_h           | [1, 255]     |
|                  | dilation_w           | [1, 255]     |
| groups           | -                    | [1, 65535]   |
| data_format      | -                    | ["NDHWC", "NCDHW"] |
| offset_x         | -                    | [-128, 127]  |
| pad_mode         | -                    | ["SPECIFIC", "SAME", "VALID"] |
| enable_hf32      | -                    | [true, false] |
- The w dimension of the input image supports cases exceeding 4096, but it may
cause compilation errors.
- If any dimension of x/filter/bias/scale/offset/y shape exceeds max 1000000,
the product of each dimension of x/filter/bias/scale/offset/y
shape exceeds max int32 minus one (2147483646) or the value of
strides/pads/dilations/groups/data_format/offset_x/pad_mode/enable_hf32
exceeds the range in the above table, the correctness of the operator cannot be guaranteed.


---

[Back to Operator Specifications (Ascend950)](../README.md)
