# BatchMatMulV2

```c
REG_OP(BatchMatMulV2)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8, DT_INT4, DT_BF16, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8, DT_INT4}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .ATTR(adj_x1, Bool, false)
    .ATTR(adj_x2, Bool, false)
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(BatchMatMulV2)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a @ b" .

## Inputs

Four inputs, including:
- x1: A matrix Tensor. Must be one of the following types: float16,
float32, int32, int8, int4, bfloat16, hifloat8. 2D-6D. Has format [ND, NHWC, NCHW].
- x2: A matrix Tensor. Must be one of the following types: float16,
float32, int32, int8, int4, bfloat16, hifloat8. 2D-6D. Has format [ND, NHWC, NCHW].
- bias: A optional Tensor. Must be one of the following types:
float16, float32, int32, bfloat16. Has format [ND, NHWC, NCHW].
- offset_w: A optional Tensor. Must be one of the following types:
int8, int4. Has format [ND, NHWC, NCHW].

## Outputs

y: The result matrix Tensor. Must be one of the following types: float16,
float32, int32, bfloat16, hifloat8. 2D-6D. Has format [ND, NHWC]. Has the same shape
length as "x1" and "x2".

## Attributes

- adj_x1: A bool. If True, changes the shape of "x1" from [B, M, K] to
[B, K, M] before multiplication.
- adj_x2: A bool. If True, changes the shape of "x2" from [B, K, N] to
[B, N, K] before multiplication.
- offset_x: An optional integer for quantized BatchMatMulV2.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16
- input1 x2: float16
- input2 bias: float16
- output0 y: float16,float32
### AI CPU
- input0 x1: float32
- input1 x2: float32
- output0 y: float32

## Attention Constraints

if performances better in format NZ, please close
"MatmulTransdataFusionPass" in fusion configuration.

## Third-party framework compatibility

Compatible with the TensorFlow operator BatchMatmul.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
