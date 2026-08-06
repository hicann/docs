# DualLevelQuantBatchMatmul

```c
REG_OP(DualLevelQuantBatchMatmul)
    .INPUT(x1, TensorType({DT_FLOAT4_E2M1}))
    .INPUT(x2, TensorType({DT_FLOAT4_E2M1}))
    .INPUT(x1_level0_scale, TensorType({DT_FLOAT}))
    .INPUT(x1_level1_scale, TensorType({DT_FLOAT8_E8M0}))
    .INPUT(x2_level0_scale, TensorType({DT_FLOAT}))
    .INPUT(x2_level1_scale, TensorType({DT_FLOAT8_E8M0}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, true)
    .ATTR(level0_group_size, Int, 512)
    .ATTR(level1_group_size, Int, 32)
    .OP_END_FACTORY_REG(DualLevelQuantBatchMatmul)
```

## Brief

The fusion operator of antiquant function and matmul.

## Inputs

- x1: A matrix tensor. Format supports ND. The type supports DT_FLOAT4_E2M1. Shape is [M, K].
- x2: A matrix tensor. Format supports NZ. The type supports DT_FLOAT4_E2M1. Shape is [N, K].
- x1_level0_scale: A matrix tensor. Format supports ND. The type supports DT_FLOAT.
First-level quantization parameter for x1. Shape is [M, Ceil(K/level0_group_size)].
- x1_level1_scale: A matrix tensor. Format supports ND. The type supports DT_FLOAT8_E8M0.
Second-level quantization parameter for x1. Shape is [M, Ceil(K/(2*level1_group_size)), 2].
- x2_level0_scale: A matrix tensor. Format supports ND. The type supports DT_FLOAT.
First-level quantization parameter for x2. Shape is [Ceil(K/level0_group_size), N].
- x2_level1_scale: A matrix tensor. Format supports ND. The type support DT_FLOAT8_E8M0.
Second-level quantization parameter for x2. Shape is [N, Ceil(K/(2*level1_group_size)), 2].
- bias: An Optional tensor. Shape support (N). Format support ND. The type support DT_FLOAT.

## Outputs

y: A matrix tensor. The format support ND. The type support float16, bfloat16.

## Attributes

- dtype: An int. Declare the output dtype, supports 1(float16), 27(bfloat16).
- transpose_x1: A bool. If True, changes the shape of "x1" from [M, K] to [K, M]. Now only support false.
Default value is false.
- transpose_x2: A bool. If True, changes the shape of "x2" from [K, N] to [N, K] and
"x2_level1_scale" from [Ceil(K/(2*level1_group_size)), N, 2] to [N, Ceil(K/(2*level1_group_size)), 2].
Now only support true. Default value is true.
- level0_group_size: An int. First-level quantization parameter. Size supports 512.
Default value is 512.
- level1_group_size: An int. Second-level quantization parameter. Size supports 32.
Default value is 32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float4_e2m1
- input1 x2: float4_e2m1
- input2 x1_level0_scale: float32
- input3 x1_level1_scale: float8_e8m0
- input4 x2_level0_scale: float32
- input5 x2_level1_scale: float8_e8m0
- input6 bias: float32
- output0 y: bfloat16,float16


---

[Back to Operator Specifications (Ascend950)](../README.md)
