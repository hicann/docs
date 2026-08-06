# DecodeGif

```c
REG_OP(DecodeGif)
    .INPUT(contents, TensorType({DT_STRING}))
    .OUTPUT(image, TensorType({DT_UINT8}))
    .OP_END_FACTORY_REG(DecodeGif)
```

## Brief

Decode the frame(s) of a GIF-encoded image to a uint8 tensor . 

## Inputs

contents: A Tensor of type string. 0-D. The GIF-encoded image. 

## Outputs

image: A Tensor of type uint8. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 contents: string
- output0 image: uint8

## Third-party framework compatibility

Compatible with tensorflow DecodeGif operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
