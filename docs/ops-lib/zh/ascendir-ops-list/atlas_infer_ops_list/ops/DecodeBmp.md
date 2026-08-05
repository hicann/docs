# DecodeBmp

```c
REG_OP(DecodeBmp)
    .INPUT(contents, TensorType({DT_STRING}))
    .OUTPUT(image, TensorType({DT_UINT8}))
    .ATTR(channels, Int, 0)
    .OP_END_FACTORY_REG(DecodeBmp)
```

## Brief

Bmp-decode an image. 

## Inputs

contents: A Tensor of type string. 0-D. The BMP-encoded image. 

## Outputs

image: A Tensor dtype of uint8.

## Attributes

channels: Decode the desired number of color channels of the image. An optional int, default is 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 contents: string
- output0 image: uint8

## Third-party framework compatibility

Compatible with tensorflow DecodeBmp operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
