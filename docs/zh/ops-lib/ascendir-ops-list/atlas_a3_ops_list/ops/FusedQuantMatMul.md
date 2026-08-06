# FusedQuantMatMul

```c
REG_OP(FusedQuantMatMul)
    .INPUT(x1, TensorType({DT_INT8}))
    .INPUT(x2, TensorType({DT_INT8, DT_INT4}))
    .OPTIONAL_INPUT(bias, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(x1_scale, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(x2_scale, TensorType({DT_UINT64, DT_INT64}))
    .OPTIONAL_INPUT(y_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(x1_offset, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(x2_offset, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(y_offset, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(x2_table, TensorType({DT_INT8}))
    .OPTIONAL_INPUT(x3, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT8}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(compute_type, Int, -1)
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(group_size, Int, -1)
    .ATTR(fused_op_type, String, "")
    .OP_END_FACTORY_REG(FusedQuantMatMul)
```

## Brief

FusedQuantMatMul computes a quant matmul + vector operation fused operator.

## Inputs

- x1: A matrix Tensor. The shape supports (m, k), and the format supports ND.
The data type supports int8. The m and k value must be in [1, 65535].
- x2: A matrix Tensor of quantized weight. The shape supports (k, n) for ND format if fused_op_type is not "swiglu".
only support (2, n1, k1, k0, n0) for NZ format, and ori shape should be (2, k, n) if fused_op_type is "swiglu".
The data type supports int8/int4. The k, n value must be in [1, 65535], k0 should be 16, n0 should be 64.
- bias: An Optional Tensor.
The shape supprts (1,) or (n,), format supports ND, the type supports int32, swiglu type is not supproted yet.
- x1_scale: An Optional Tensor for quantization parameters. It's not supported yet.
- x2_scale: An Optional Tensor for quantization parameters.
The type supports uint64, int64, format supports ND.
The shape supprts(1), (n) if fused_op_type is not "swiglu".
The shape supports (2, n) or (2 * n) if fused_op_type is "swiglu".
- y_scale:  An Optional Tensor for quantization parameters. It's not supported yet.
- x1_offset: An Optional Tensor for quantization parameters. It's not supported yet.
- x2_offset: An Optional Tensor for quantization parameters. It's not supported yet.
- y_offset: An Optional Tensor for quantization parameters. It's not supported yet.
- x2_table: An Optional Tensor for quantization parameters. It's not supported yet.
- x3: An Optional tensor.
The data type supports float only.
The shape support (n,), only support fused_op_type is "swiglu" and output type is int8 for quant scale fp16 to int8

## Outputs

y: A matrix Tensor. The data type support int8, float16. The format supports ND.

## Attributes

- dtype: An int32. The data type of y. It supports 1(float16) and 2(int8).
- compute_type: An int32. It's compute type. It's not supported yet.
- transpose_x1: A bool. x1 is transposed if true. Default: false.
When transpose_x1 is true, x1's shape is (k, m). Currently, it should always be false.
- transpose_x2: A bool. x2 is transposed if true. Default: false.
When transpose_x2 is true, x2's shape is (n, k). Currently, it should always be false.
- group_size: An int32. It's not supported yet.
- fused_op_type: A string. The fused_op_type include "add","mul","gelu_erf","gelu_tanh","relu","swiglu".
Currently, only "relu" and "swiglu" is supported.
Default type is defined as "".
"relu":
out = relu(matmul(x1, x2) + bias) * x2_scale.
"swiglu":
out = silu(matmul(x1, x2[0]) * x2_scale[0]) * (matmul(x1, x2[1]) * x2_scale[1]) * x3.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int4,int8
- input1 x2: int4,int8
- input2 bias: bfloat16,float16,float32,int32
- input3 x1_scale: float32
- input4 x2_scale: bfloat16,float32
- input5 y_scale: uint64
- input6 x1_offset: float32
- input7 x2_offset: float32
- input8 y_offset: float32
- input9 x2_table: int8
- input10 x3: float32
- output0 y: bfloat16,float16


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
