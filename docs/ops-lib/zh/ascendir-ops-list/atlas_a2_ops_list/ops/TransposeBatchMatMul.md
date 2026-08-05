# TransposeBatchMatMul

```c
REG_OP(TransposeBatchMatMul)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(scale, TensorType({DT_INT64, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8}))
    .ATTR(perm_x1, ListInt, {})
    .ATTR(perm_x2, ListInt, {})
    .ATTR(perm_y, ListInt, {})
    .ATTR(enable_hf32, Bool, false)
    .ATTR(batch_split_factor, Int, 1)
    .OP_END_FACTORY_REG(TransposeBatchMatMul)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a @ b". 

## Inputs

Four inputs, including:
- x1: A matrix tensor. Must be one of the following types:
float32, float16, bfloat16. 3D. Has format ND.
- x2: A matrix tensor. Must be one of the following types:
float32, float16, bfloat16. 3D. Has format ND.
- bias: An optional tensor. Bias for batchmatmul. Must be one of the following types:
float32, float16, bfloat16. 1D. Has format ND.
- scale: A matrix tensor, quantization parameter.
Must be one of the following types: uint64, int64. The format
supports ND. The shape is 1D (t,), with t equal to b*n, where b, n is the same as that of x2.

## Outputs

y: The result matrix tensor. 3D. Must be one of the following
types: float32, float16, int8, bfloat16. 3D. Has format ND. 

## Attributes

Four attributes, including:
- perm_x1: A list int. "x1" is permuted to shape [B, M, K] before multiplication, the default value is no permutation.
- perm_x2: A list int. "x2" is permuted to shape [B, K, N] before multiplication, the default value is no permutation.
- perm_y: A list int. "y" is permuted after multiplication.
- enable_hf32: An optional bool. If True, enable enable_hi_float_32_execution.
- batch_split_factor: An optional int. Declares factor of output_batch. Default to be 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 bias: bfloat16,float16,float32
- input3 scale: int64,uint64
- output0 y: bfloat16,float16,float32,int8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
