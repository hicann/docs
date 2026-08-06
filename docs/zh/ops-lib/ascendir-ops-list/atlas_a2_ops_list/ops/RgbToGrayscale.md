# RgbToGrayscale

```c
REG_OP(RgbToGrayscale)
    .INPUT(images, "T")
    .ATTR(data_format, String, "HWC")
    .ATTR(output_channels, Int, 1)
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_UINT8, DT_FLOAT}))
    .OP_END_FACTORY_REG(RgbToGrayscale)
```

## Brief

Convert an RGB image to a gray image. 

## Inputs

Input images is a tensor of at least 3 dimensions. The last 3 dimensions are
interpreted as '[height, width, channels]'. Inputs include:
- images: A Tensor of type T. Images to adjust. At least 3-D. The format
must be NHWC or NCHW.

## Outputs

y: A Tensor of type T. The format must be NHWC or NCHW. 

## Attributes

- output_channels: An optional int. Could be 1 or 3. Defaults to 1.
Value used for different mean mode.
- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- output0 y: float32,uint8

## Attention Constraints

- This operator will be deprecated in the future.
- Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three. 

## DataType

- T: type of uint8 or float32.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
