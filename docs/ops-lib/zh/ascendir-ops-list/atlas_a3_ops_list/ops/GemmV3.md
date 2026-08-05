# GemmV3

```c
REG_OP(GemmV3)
.INPUT(a, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_INT32}))
.INPUT(b, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_INT32}))
.OPTIONAL_INPUT(c, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_INT32}))
.OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_INT32}))
.ATTR(alpha, Float, 1.0)
.ATTR(beta, Float, 1.0)
.ATTR(transpose_a, Bool, false)
.ATTR(transpose_b, Bool, false)
.ATTR(enable_hf32, Bool, false)
.OP_END_FACTORY_REG(GemmV3)
```

## Brief

Performs Matrix-to-matrix Multiply,
producing y= alpha * a @ b + beta * c.

## Inputs

Three inputs, including:
- a: An matrix tensor. Must be one of the following types:float32, float16, bfloat16
int8, int32. Has format ND.
- b: An matrix tensor. Must be one of the following types:float32, float16, bfloat16
int8, int32. Has format ND.
- c: An optional matrix tensor. Must be one of the following types:float32, float16, bfloat16
int8, int32. Has format ND.

## Outputs

y: The result matrix tensor. Must be one of the following types: float32,
float16, int8, int32. Has format [ND], the format should be equal to a.

## Attributes

Five attributes, including:
- alpha: An optional attribute, the type is float. Defaults to 1.0.
- beta: An optional attribute, the type is float. Defaults to 1.0.
- transpose_a: Optional. A bool. If True, changes the shape of "a" from
[M, K] to [K, M] before multiplication. Defaults to "false".
- transpose_b: Optional. A bool. If True, changes the shape of "b" from
[K, N] to [N, K] before multiplication. Defaults to "false".
- enable_hf32: Optional. A bool. If True, enable enable_hi_float_32_execution.
If False, do not enable enable_hi_float_32_execution.
Defaults to "false".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 a: bfloat16,float16
- input1 b: bfloat16,float16
- input2 c: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

For better performance, The k-axis must be aligned to 16 (input type
is float16) or 32 (input type is int8).


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
