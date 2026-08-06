# Conv2DV2

```c
REG_OP(Conv2DV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8}))
    .INPUT(filter, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_HIFLOAT8}))
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(pads, ListInt, {0, 0, 0, 0})
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(groups, Int, 1)
    .ATTR(data_format, String, "NCHW")
    .ATTR(offset_x, Int, 0)
    .ATTR(pad_mode, String, "SPECIFIC")
    .ATTR(enable_hf32, Bool, false)
    .OP_END_FACTORY_REG(Conv2DV2)
```

## Brief

Conv2DV2 computes a 2D convolution given "x", "filter" and "bias" tensors.
The output is computed as: output = CONV(x, filter) + bias.

## Inputs

- x: A required 4D tensor of input image. With the format "NHWC" which shape is
[n, h, w, in_channels] or the format "NCHW" which shape is [n, in_channels, h, w].
- filter: A required 4D tensor of convolution kernel.
With the format "HWCN" which shape is [kernel_h, kernel_w, in_channels / groups, out_channels]
or the format "NCHW" which shape is [out_channels, in_channels / groups, kernel_h, kernel_w].
- bias: An optional 1D tensor of additive biases to the outputs.
The data is stored in the order of: [out_channels].
- offset_w: An optional quantitative offset tensor. A tensor of type int8. Reserved.
The following are the supported data types and data formats:
| Tensor    | x        | filter   | bias     | y        |
| :-------: | :------: | :------: | :------: | :------: |
| Data Type | float16  | float16  | float16  | float16  |
|           | bfloat16 | bfloat16 | bfloat16 | bfloat16 |
|           | float32  | float32  | float32  | float32  |
|           | hifloat8 | hifloat8 | float32  | hifloat8 |
| Format    | NCHW     | NCHW     | ND       | NCHW     |
|           | NHWC     | HWCN     | ND       | NHWC     |
The following are the supported data types and data formats for MC62:
| Tensor    | x        | filter                   | bias    | y        |
| :-------: | :------: | :----------------------: | :-----: | :------: |
| Data Type | float16  | float16                  | float16 | float16  |
| Format    | NCHW     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | NCHW     |
|           | NCHW     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | NHWC     |
|           | NHWC     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | NCHW     |
|           | NHWC     | FRACTAL_Z/FRACTAL_Z_C04  | ND      | NHWC     |

## Outputs

y: A 4D tensor of output feature map.
With the format "NHWC" which shape is [n, out_height, out_width, out_channels]
or the format "NCHW" which shape is [n, out_channels, out_height, out_width].
    out_height = (h + pad_top + pad_bottom -
                  (dilation_h * (kernel_h - 1) + 1))
                 / stride_h + 1
    out_width = (w + pad_left + pad_right -
                 (dilation_w * (kernel_w - 1) + 1))
                / stride_w + 1

## Attributes

- strides: Required. A list of 4 integers. The stride of the sliding window
for each dimension of input. The dimension order is determined by the data
format of "x". The n and in_channels dimensions must be set to 1.
When the format is "NHWC", its shape is [1, stride_h, stride_w, 1],
when the format is "NCHW", its shape is [1, 1, stride_h, stride_w].
- pads: Optional. A list of 4 integers. The number of pixels to add to each
(pad_top, pad_bottom, pad_left, pad_right) side of the input. Defaults to [0, 0, 0, 0].
- dilations: Optional. A list of 4 integers. The dilation factor for each
dimension of input. The dimension order is determined by the data format of
"x". The n and in_channels dimensions must be set to 1.
When the format is "NHWC", its shape is [1, dilation_h, dilation_w, 1],
when the format is "NCHW", its shape is [1, 1, dilation_h, dilation_w]. Defaults to [1, 1, 1, 1].
- groups: Optional. An integer of type int32. The number of groups
in group convolution. In_channels and out_channels must both be divisible by "groups". Defaults to 1.
- data_format: Optional. It is a string representing x's data format. Defaults to "NCHW".
- offset_x: Optional. An integer of type int32. It means offset in quantization algorithm
and is used for filling in pad values. Ensure that the output is within the
effective range. Defaults to 0.
- pad_mode: Optional. A string parameter, indicating the mode of
pad. It must be "SPECIFIC" or "SAME" or "VALID" or "SAME_UPPER" or "SAME_LOWER".
Defaults to "SPECIFIC".
- enable_hf32: Optional. A bool parameter. Used to enable hf32 computation.
If true, enable hf32 computation, otherwise, disable hf32 computation. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,hifloat8
- input1 filter: bfloat16,float16,float32,hifloat8
- input2 bias: bfloat16,float16,float32
- input3 offset_w: int8
- output0 y: bfloat16,float16,float32,hifloat8

## Attention Constraints

- The following value range restrictions must be met:
| Name             | Field                | Scope        |
| :--------------: | :------------------: | :----------: |
| x size           | n                    | [1, 1000000] |
|                  | in_channels          | [1, 1000000] |
|                  | h                    | [1, 100000]  |
|                  | w                    | [1, 4096]    |
| filter size      | out_channels         | [1, 1000000] |
|                  | in_channels / groups | [1, 1000000] |
|                  | kernel_h             | [1, 511]     |
|                  | kernel_w             | [1, 511]     |
| bias size        | out_channels         | [1, 1000000] |
| offset_w size    | out_channels         | [1, 1000000] |
| strides          | stride_h             | [1, 63]      |
|                  | stride_w             | [1, 63]      |
| pads             | pad_top              | [0, 255]     |
|                  | pad_bottom           | [0, 255]     |
|                  | pad_left             | [0, 255]     |
|                  | pad_right            | [0, 255]     |
| dilations        | dilation_h           | [1, 255]     |
|                  | dilation_w           | [1, 255]     |
| groups           | -                    | [1, 65535]   |
| data_format      | -                    | ["NHWC", "NCHW"] |
| offset_x         | -                    | [-128, 127]  |
| pad_mode         | -                    | ["SPECIFIC", "SAME", "VALID", "SAME_UPPER", "SAME_LOWER"] |
| enable_hf32      | -                    | [true, false] |
- The w dimension of the input image supports cases exceeding 4096, but it may
cause compilation errors.
- If any dimension of x/filter/bias/offset_w/y shape exceeds max
1000000, the product of each dimension of x/filter/bias/offset_w/y
shape exceeds max int32(2147483647) or the value of
strides/pads/dilations/groups/data_format/offset_x/pad_mode/enable_hf32
exceeds the range in the above table, the correctness of the operator cannot be guaranteed.


---

[Back to Operator Specifications (Ascend950)](../README.md)
