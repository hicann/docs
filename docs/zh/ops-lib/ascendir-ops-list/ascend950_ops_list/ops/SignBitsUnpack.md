# SignBitsUnpack

```c
REG_OP(SignBitsUnpack)
    .INPUT(x, TensorType({DT_UINT8}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(size, Int)
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(SignBitsUnpack)
```

## Brief

SignBitsUnpack.

## Inputs

one input, including:
x: A 1D Tensor of uint8.

## Outputs

y: A 2D Tensor of type float32 (float16) with shape (size, (x.shape * 8) / size),

## Attributes

- size: dim of out put tensor, defaults to 1. Must be int type.
- dtype: dtype of out put tensor: DT_FLOAT(0) or DT_FLOAT16(1).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: uint8
- output0 y: float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
