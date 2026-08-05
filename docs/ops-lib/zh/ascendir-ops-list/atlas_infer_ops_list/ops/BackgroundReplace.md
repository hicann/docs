# BackgroundReplace

```c
REG_OP(BackgroundReplace)
    .INPUT(bkg, TensorType({ DT_UINT8, DT_FLOAT16 }))
    .INPUT(src, TensorType({ DT_UINT8, DT_FLOAT16 }))
    .INPUT(mask, TensorType({ DT_FLOAT16, DT_FLOAT16 }))
    .OUTPUT(out, TensorType({ DT_UINT8, DT_FLOAT16 }))
    .OP_END_FACTORY_REG(BackgroundReplace)
```

## Brief

Replace Background to the image.
- bkg: A tensor of the type DT_UINT8, DT_FLOAT16.
- src:A tensor of the type DT_UINT8, DT_FLOAT16.
- mask:A tensor of the type DT_FLOAT16.
- out: A tensor of the type DT_UINT8, DT_FLOAT16.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bkg: float16,uint8
- input1 src: float16,uint8
- input2 mask: float16
- output0 out: float16,uint8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
