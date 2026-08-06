# HSVToRGB

```c
REG_OP(HSVToRGB)
    .INPUT(images, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE}))
    .OP_END_FACTORY_REG(HSVToRGB)
```

## Brief

Convert one or more images from HSV to RGB . 

## Inputs

Last dimension of input x must be size 3. Inputs include:
images: 1-D or higher rank. HSV data to convert. Last dimension must be size 3 . 

## Outputs

y:images converted to RGB . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

Input images currently supports DT_FLOAT, DT_DOUBLE .
Last dimension of input x must be size 3 . 

## Third-party framework compatibility

Compatible with tensorflow HSVToRGB operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
