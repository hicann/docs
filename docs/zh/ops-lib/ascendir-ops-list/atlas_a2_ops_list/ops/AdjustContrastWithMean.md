# AdjustContrastWithMean

```c
REG_OP(AdjustContrastWithMean)
    .INPUT(images, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .INPUT(mean, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .INPUT(contrast_factor, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .ATTR(data_format, String, "HWC")
    .OP_END_FACTORY_REG(AdjustContrastWithMean)
```

## Brief

Adjust the contrast of images for DVPP with mean, need mean input. 

## Inputs

Input images is a tensor of at least 3 dimensions. The last 3 dimensions are
interpreted as '[height, width, channels]'. Inputs include:
- images: A Tensor of type float. Images to adjust. At least 3-D. The format
must be NHWC.
- mean: A Tensor of type float.Indicates the average value of each channel.
- contrast_factor: A Tensor of type float. A float multiplier for adjusting contrast .

## Outputs

y: A Tensor of type float. The format must be NHWC. 

## Attributes

- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input1 mean: float16,float32,uint8
- input2 contrast_factor: float32
- output0 y: float16,float32,uint8

## Attention Constraints

- This operator will be deprecated in the future.
- Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 

## Third-party framework compatibility

Compatible with tensorflow AdjustContrast operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
