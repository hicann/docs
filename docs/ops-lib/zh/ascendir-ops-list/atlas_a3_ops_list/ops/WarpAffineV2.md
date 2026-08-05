# WarpAffineV2

```c
REG_OP(WarpAffineV2)
    .INPUT(x, TensorType({DT_FLOAT, DT_UINT8}))
    .INPUT(matrix, TensorType({DT_FLOAT}))
    .INPUT(dst_size, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_UINT8}))
    .ATTR(interpolation, String, "bilinear")
    .ATTR(border_type, String, "constant")
    .ATTR(border_value, Float, 0.0)
    .ATTR(data_format, String, "HWC")
    .OP_END_FACTORY_REG(WarpAffineV2)
```

## Brief

Applies a affine transformation to an image. 

## Inputs

- x: An tensor of at least 3 dimensions, type must be float32 or uint8.
- matrix: transformation matrix, format ND , shape must be (2, 3), type must be float32.
- dst_size: Required int32 and int64, shape must be (1, 2), specifying the size of the output image.
Must be greater than "0". 

## Outputs

y: output tensor of at least 3 dimensions, type must be float32 or uint8.

## Attributes

- interpolation: An optional string. Used to select interpolation type.
only support "bilinear"/"nearest"/"cubic"/"area", default "bilinear".
- border_type: An optional string. Pixel extension method, currently only support "constant", default "constant".
- border_value: An optional float. Used when border_type is "constant".
Data type is the same as that of the original picture. The number of data is the same as that of the original
picture channels. Default value is 0.
- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float32,uint8
- input1 matrix: float32
- input2 dst_size: int32,int64
- output0 y: float32,uint8


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
