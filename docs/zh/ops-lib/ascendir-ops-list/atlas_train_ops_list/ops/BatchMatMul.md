# BatchMatMul

```c
REG_OP(BatchMatMul)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_HIFLOAT8}))
    .ATTR(adj_x1, Bool, false)
    .ATTR(adj_x2, Bool, false)
    .OP_END_FACTORY_REG(BatchMatMul)
```

## Brief

Multiplies matrix "a" by matrix "b", producing "a @ b".

## Inputs

Two inputs, including:
- x1: A matrix Tensor. Must be one of the following types: float16,
float32, int32, bfloat16, hifloat8. 2D-6D. Has format [ND, NHWC, NCHW].
- x2: A matrix Tensor. Must be one of the following types: float16,
float32, int32, bfloat16, hifloat8. 2D-6D. Has format [ND, NHWC, NCHW].

## Outputs

y: The result matrix Tensor. Must be one of the following types: float16,
float32, int32, bfloat16, hifloat8. 2D-6D. Has format [ND, NHWC, NCHW]. BatchMatMul supports broadcasting in the batch dimensions.

## Attributes

- adj_x1: A bool. If True, changes the shape of "x1" from [B, M, K]
to [B, K, M] before multiplication.
- adj_x2: A bool. If True, changes the shape of "x2" from [B, K, N]
to [B, N, K] before multiplication.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int32
- input1 x2: complex64,complex128,double,float16,float32,int32
- output0 y: complex64,complex128,double,float16,float32,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator BatchMatmul.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
