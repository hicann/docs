# MatMulV2

```c
REG_OP(MatMulV2)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8, DT_INT4}))
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(MatMulV2)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a @ b".

## Inputs

Four inputs, including:
- x1: A matrix Tensor. 2D. Must be one of the following types: float32,
float16, int32, int8, int4, bfloat16, hifloat8. Has format [ND, NHWC, NCHW].
- x2: A matrix Tensor. 2D. Must be one of the following types: float32,
float16, int32, int8, int4, bfloat16, hifloat8. Has format [ND, NHWC, NCHW].
- bias: A 1D Tensor. Must be one of the following types: float32,
float16, int32, bfloat16. Has format [ND, NHWC, NCHW].
- offset_w: A Optional 1D Tensor for quantized inference. Type is int8, int4, bfloat16.
Reserved.

## Outputs

y: The result matrix Tensor. 2D. Must be one of the following types: float32,
float16, int32, bfloat16, hifloat8. Has format [ND, NHWC, NCHW].

## Attributes

- transpose_x1: A bool. If True, changes the shape of "x1" from [K, M] to
[M, K] before multiplication.
- transpose_x2: A bool. If True, changes the shape of "x2" from [N, K] to
[K, N] before multiplication.
- offset_x: An optional integer for quantized MatMulV2.
The negative offset added to the input x1 for int8 type. Ensure offset_x
within the effective range of int8 [-128, 127]. Defaults to "0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16
- input1 x2: float16
- input2 bias: float16
- output0 y: float16,float32

## Attention Constraints

if performances better in format NZ, please close
"MatmulTransdataFusionPass" in fusion configuration.

## Third-party framework compatibility

Compatible with the TensorFlow operator MatMul.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
