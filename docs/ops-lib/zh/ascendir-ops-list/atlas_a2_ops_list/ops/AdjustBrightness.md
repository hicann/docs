# AdjustBrightness

```c
REG_OP(AdjustBrightness)
    .INPUT(images, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(delta, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(AdjustBrightness)
```

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 images: float16,float32
- input1 delta: float32
- output0 y: float16,float32

## Attention Constraints

- This operator will be deprecated in the future.
- Input images is a tensor of at least 3 dimensions. The last dimension is
interpretted as channels, and must be three . 
@ Third-party framework compatibility
Compatible with tensorflow AdjustBrightness operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
