# ImgRawDecodePostHandleV2

```c
REG_OP(ImgRawDecodePostHandleV2)
    .INPUT(img_channel_0, TensorType({DT_UINT16}))
    .INPUT(img_channel_1, TensorType({DT_UINT16}))
    .INPUT(img_channel_2, TensorType({DT_UINT16}))
    .INPUT(img_channel_3, TensorType({DT_UINT16}))
    .INPUT(gamma, TensorType({DT_FLOAT}))
    .INPUT(bayer_coordinate, TensorType({DT_INT32}))
    .INPUT(bayer_params, TensorType({DT_FLOAT}))
    .INPUT(bayer_ptn, TensorType({DT_INT32}))
    .OUTPUT(raw_img, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(ImgRawDecodePostHandleV2)
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
- gamma: A 1D Tensor, dtype is float32, format is ND, shape is (4,).
- bayer_coordinate: A 1D Tensor, format is ND, dtype is int32, shape is (4,).
The data is supplied as [lt_x, lt_y, rb_x, rb_y], where the (lt_x, lt_y), (rb_x, rb_y)
are the left top and right bottom coordinates, respectively.
- bayer_params: A 1D Tensor, format is ND, dtype is float32, shape is (8,).
The data is supplied as
[r_gain, g_gain, b_gain, iso, ev_gain, iso_long, evSL, exposure_gain].
- bayer_ptn: A 1D Tensor, format is ND, dtype is int32, shape is (4,).
The bayer_ptn is used as index to obtain the value of rgb_gain.

## Outputs

raw_img: A 2D Tensor, format is ND, dtype is float32,
shape is (h_out, w_out), where h_out = rb_y - rb_x, w_out = lt_y - lt_x.
The output raw image. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 img_channel_0: uint16
- input1 img_channel_1: uint16
- input2 img_channel_2: uint16
- input3 img_channel_3: uint16
- input4 gamma: float32
- input5 bayer_coordinate: int32
- input6 bayer_params: float32
- input7 bayer_ptn: int32
- output0 raw_img: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
