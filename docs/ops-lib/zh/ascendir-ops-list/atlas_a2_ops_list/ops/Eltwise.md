# Eltwise

```c
REG_OP(Eltwise)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(N, Int)
    .ATTR(mode, Int, 1)
    .ATTR(coeff, ListFloat, {})
    .OP_END_FACTORY_REG(Eltwise)
```

## Brief

Compute elementwise modes, such as 0: PRODUCT, 1: SUM, 2: MAX

## Inputs

One input: An ND or 5HD tensor. Support 1D~8D.
x: the list of input data, the type of element in Tensor should be same.
  The max size of x is 32.
  Should met one of the following types: bfloat16, float16, float32. It's a dynamic input.

## Outputs

y: A ND Tensor. Has the same dtype and format as "x".

## Attributes

- N: A required attribute. the number of input x, max size is 32. Type is int.
- model: An optional attribute. Type is int. Defaults to "1".
   "0": product, "1": sum, "2": max.
- coeff: A required attribute. Must met all of following rules:
   Size of "coeff" must be equal to len("x") or is null.
   The absolute value of "coeff" must less than or equal to 1. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
