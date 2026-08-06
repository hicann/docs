# ResizeNearestNeighborV2

```c
REG_OP(ResizeNearestNeighborV2)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32,
                          DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32,
                           DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .ATTR(scales, ListFloat, {0.0f, 0.0f})
    .OP_END_FACTORY_REG(ResizeNearestNeighborV2)
```

## Brief

Resize images to size using nearest neighbor interpolation. 

## Inputs

Inputs include:
- x: A 4-D tensor. Represents the original image. Must set the format, supported format list ["NCHW, NHWC"].
Must be one of the following types: int8, uint8, int16, uint16, int32, int64, float16, float32,
double, bfloat16.
- size: A 1-D int32 tensor of 2 elements: new_height, new_width.
Indicates the size of the target image, which is used to determine the height and width of the output image.
Must be the type int32. 

## Outputs

y: A 4-D tensor. Indicates the target image. Has the same type and format as input "x".
The N, C dimension must be the same as x. 

## Attributes

- align_corners: An optional bool. Determines whether to align the corners of the input and output images.
If set to True, the corner pixels of the input and output images are aligned,
preserving the value of the corner pixels. When set to false,
the scaling process scales according to proportions and does not strictly align the corners.
Defaults to false.
- half_pixel_centers: An optional bool. Determines the pixel center position during interpolation.
If this parameter is set to True, the interpolation algorithm considers the center point of the pixel
to estimate the pixel value more accurately. When set to false, the pixel center is on the integer coordinate point.
Defaults to false. 
- scales: An optional listfloat. Multiplier for spatial size. Defaults to {0.0f, 0.0f} .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 size: int32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 size: int32
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with tensorflow ResizeNearestNeighbor operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
