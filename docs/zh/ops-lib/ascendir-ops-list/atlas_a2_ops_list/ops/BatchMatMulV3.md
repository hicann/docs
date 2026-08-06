# BatchMatMulV3

```c
REG_OP(BatchMatMulV3)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8, DT_INT4}))
    .ATTR(adj_x1, Bool, false)
    .ATTR(adj_x2, Bool, false)
    .ATTR(offset_x, Int, 0)
    .ATTR(enable_hf32, Bool, false)
    .OP_END_FACTORY_REG(BatchMatMulV3)
```

## Brief

Multiplies matrix "x1" by matrix "x2", producing "x1 * x2".

## Inputs

Four inputs, including:
- x1: A matrix Tensor. Must be one of the following types: float16,
float32, bfloat16. 2D-6D. Has format [ND, NHWC, NCHW].
- x2: A matrix Tensor. Must be one of the following types: float16,
float32, bfloat16. 2D-6D. Has format [ND, NHWC, NCHW].
- bias: A optional Tensor. Must be one of the following types: float16,
float32, bfloat16. Has format [ND, NHWC, NCHW],
bfloat16 is only supported in Ascend 950 AI processor
- offset_w: A optional Tensor. Must be one of the following types:
int8, int4. Has format [ND, NHWC, NCHW].

## Outputs

y: The result matrix Tensor. Must be one of the following types: float16,
float32, bfloat16. 2D-6D. Has format [ND, NHWC, NCHW]. BatchMatMulV3 supports broadcasting in the batch dimensions.

## Attributes

- adj_x1: A bool. If True, changes the shape of "x1" from [B, M, K] to
[B, K, M] before multiplication.
- adj_x2: A bool. If True, changes the shape of "x2" from [B, K, N] to
[B, N, K] before multiplication.
- offset_x: An optional integer for quantized BatchMatMulV3.
- enable_hf32: An optional bool for BatchMatMulV3. If True, enable enable_hi_float_32_execution
before multiplication. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 bias: float16,float32
- input3 offset_w: int4,int8
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
