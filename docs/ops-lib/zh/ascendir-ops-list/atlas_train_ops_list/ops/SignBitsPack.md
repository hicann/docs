# SignBitsPack

```c
REG_OP(SignBitsPack)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_UINT8}))
    .REQUIRED_ATTR(size, Int)
    .OP_END_FACTORY_REG(SignBitsPack)
```

## Brief

SignBitsPack.

## Inputs

one input, including:
x: A 1D Tensor of float32 or float16.

## Outputs

y: A 2D Tensor of type uint8 with shape (size, N)

## Attributes

size: first dim value of output tensor. Must be uint8 type.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: uint8


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
