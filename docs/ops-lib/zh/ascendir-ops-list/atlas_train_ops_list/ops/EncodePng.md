# EncodePng

```c
REG_OP(EncodePng)
    .INPUT(image, TensorType({DT_UINT8, DT_UINT16}))
    .OUTPUT(contents, TensorType({DT_STRING}))
    .ATTR(compression, Int, -1)
    .OP_END_FACTORY_REG(EncodePng)
```

## Brief

PNG-encode an image.

## Inputs

Input image must be unit8 or uint16 type. Inputs include:
image: is a 3-D uint8 or uint16 Tensor of shape [height, width, channels]
where channels is: 1: for grayscale; 2: for grayscale + alpha; 3: for RGB;
4: for RGBA. 

## Outputs

contents: 0-D. PNG-encoded image. 

## Attributes

compression: Compression level. An optional int, default is -1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 image: uint8,uint16
- output0 contents: string

## Third-party framework compatibility

Compatible with tensorflow EncodePng operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
