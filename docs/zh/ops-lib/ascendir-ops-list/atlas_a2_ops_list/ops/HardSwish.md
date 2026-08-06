# HardSwish

```c
REG_OP(HardSwish)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(HardSwish)
```

## Brief

Compute hard_swish of "x" element-wise .

## Inputs

One input, including:
x: A Tensor. Must be one of the following types: float16, float32, bfloat16

## Outputs

y: A Tensor. Has the same type as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Torch operator HardSwish.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
