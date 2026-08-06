# ResizeLinear

```c
REG_OP(ResizeLinear)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(scale, Float, 0.0f)
    .OP_END_FACTORY_REG(ResizeLinear)
```

## Brief

Resize images to size using linear interpolation.

## Inputs

Input images must be a 3-D tensor. Inputs include:
- x: 3-D with shape [batch, channels, L] (format is NCL), dtype must in (FLOAT32, BFLOAT16, FLOAT16).
- size: A 1-D int32 tensor of 1 elements: output L. The new size L for the images.

## Outputs

y: 3-D with shape [batch, channels, L] (format is NCL), dtype and format is same as input x.
The N, C dimension must be the same as x.

## Attributes

- align_corners: An optional bool. If true, the centers of the 4 corner pixels of the input
and output tensors are aligned, preserving the values at the corner pixels.
Defaults to false.
- scale: An optional float. Multiplier for spatial size. Defaults to 0.0f.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 size: int32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch upsample_linear1d operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
