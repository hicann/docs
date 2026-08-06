# ResizeBicubicV2

```c
REG_OP(ResizeBicubicV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(scales, ListFloat, {0.0f, 0.0f})
    .OP_END_FACTORY_REG(ResizeBicubicV2)
```

## Brief

Resize images to size using bicubic interpolation.

## Inputs

Input images must be a 4-D tensor. Inputs include:
- x: 4-D with shape [batch, height, width, channels] (format is NHWC) or
[batch, channels, height, width] (format is NCHW).Dtype must in (FLOAT32, BFLOAT16, FLOAT16).
- size: A 1-D int32 tensor of 2 elements: output h and w. The new
size for the images.

## Outputs

y: 4-D with shape [batch, height, width, channels] (format is NHWC) or
[batch, channels, height, width] (format is NCHW). Dtype and format is same as input x.
The N, C dimension must be the same as x.

## Attributes

- align_corners: An optional bool. If true, the centers of the 4 corner pixels of the input
and output tensors are aligned, preserving the values at the corner pixels.
Defaults to false.
- scales: An optional listfloat. Multiplier for spatial size. Defaults to {0.0f, 0.0f}.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 size: int32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch upsample_bicubic2d operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
