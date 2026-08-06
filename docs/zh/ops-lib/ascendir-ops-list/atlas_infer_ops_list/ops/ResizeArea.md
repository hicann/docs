# ResizeArea

```c
REG_OP(ResizeArea)
    .INPUT(images, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(align_corners, Bool, false)
    .OP_END_FACTORY_REG(ResizeArea)
```

## Brief

Resize images to size using area interpolation . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- images: 4-D with shape [batch, height, width, channels]. The format must
be NHWC.
- size: A 1-D int32 Tensor of 2 elements: new_height, new_width.
The new size for the images . 

## Outputs

y: 4-D with shape [batch, new_height, new_width, channels]. The format must
be NHWC. 

## Attributes

align_corners: If true, the centers of the 4 corner pixels of the input and
output tensors are aligned, preserving the values at the corner pixels.
Defaults to false . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 size: int32
- output0 y: float32

## Attention Constraints

Input images can be of different types but output images are always float . 

## Third-party framework compatibility

Compatible with tensorflow ResizeArea operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
