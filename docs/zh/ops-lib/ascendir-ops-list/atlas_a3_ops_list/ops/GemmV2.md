# GemmV2

```c
REG_OP(GemmV2)
    .INPUT(a, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(b, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(alpha, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(beta, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(c, TensorType({DT_FLOAT}))
    .OUTPUT(c, TensorType({DT_FLOAT}))
    .ATTR(transpose_a, Bool, false)
    .ATTR(transpose_b, Bool, false)
    .OP_END_FACTORY_REG(GemmV2)
```

## Brief

GemmV2 matrix "a" by matrix "b" and add matrix "c", producing "alpha * op(a) * op(b) + beta * op(c)". 

## Inputs

Four inputs, including:
- a: A matrix Tensor. 2D. Must be one of the following types: bfloat16,
float16. Has format [ND].
- b: A matrix Tensor. 2D. Must be one of the following types: bfloat16,
float16. Has format [ND].
- alpha: A 1D Tensor. Must be one of the following types: bfloat16,
float16. Has format [ND]. 
- beta: A 1D Tensor. Must be one of the following types: bfloat16,
float16. Has format [ND]. 
- c: A matrix Tensor. 2D. Must be one of the following types: bfloat16,
float16. Has format [ND].

## Outputs

c: The result matrix Tensor. 2D. Must be one of the following types: bfloat16,
float16. Has format [ND]. 

## Attributes

- transpose_a: A bool. If True, changes the shape of "a" from [M, K] to
[K, M] before multiplication.
- transpose_b: A bool. If True, changes the shape of "b" from [K, N] to
[N, K] before multiplication. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 a: bfloat16,float16
- input1 b: bfloat16,float16
- input2 alpha: bfloat16,float16
- input3 beta: bfloat16,float16
- input4 c: float32
- output0 c: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
