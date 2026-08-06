# Pow

```c
REG_OP(Pow)
    .INPUT(x1, "T1")
    .INPUT(x2, "T2")
    .OUTPUT(y, "T3")
    .DATATYPE(T1, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_INT8, DT_INT16,
                              DT_UINT8, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .DATATYPE(T2, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_INT8, DT_INT16,
                              DT_UINT8, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .DATATYPE(T3, Promote({"T1", "T2"}))
    .OP_END_FACTORY_REG(Pow)
```

## Brief

Computes the power of "x1" to "x2". Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types:
    bfloat16, float16, float32, int32, int64, int8, int16, uint8, double, complex64, complex128.
- x2: A ND Tensor of the same dtype as "x1".

## Outputs

y: A ND Tensor. Has the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int32,uint8
- input1 x2: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8
- input1 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with the TensorFlow operator Pow.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
