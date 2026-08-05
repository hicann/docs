# SquaredDifference

```c
REG_OP(SquaredDifference)
    .INPUT(x1, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32,
                           DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x2, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32,
                           DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32,
                           DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(SquaredDifference)
```

## Brief

Returns (x1 - x2)(x1 - x2) element-wise. Support broadcasting operations.

## Inputs

Two inputs, including: 
- x1: A ND Tensor. Must be one of the following types: bfloat16, float16, float32,
float64, int32, int64, complex64, complex128.
- x2: A ND Tensor. Has the same dtype as "x1".
The shape of x1 and x2 must meet the requirements of the broadcast relationship. 

## Outputs

y: A ND Tensor. Has the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32,int64
- input1 x2: bfloat16,float16,float32,int32,int64
- output0 y: bfloat16,float16,float32,int32,int64
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int32,int64
- input1 x2: complex64,complex128,double,float16,float32,int32,int64
- output0 y: complex64,complex128,double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with TensorFlow operator SquaredDifference.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
