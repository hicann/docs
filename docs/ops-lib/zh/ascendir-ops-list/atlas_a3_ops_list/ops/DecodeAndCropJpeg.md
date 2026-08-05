# DecodeAndCropJpeg

```c
REG_OP(DecodeAndCropJpeg)
    .INPUT(contents, TensorType({DT_STRING}))
    .INPUT(crop_window, TensorType({DT_INT32}))
    .OUTPUT(image, TensorType({DT_UINT8}))
    .ATTR(channels, Int, 0)
    .ATTR(ratio, Int, 1)
    .ATTR(fancy_upscaling, Bool, true)
    .ATTR(try_recover_truncated, Bool, false)
    .ATTR(acceptable_fraction, Float, 1.0)
    .ATTR(dct_method, String, "")
    .ATTR(dst_img_format, String, "HWC")
    .OP_END_FACTORY_REG(DecodeAndCropJpeg)
```

## Brief

Function parse image from string to int. 

## Inputs

- contents: A Tensor of type string. 0-D. The JPEG-encoded image.
- crop_window: 1-D. The crop window: [crop_y, crop_x, crop_height, crop_width].

## Outputs

image: A Tensor dtype of uint8.

## Attributes

- channels: An optional int. Defaults to 0. Number of color channels for the
decoded image.
- ratio: An optional int. Defaults to 1. Downscaling ratio.
- fancy_upscaling: An optional bool. Defaults to True. If true use a slower
but nicer upscaling of the chroma planes
- try_recover_truncated: An optional bool. Defaults to False. If true try to
recover an image from truncated input.
- acceptable_fraction: An optional float. Defaults to 1. The minimum required
fraction of lines before a truncated input is accepted.
- dct_method: An optional string. Defaults to "". string specifying a hint
about the algorithm used for decompression.
- dst_img_format: An optional string. Format of the output, "HWC" or "CHW". Defaults to "HWC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 contents: string
- input1 crop_window: int32
- output0 image: uint8


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
