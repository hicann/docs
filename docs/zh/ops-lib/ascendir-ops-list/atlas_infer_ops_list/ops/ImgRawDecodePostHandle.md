# ImgRawDecodePostHandle

```c
REG_OP(ImgRawDecodePostHandle)
    .INPUT(img_channel_0, TensorType({DT_UINT16}))
    .INPUT(img_channel_1, TensorType({DT_UINT16}))
    .INPUT(img_channel_2, TensorType({DT_UINT16}))
    .INPUT(img_channel_3, TensorType({DT_UINT16}))
    .INPUT(img_size, TensorType({DT_INT32}))
    .INPUT(gamma, TensorType({DT_FLOAT}))
    .OUTPUT(raw_img, TensorType({DT_UINT16}))
    .ATTR(bayer_pattern, String, "binning")
    .OP_END_FACTORY_REG(ImgRawDecodePostHandle)
```

## Brief

Convert the image from YUV to Raw.

## Inputs

- img_channel_0: A 2D Tensor, format is ND, dtype is uint16, shape is (h, w).
The input image of channel 0.
- img_channel_1: A 2D Tensor, format is ND, dtype is uint16, shape is (h, w).
The input image of channel 1.
- img_channel_2: A 2D Tensor, format is ND, dtype is uint16, shape is (h, w).
The input image of channel 2.
- img_channel_3: A 2D Tensor, format is ND, dtype is uint16, shape is (h, w).
The input image of channel 3.
- img_size: A 1D Tensor, format is ND, dtype is int32, shape is (2,).
The data is h_out and w_out, which indicates the output height and width.
- gamma: A 1D Tensor, format is ND, dtype is float32, shape is (4,).

## Outputs

raw_img: A 2D Tensor, format is ND, dtype is uint16, shape is (h_out, w_out).
The output raw image. 

## Attributes

bayer_pattern: A optional string. Choice calculate mode, the value must
be one of ["binning", "quad"]. Default: "binning".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 img_channel_0: uint16
- input1 img_channel_1: uint16
- input2 img_channel_2: uint16
- input3 img_channel_3: uint16
- input4 img_size: int32
- input5 gamma: float32
- output0 raw_img: uint16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
