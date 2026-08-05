# DeformableOffsets

```c
REG_OP(DeformableOffsets)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(offsets, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .REQUIRED_ATTR(ksize, ListInt)
    .ATTR(dilations, ListInt, {1, 1, 1, 1})
    .ATTR(data_format, String, "NCHW")
    .ATTR(deformable_groups, Int, 1)
    .ATTR(modulated, Bool, true)
    .OP_END_FACTORY_REG(DeformableOffsets)
```

## Brief

Computes the deformed convolution output with the expected input

## Inputs

Two inputs:
- x: A 4D tensor of input image. A tensor of type float16, float32, bfloat16. The format support NHWC.
Shape support 4D.
- offsets: A tensor of type float16, float32, bfloat16. Deformation offset parameter.
The format support NHWC. Shape support 4D. Has the same format and dtype as "x".

## Outputs

y: Deformed convolution output. A tensor of type float16, float32, bfloat16. The format support NHWC.
Shape support 4D. Has the same format and dtype as input "x".

## Attributes

- strides: A tuple/list of 4 integers. The stride of the sliding window for
height and width for H/W dimension. Required and no default value.
- pads: A tuple/list of 4 integers. Padding added to H/W dimension
of the input. Required and no default value.
- ksize: A tuple/list of 2 integers. Kernel size. Required and no default value.
- dilations: A tuple/list of 4 integers. The dilation factor for each dimension
of input. Defaults to [1, 1, 1, 1]
- data_format: An optional string from: "NCHW", "NHWC". The default value "NCHW" is not supported.
Specify the data format of the input x. The format of the attribute
- deformable_groups: An optional int specify the c-axis grouping number of input x. Defaults to "1".
- modulated: An optional bool specify version of DeformableConv2D, true means v2, false means v1. Defaults to "true".
Only support true now.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 offsets: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: float16,float32
- input1 offsets: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
