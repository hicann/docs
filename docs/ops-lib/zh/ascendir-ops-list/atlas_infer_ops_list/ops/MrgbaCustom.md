# MrgbaCustom

```c
REG_OP(MrgbaCustom)
    .INPUT(rgb, TensorType({ DT_UINT8 }))
    .INPUT(alpha, TensorType({ DT_UINT8 }))
    .OUTPUT(dst, TensorType({ DT_UINT8 }))
    .OP_END_FACTORY_REG(MrgbaCustom)
```

## Brief

Give transparency to the image.

## Inputs

- rgb: A tensor of the type DT_UINT8.
- alpha:A tensor of the type DT_UINT8.

## Outputs

- dst: A tensor of the type DT_UINT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 rgb: uint8
- input1 alpha: uint8
- output0 dst: uint8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
