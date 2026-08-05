# ImgToTensor

```c
REG_OP(ImgToTensor)
    .INPUT(x, TensorType({DT_UINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(ImgToTensor)
```

## Brief

ImgToTensor: Convert image to tensor 

## Inputs

- image: A 4-D Tensor. type support uint8, format support NCHW or NHWC

## Outputs

- y: A 4-D Tensor. type support float, format support NCHW

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 x: uint8
- output0 y: float32

## Attention Constraints

This operator will be deprecated in the future. 

## Third-party framework compatibility

Compatible with pytorch ToTensor operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
