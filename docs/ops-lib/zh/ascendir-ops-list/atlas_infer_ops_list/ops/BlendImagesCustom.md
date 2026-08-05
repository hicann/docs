# BlendImagesCustom

```c
REG_OP(BlendImagesCustom)
    .INPUT(rgb, TensorType({DT_UINT8}))
    .INPUT(alpha, TensorType({DT_UINT8}))
    .INPUT(frame, TensorType({DT_UINT8}))
    .OUTPUT(out, TensorType({DT_UINT8}))
    .OP_END_FACTORY_REG(BlendImagesCustom)
```

## Brief

Generate rgb and frame images into a out image with alpha transparency. 

## Inputs

- rgb: A Int, dtype is uint8, rgb images data.
- alpha: A Int, dtype is uint8, alpha transparency images data.
- frame: A Int, dtype is uint8, frame images data.

## Outputs

- out: The out tensor. Dtype is same as rgb.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 rgb: uint8
- input1 alpha: uint8
- input2 frame: uint8
- output0 out: uint8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
