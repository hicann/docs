# Diag

```c
REG_OP(Diag)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16, DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16, DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Diag)
```

## Brief

Create a diagonal tensor

## Inputs

One input, include:
x: A mutable Tensor with rank k, where k is at most 4. Must be one of the Must be one of the following types:
    bfloat16, float16, float32, double, int32, int64, complex64, complex128. Supported format list ["ND"]. 
    Note: bfloat16 is only supported on Ascend950PR/Ascend950DT.

## Outputs

y: A mutable Tensor. Has the same type as "x". Supported format list ["ND"]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,complex64,double,float16,float32,int32,int64
- output0 y: bfloat16,complex64,double,float16,float32,int32,int64
### AI CPU
- input0 x: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator Diag.


---

[Back to Operator Specifications (Ascend950)](../README.md)
