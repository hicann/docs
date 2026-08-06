# ResizeTrilinear

```c
REG_OP(ResizeTrilinear)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .OP_END_FACTORY_REG(ResizeTrilinear)
```

## Brief

Resize images to size using trilinear interpolation . 

## Inputs

Input images must be a 5-D tensor. Inputs include:
- x: A 5-D tensor, type must be float16, float32 or double. Must set the format, supported format list
is ["NCDHW, NDHWC"] .
- size: A 1-D tensor, type must be int32. Contains 3 elements: new_depth, new_height, new_width.
Set the shape of output y . 

## Outputs

y: 5-D with shape [batch, channels, new_depth, new_height, new_width] . 

## Attributes

- align_corners: If true, the centers of the 8 corner pixels of the input and
output tensors are aligned, preserving the values at the corner pixels.
Defaults to false .
- half_pixel_centers: An optional bool. Defaults to false .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- input1 size: int32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with onnx Resize operator using trilinear interpolation.


---

[Back to Operator Specifications (Ascend950)](../README.md)
