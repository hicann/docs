# GEMM

```c
REG_OP(GEMM)
    .INPUT(a, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT32}))
    .INPUT(b, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT32}))
    .INPUT(c, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT32}))
    .INPUT(alpha, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT32}))
    .INPUT(beta, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT32}))
    .ATTR(transpose_a, Bool, false)
    .ATTR(transpose_b, Bool, false)
    .OP_END_FACTORY_REG(GEMM)
```

## Brief

Performs Matrix-to-matrix Multiply,
producing y = alpha[0] * a @ b + beta[0] * c.

## Inputs

Five inputs, including:
- a: A matrix Tensor. Must be one of the following types:float32, float16,
int8, int32. Has format ND.
- b: A matrix Tensor. Must be one of the following types:float32, float16,
int8, int32. Has format ND.
- c: A matrix Tensor. Must be one of the following types:float32, float16,
int8, int32. Has format ND.
- alpha: A 1D Tensor. The shape of alpha is [1].Must be one of the
following types: float32, float16, int8, int32. Has format ND.
- beta: A 1D Tensor. The shape of beta is [1]. Must be one of the following
types: float32, float16, int8, int32. Has format ND.

## Outputs

y: The result matrix Tensor. Must be one of the following types: float32,
float16, int8, int32. Has format [ND], the format should be equal to a.

## Attributes

Two attributes, including:
- transpose_a: Optional. A bool. If True, changes the shape of "a" from
[M, K] to [K, M] before multiplication.
- transpose_b: Optional. A bool. If True, changes the shape of "b" from
[K, N] to [N, K] before multiplication.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 a: float16,float32,int8,int32
- input1 b: float16,float32,int8,int32
- input2 c: float16,float32,int8,int32
- input3 alpha: float16,float32,int8,int32
- input4 beta: float16,float32,int8,int32
- output0 y: float16,float32,int8,int32

## Attention Constraints

For better performance, The k-axis must be aligned to 16 (input type
is float16) or 32 (input type is int8).


---

[Back to Operator Specifications (Ascend950)](../README.md)
