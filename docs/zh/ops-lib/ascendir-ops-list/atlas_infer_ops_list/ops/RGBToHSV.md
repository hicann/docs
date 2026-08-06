# RGBToHSV

```c
REG_OP(RGBToHSV)
    .INPUT(images, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE }))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE }))
    .OP_END_FACTORY_REG(RGBToHSV)
```

## Brief

Converts one or more images from RGB to HSV . 

## Inputs

Last dimension of input images must be size 3. Inputs include:
images: A Tensor. Must be one of the following types: float, double. 1-D or
higher rank. RGB data to convert. Last dimension must be size 3 . 

## Outputs

y: A Tensor. Has the same type as images . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

Outputs a tensor of the same shape as the images tensor, containing the HSV
value of the pixels. The output is only well defined if the value in images
are in [0,1] . 

## Third-party framework compatibility

Compatible with tensorflow RGBToHSV operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
