# RsqrtGrad

```c
REG_OP(RsqrtGrad)
    .INPUT(y, TensorType({UnaryDataType, DT_INT32, DT_INT8, DT_BF16}))
    .INPUT(dy, TensorType({UnaryDataType, DT_INT32, DT_INT8, DT_BF16}))
    .OUTPUT(z, TensorType({UnaryDataType, DT_INT32, DT_INT8, DT_BF16}))
    .OP_END_FACTORY_REG(RsqrtGrad)
```

## Brief

Computes the backpropagation of the square root operation.

## Inputs

Two inputs, including:
- y: An NCHW, NHWC, ND tensor. Support 1D ~ 8D. Must be one of the following types:
float, int32, int8, double, complex64, complex128, float16, bfloat16.
- dy: A ND tensor of the same dtype, shape and format as "y".

## Outputs

z: A ND tensor of the same dtype, shape and format as "y".
@see Matmul() | Rsqrt ()

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: bfloat16,float16,float32,int8,int32
- input1 dy: bfloat16,float16,float32,int8,int32
- output0 z: bfloat16,float16,float32,int8,int32
### AI CPU
- input0 y: complex64,complex128,double,float16,float32,int8,int32
- input1 dy: complex64,complex128,double,float16,float32,int8,int32
- output0 z: complex64,complex128,double,float16,float32,int8,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator RsqrtGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
