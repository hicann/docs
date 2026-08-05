# AdjustContrast

```c
REG_OP(AdjustContrast)
    .INPUT(images, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .INPUT(contrast_factor, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .ATTR(data_format, String, "HWC")
    .ATTR(mean_mode, String, "chn_wise")
    .OP_END_FACTORY_REG(AdjustContrast)
```

## Brief

Adjust the contrast of one or more images . 

## Inputs

Input images is a tensor of at least 3 dimensions. The last 3 dimensions are
interpreted as '[height, width, channels]'. Inputs include:
- images: A Tensor of type float. Images to adjust. At least 3-D. The format
must be NHWC.
- contrast_factor: A Tensor of type float. A float multiplier for adjusting contrast .

## Outputs

y: A Tensor of type float. The format must be NHWC. 

## Attributes

- mean_mode: An optional string. Could be "chn_wise" or "chn_y". Defaults to "chn_wise".
Value used for different mean mode.
- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float16,float32
- input1 contrast_factor: float32
- output0 y: float16,float32

## Attention Constraints

Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 

## Third-party framework compatibility

Compatible with tensorflow AdjustContrast operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
