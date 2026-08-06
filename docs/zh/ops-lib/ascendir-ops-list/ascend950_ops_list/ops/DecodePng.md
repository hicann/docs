# DecodePng

```c
REG_OP(DecodePng)
    .INPUT(contents, TensorType({DT_STRING}))
    .OUTPUT(image, TensorType({DT_UINT8, DT_UINT16}))
    .ATTR(dtype, Type, DT_UINT8)
    .ATTR(channels, Int, 0)
    .OP_END_FACTORY_REG(DecodePng)
```

## Brief

PNG-decode an image.

## Inputs

contents: 0-D. PNG-decoded image.

## Outputs

image: is a 3-D uint8 or uint16 Tensor of shape [height, width, channels]
where channels is: 1: for grayscale; 2: for grayscale + alpha; 3: for RGB;
4: for RGBA . 

## Attributes

- channels: graph channels. An optional int, default is 0.
- dtype: type of image. An optional attribute, default is uint8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 contents: string
- output0 image: uint8,uint16

## Third-party framework compatibility

Compatible with tensorflow DecodePng operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
