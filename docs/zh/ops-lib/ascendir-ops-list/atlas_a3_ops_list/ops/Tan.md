# Tan

```c
REG_OP(Tan)
    .INPUT(x, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_DOUBLE, DT_COMPLEX64,
                          DT_COMPLEX128, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128, DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(Tan)
```

## Brief

Computes tan of "x" element-wise.

## Inputs

One input:
x: A ND Tensor. Must be one of the following types: bfloat16, float16, float32, double,
complex64, complex128, int32, int64.

## Outputs

y: An ND or 5HD tensor. Support 1D ~ 8D. A ND Tensor with the same dtype and shape of input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Tan.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
