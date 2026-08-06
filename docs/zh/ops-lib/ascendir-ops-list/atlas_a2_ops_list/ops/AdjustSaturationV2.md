# AdjustSaturationV2

```c
REG_OP(AdjustSaturationV2)
    .INPUT(images, TensorType({DT_UINT8}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_UINT8}))
    .ATTR(data_format, String, "CHW")
    .OP_END_FACTORY_REG(AdjustSaturationV2)
```

## Attributes

- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "CHW".
Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 images: uint8
- input1 scale: float32
- output0 y: uint8

## Attention Constraints

- This operator will be deprecated in the future.
- Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 
@ Third-party framework compatibility
Compatible with Pytorch AdjustSaturation operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
