# Ger

```c
REG_OP(Ger)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(Ger)
```

## Brief

Computes the outer product of two 1D vectors . 

## Inputs

The input x1 and x2 has to be a 1D vector.Inputs include:
- x1:A Tensor. Must be one of the following types: float16, float32, bfloat16.
Shape is [N] . 
- x2:A Tensor. Must have the same type as x. Shape is [M] .

## Outputs

y:A Tensor. Has the same type as x . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
