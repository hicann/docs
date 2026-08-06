# FusedMatMul

```c
REG_OP(FusedMatMul)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(x3, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8}))
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(enable_hf32, Bool, false)
    .ATTR(fused_op_type, String, "")
    .ATTR(inner_precise, Int, 1)
    .OP_END_FACTORY_REG(FusedMatMul)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a @ b".

## Inputs

Four inputs, including:
- x1: A matrix tensor. Must be one of the following types: float16,
bfloat16. The type of float32 is not supported right now.
- x2: A matrix tensor. Must be one of the following types: float16,
bfloat16. The type of float32 is not supported right now.
- bias: An optional tensor. 1D. Must be one of the following types: float32,
bfloat16, float16.
- x3: An optional tensor. For "add" and "mul", x3 is the fused matrix input. For "quant" and
"relu_quant", x3 must be a uint64 tensor with shape [1], carrying the encoded logical quantization parameter.

## Outputs

y: The result matrix tensor. Must be one of the following types: float16, bfloat16, float32, int8.

## Attributes

- transpose_x1: A bool. If True, changes the shape of "x1" from [M, K] to
[K, M] before multiplication.
- transpose_x2: A bool. If True, changes the shape of "x2" from [K, N] to
[N, K] before multiplication.
- enable_hf32: A bool. This input is not support right now.
- fused_op_type: A string. The fused_op_type include "","add","mul","gelu_erf","gelu_tanh","relu",
"quant","relu_quant".
Default type is defined as "".
- inner_precise: An int. 0 means high precision vector fusion, 1 means high performance vector fusion.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 bias: bfloat16,float16,float32
- input3 x3: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
