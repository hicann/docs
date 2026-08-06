# QuantBatchMatmulV4

```c
REG_OP(QuantBatchMatmulV4)
    .INPUT(x1, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_INT8}))
    .INPUT(x2, TensorType({DT_FLOAT4_E2M1, DT_INT4, DT_INT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT32}))
    .OPTIONAL_INPUT(x1_scale, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT8_E8M0, DT_FLOAT32}))
    .OPTIONAL_INPUT(x2_scale, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT8_E8M0, DT_UINT64, DT_FLOAT32}))
    .OPTIONAL_INPUT(y_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(x1_offset, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(x2_offset, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(y_offset, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(x2_table, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(compute_type, Int, -1)
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(group_size, Int, -1)
    .OP_END_FACTORY_REG(QuantBatchMatmulV4)
```

## Brief

The fusion operator of antiquant and matmul for A8W4, MxA8W4, and A8W8.

## Inputs

- x1: A matrix Tensor. The shape supports (m, k), and the format supports ND.
The data type supports float8_e5m2, float8_e4m3fn, int8. The m and k value must be in [1, 65535]. The k value
must be in [1, 65535] and must be a multiple of 64.
- x2: A matrix Tensor of quantized weight. The shape supports (n, k), and the format supports ND/FRACTAL_NZ.
- In MxA8W4 scenario:
For ND format, the data type supports float4_e2m1. For FRACTAL_NZ format, the data type supports float4_e2m1.
- In A8W4 scenario:
The data type supports float4_e2m1.
The k, n value must be in [1, 65535] and k, n value must be a multiple of 64.
The shape must be (k1, n1, n0, k0) (n0 = 16, k0 = 32) when the format is FRACTAL_NZ.
- In A8W8 scenario: The data type supports int8.
- bias: An Optional Tensor.
The shape supprts(1, n), format supports ND, the type supports bfloat16, float16, float32.
- x1_scale: An Optional Tensor for quantization parameters.
The type supports float8_e8m0, float16, bfloat16, format supports ND.
The shape supprts(m, k/group_size) when type is float8_e8m0, float32.
The type bfloat16, bfloat16 is not supported yet.
- x2_scale: An Optional Tensor for quantization parameters.
The type supports float8_e8m0, bfloat16, float16, uint64, format supports ND, The shape supports (n, ceildiv(k, group_size)).
- In A8W8 scenario: The shape supports (ceildiv(k, group_size_k), ceildiv(n, group_size_n)). The type supports float32.
- y_scale: An Optional Tensor for quantization parameters.
The type support uint64, format supports ND, The shape supprts(1, n).
- x1_offset: An Optional Tensor for quantization parameters. It's not supported yet.
- x2_offset: An Optional Tensor for quantization parameters. It's not supported yet.
- y_offset: An Optional Tensor for quantization parameters. It's not supported yet.
- x2_table: An Optional Tensor for quantization parameters. It's not supported yet.

## Outputs

y: A matrix Tensor. The data type support bfloat16, float16. The format supports ND.

## Attributes

- dtype: An int32. The data type of y. It supports 1(float16) and 27(bfloat16).
- compute_type: An int32. It's compute type. The value must be -1(auto) or 4(f8f4). Default -1.
- transpose_x1: A bool. x1 is transposed if true. Default: false.
When transpose_x1 is true, x1's shape is (k, m). Currently, it should always be false.
- transpose_x2: A bool. x2 is transposed if true. Default: false.
When transpose_x2 is true, x2's shape is (n, k), x2_scale's shape should be (n, k / group_size).
Currently, it should always be true.
In A8W8 scenario, when transpose_x2 is true, x2_scale's shape should be
(ceildiv(n, group_size_n), ceildiv(k, group_size_k)).
- group_size: An int32. Default: -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int8
- input1 x2: int8
- input2 bias: bfloat16,int32
- input3 x1_scale: float32
- input4 x2_scale: bfloat16,float32,int64,uint64
- input5 y_scale: uint64
- input6 x1_offset: float32
- input7 x2_offset: float32
- input8 y_offset: float32
- input9 x2_table: int8
- output0 y: bfloat16,float16,int8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
