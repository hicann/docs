# MatMul

```c
REG_OP(MatMul)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .ATTR(transpose_x1, Bool, false)
    .ATTR(transpose_x2, Bool, false)
    .OP_END_FACTORY_REG(MatMul)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a @ b".

## Inputs

Three inputs, including:
- x1: A matrix Tensor. 2D. Must be one of the following types: float16,
float32, int32, bfloat16, hifloat8. Has format [ND, NHWC, NCHW].
- x2: A matrix Tensor. 2D. Must be one of the following types: float16,
float32, int32, bfloat16, hifloat8. Has format [ND, NHWC, NCHW].
- bias: A optional 1D Tensor. Must be one of the following types: float16,
float32, int32, bfloat16. Has format [ND, NHWC, NCHW].

## Outputs

y: The result matrix Tensor. 2D. Must be one of the following types: float16,
float32, int32, hifloat8. Has format [ND, NHWC, NCHW].

## Attributes

- transpose_x1: A bool. If True, changes the shape of "x1" from [M, K] to
[K, M] before multiplication.
- transpose_x2: A bool. If True, changes the shape of "x2" from [K, N] to
[N, K] before multiplication.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,hifloat8,int8,int32
- input1 x2: bfloat16,float16,float32,hifloat8,int8,int32
- input2 bias: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,hifloat8,int32
### AI CPU
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- input2 bias: float16,float32,int32
- output0 y: float16,float32,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator MatMul.


---

[Back to Operator Specifications (Ascend950)](../README.md)
