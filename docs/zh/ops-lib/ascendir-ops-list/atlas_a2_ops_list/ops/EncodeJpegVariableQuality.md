# EncodeJpegVariableQuality

```c
REG_OP(EncodeJpegVariableQuality)
    .INPUT(images, TensorType({DT_UINT8}))
    .INPUT(quality, TensorType({DT_INT32}))
    .OUTPUT(contents, TensorType({DT_STRING}))
    .OP_END_FACTORY_REG(EncodeJpegVariableQuality)
```

## Brief

JPEG encode input image with provided compression quality. 

## Inputs

- images: image is a 3-D uint8 tensor of shape [height, width, channels].
- quality: int32 jpeg compression quality value between 0 and 100, 0-D tensor.

## Outputs

contents: an output string. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: uint8
- input1 quality: int32
- output0 contents: string

## Third-party framework compatibility.

Compatible with tensorflow EncodeJpegVariableQuality operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
