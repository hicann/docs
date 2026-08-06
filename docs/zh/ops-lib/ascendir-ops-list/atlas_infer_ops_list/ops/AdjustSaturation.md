# AdjustSaturation

```c
REG_OP(AdjustSaturation)
    .INPUT(images, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OP_END_FACTORY_REG(AdjustSaturation)
```

## Brief

Adjust the saturation of one or more images . 

## Inputs

Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three. Inputs include:
- images: A Tensor of type float. Images to adjust. At least 3-D. The format
must be NHWC.
- scale: A Tensor of type float. A float scale to add to the saturation .

## Outputs

y: A Tensor of type float. The format must be NHWC. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float16,float32
- input1 scale: float32
- output0 y: float16,float32

## Attention Constraints

Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 

## Third-party framework compatibility

Compatible with tensorflow AdjustSaturation operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
