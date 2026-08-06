# QuantMatmulReduceSum

```c
REG_OP(QuantMatmulReduceSum)
    .INPUT(x1, TensorType({DT_INT8}))
    .INPUT(x2, TensorType({DT_INT8}))
    .INPUT(dims, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(bias, TensorType({DT_BF16}))
    .OPTIONAL_INPUT(x1_scale, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(x2_scale, TensorType({DT_BF16}))
    .OPTIONAL_INPUT(y_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(x1_offset, TensorType({DT_BF16}))
    .OPTIONAL_INPUT(x2_offset, TensorType({DT_BF16}))
    .OPTIONAL_INPUT(y_offset, TensorType({DT_BF16}))
    .OPTIONAL_INPUT(x2_table, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_BF16}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(compute_type, Int, -1)
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(group_size, Int, -1)
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(QuantMatmulReduceSum)
```

## Brief

The fusion operator of QuantBatchMatmul and ReduceSum.

## Inputs

- x1: A matrix tensor. The shape supports (batch, m, k), and the format supports ND. The data type supports int8.
- x2: A matrix tensor of quantized weight. The shape supports (batch, k, n), and the format supports FRACTAL_NZ. The data type supports int8.
- dims: A 1D list or tuple of int64. Specifies the dimensions to reduce.
- bias: Reserved parameter, not supported now, please pass nullptr.
- x1_scale: A tensor for x1 quantization parameters. The type supports float32, format supports ND, The shape supprts(b, m).
- x2_scale: A tensor for x2 quantization parameters. The type supports bfloat16, format supports ND. The shape supprts(n,).
- y_scale: Reserved parameter, not supported now, please pass nullptr.
- x1_offset: Reserved parameter, not supported now, please pass nullptr.
- x2_offset: Reserved parameter, not supported now, please pass nullptr.
- y_offset: Reserved parameter, not supported now, please pass nullptr.
- x2_table: Reserved parameter, not supported now, please pass nullptr.

## Outputs

y: A matrix tensor. The data type is bfloat16. The format supports ND. 
Atlas A2 Trainging Series Product/Atlas 800I A2 Inference Product or Atlas A3 Training Series Product: 
| x1   | x2   | x1Scale  | x2Scale  | yScale | x1Offset | x2Offset | yOffset | bias  | out     |
|------|------|----------|----------|--------|----------|----------|---------|-------|---------|
| INT8 | INT8 | FLOAT32  | BFLOAT16 | null   | null     | null     | null    | null  |BFLOAT16 |

## Attributes

- dtype: A Int. Declare the output dtype, supports 27(bfloat16).
- compute_type: Reserved attributes, not supported now. Default is -1.
- transpose_x1: A bool. If true, changes the shape of "x1" from [m, k] to [k, m] before multiplication. Default: false. Only supports false now.
- transpose_x2: A bool. If true, changes the shape of "x2" from [k, n] to [n, k] before multiplication. Default: false. Only supports false now.
- group_size: Reverved attributes, not supported now. Default is -1.
- keep_dims: A bool. If true, keeps the original input dims in the output. Default: false. Only support false now.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int8
- input1 x2: int8
- input2 dims: int64
- input3 bias: bfloat16
- input4 x1_scale: float32
- input5 x2_scale: bfloat16
- input6 y_scale: uint64
- input7 x1_offset: bfloat16
- input8 x2_offset: bfloat16
- input9 y_offset: bfloat16
- input10 x2_table: int8
- output0 y: bfloat16


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
