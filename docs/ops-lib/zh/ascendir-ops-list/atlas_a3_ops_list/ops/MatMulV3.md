# MatMulV3

```c
REG_OP(MatMulV3)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8, DT_INT4}))
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(offset_x, Int, 0)
    .ATTR(opImplMode, Int, 0x1)
    .OP_END_FACTORY_REG(MatMulV3)
```

## Brief

Multiplies matrix "x1" by matrix "x2", producing "x1 * x2". 

## Inputs

Four inputs, including:
- x1: A matrix Tensor. 2D. Must be one of the following types: bfloat16,
float16, float32. Has format [ND, NHWC, NCHW].
- x2: A matrix Tensor. 2D/4D(NZ格式). Must be one of the following types: bfloat16,
float16, float32. Has format [ND, NHWC, NCHW, NZ].
- bias: A 1D Tensor. Must be one of the following types: float32,
float16, float32. Has format [ND, NHWC, NCHW]. 
- offset_w: An optional matrix Tensor. 2D. Must be one of the following
types: int8, int4.

## Outputs

y: The result matrix Tensor. 2D. Must be one of the following types: bfloat16,
float16, float32. Has format [ND, NHWC, NCHW]. 

## Attributes

- transpose_x1: A bool. If True, changes the shape of "x1" from [M, K] to
[K, M] before multiplication.
- transpose_x2: A bool. If True, changes the shape of "x2" from [K, N] to
[N, K] before multiplication.
- offset_x: An optional integer for quantized MatMulV2Compress.
The negative offset added to the input x1 for int8 type. Ensure offset_x
within the effective range of int8 [-128, 127]. Defaults to "0".
- enable_hf32: An optional bool for MatMulV3. If True, enable enable_hi_float_32_execution
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

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
