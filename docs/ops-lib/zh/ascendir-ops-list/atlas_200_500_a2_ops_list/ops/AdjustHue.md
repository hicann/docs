# AdjustHue

```c
REG_OP(AdjustHue)
    .INPUT(images, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .INPUT(delta, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT,DT_UINT8}))
    .ATTR(data_format, String, "HWC")
    .OP_END_FACTORY_REG(AdjustHue)
```

## Brief

Adjust the hue of one or more images . 

## Inputs

Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three. Inputs include:
- images: Images to adjust. Must be one of the following types:uint8, float16, float32.
At least 3-D. The format could be NHWC, NCHW or ND.
- delta: A Tensor of type float. A float delta to add to the hue .

## Outputs

y: Images to adjust. Must be one of the following types:uint8, float16, float32.
At least 3-D. The format could be NHWC, NCHW or ND. 

## Attributes

- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float16,float32
- input1 delta: float32
- output0 y: float16,float32

## Attention Constraints

Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 

## Third-party framework compatibility

Compatible with tensorflow AdjustHue operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
