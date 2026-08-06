# AdjustBrightnessV2

```c
REG_OP(AdjustBrightnessV2)
    .INPUT(images, TensorType({DT_UINT8}))
    .INPUT(factor, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_UINT8}))
    .OP_END_FACTORY_REG(AdjustBrightnessV2)
```

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 images: uint8
- input1 factor: float32
- output0 y: uint8

## Attention Constraints

- This operator will be deprecated in the future.
- Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 
@ Third-party framework compatibility
Compatible with tensorflow AdjustBrightness operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
