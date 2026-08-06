# MatMulV2CompressDequant

```c
REG_OP(MatMulV2CompressDequant)
    .INPUT(x1, TensorType({DT_INT8}))
    .INPUT(x2, TensorType({DT_INT8}))
    .INPUT(compress_index, TensorType({DT_INT8}))
    .INPUT(deq_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(bias, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(compress_info, ListInt, {1, 1, 1, 1, 1})
    .ATTR(offset_x, Int, 0)
    .ATTR(alg, String, "weight_unzip")
    .OP_END_FACTORY_REG(MatMulV2CompressDequant)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a * b". 

## Inputs

Five inputs, including:
- x1: A matrix Tensor. 2D. Must be one of the following types: int8.
- x2: A matrix Tensor. 2D. Must be one of the following types: int8.
- compress_index: A compress index matrix of type int8.
- bias: An optional Tensor. 1D. Must be one of the following types: int32.
- offset_w: An optional matrix Tensor. 2D. Must be one of the following
types: int8. 

## Outputs

y: The result matrix Tensor. 2D. Must be one of the following types: int32,
float16. 

## Attributes

- transpose_x1: A bool. If True, changes the shape of "x1" from [K, M] to
[M, K] before multiplication.
- transpose_x2: A bool. If True, changes the shape of "x2" from [N, K] to
[K, N] before multiplication.
- offset_x: An optional integer for quantized MatMulV2CompressDequant.
- tiling_k: An optional integer for binary quantized MatMulV2CompressDequant.
- tiling_n: An optional integer for binary quantized MatMulV2CompressDequant.
The negative offset added to the input x1 for int8 type. Ensure offset_x
within the effective range of int8 [-128, 127]. Defaults to "0". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int8
- input1 x2: int8
- input2 compress_index: int8
- input3 deq_scale: uint64
- input4 bias: int32
- input5 offset_w: int8

## Attention Constraints

if performances better in format NZ, please close
"MatmulTransdataFusionPass" in fusion configuration.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
