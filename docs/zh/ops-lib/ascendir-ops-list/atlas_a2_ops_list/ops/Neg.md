# Neg

```c
REG_OP(Neg)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
                          DT_INT8, DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
                           DT_INT8, DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Neg)
```

## Brief

Computes numerical negative value element-wise (y = -x)

## Inputs

One input:
x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
float16, float32, int32, int64, complex64, complex128, bfloat16, int8, float64.

## Outputs

y: A ND Tensor. Has the same dtype and format as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int32,int64
- output0 y: bfloat16,float16,float32,int8,int32,int64
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int32,int64
- output0 y: complex64,complex128,double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator Neg.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
