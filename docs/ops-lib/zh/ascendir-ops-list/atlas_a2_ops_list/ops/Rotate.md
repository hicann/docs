# Rotate

```c
REG_OP(Rotate)
    .INPUT(x, "T")
    .OUTPUT(y, "T")
    .REQUIRED_ATTR(angle, Float)
    .ATTR(center, ListInt, {})
    .ATTR(expand, Bool, false)
    .ATTR(interpolation, String, "nearest")
    .ATTR(padding_mode, String, "constant")
    .ATTR(padding_value, Float, 0.0)
    .ATTR(data_format, String, "HWC")
    .DATATYPE(T, TensorType({DT_UINT8, DT_FLOAT}))
    .OP_END_FACTORY_REG(Rotate)
```

## Brief

Applies a rotate to an image. 

## Inputs

- x: An NHWC or NCHW tensor of type T.

## Outputs

y: output tensor, NHWC or NCHW, type must be T.

## Attributes

- angle: An required float attr. In degress counter clockwise.
- center: An optional ListInt, center of rotation. Origin is the upper left corner.
Default is the center of the image.
- expand: An optional Bool, expansion flag. If true, expands the output image to make it large enough to hold the
entire rotated image. If false or omitted, make the output image the same size as the input image.
Note that the expand flag assumes rotation around the center and no translation.
- interpolation: An optional string. Interpolation type, only support "bilinear"/"nearest", default "nearest".
- padding_mode: An optional string. Pixel extension method, only support "constant" and "edge", default "constant".
- padding_value: An optional float. Used when padding_mode is "constant". Data type is the same as that of the
original picture. The number of data is the same as that of the original picture channels. Deatulat value is 0 . 
- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 x: float32,uint8
- output0 y: float32,uint8

## Attention Constraints

This operator will be deprecated in the future.

## DataType

- T: type of uint8 or float32.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
