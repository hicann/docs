# ResizeBicubic

```c
REG_OP(ResizeBicubic)
    .INPUT(images, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_UINT8, DT_FLOAT}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(ResizeBicubic)
```

## Brief

Resize images to size using bicubic interpolation . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- images: 4-D with shape [batch, height, width, channels] (format is NHWC) or
[batch, channels, height, width] (format is NCHW).
- size: A 1-D int32 Tensor of 2 elements: new_height, new_width. The new
size for the images . 

## Outputs

y: 4-D with shape [batch, height, width, channels] (format is NHWC) or
[batch, channels, height, width] (format is NCHW). 

## Attributes

- align_corners: An optional bool. If true, the centers of the 4 corner pixels of the input
and output tensors are aligned, preserving the values at the corner pixels.
Defaults to false.
- half_pixel_centers: An optional bool. Defaults to False .
- dtype: An optional Type attr. Determine the DataType of input tensor and output tensor,
must be float (set value 0) or uint8 (set value 4) , defaults to float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 size: int32
- output0 y: float32

## Attention Constraints

Input images can be of different types, output images must be float or uint8.

## Third-party framework compatibility

Compatible with tensorflow ResizeBicubic operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
