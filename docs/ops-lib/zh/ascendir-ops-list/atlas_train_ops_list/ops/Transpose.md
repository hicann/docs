# Transpose

```c
REG_OP(Transpose)
    .INPUT(x, TensorType({DT_BF16,      DT_FLOAT16,   DT_FLOAT,      DT_DOUBLE,   DT_INT64,       DT_INT32,
                          DT_UINT8,     DT_UINT16,    DT_UINT32,     DT_UINT64,   DT_INT8,        DT_INT16,
                          DT_COMPLEX32, DT_COMPLEX64, DT_COMPLEX128, DT_QINT8,    DT_QUINT8,      DT_QINT16,
                          DT_QUINT16,   DT_QINT32,    DT_BOOL,       DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(perm, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_BF16,      DT_FLOAT16,   DT_FLOAT,      DT_DOUBLE,   DT_INT64,       DT_INT32,
                           DT_UINT8,     DT_UINT16,    DT_UINT32,     DT_UINT64,   DT_INT8,        DT_INT16,
                           DT_COMPLEX32, DT_COMPLEX64, DT_COMPLEX128, DT_QINT8,    DT_QUINT8,      DT_QINT16,
                           DT_QUINT16,   DT_QINT32,    DT_BOOL,       DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OP_END_FACTORY_REG(Transpose)
```

## Brief

Permutes the dimensions according to perm.
The returned tensor's dimension i will correspond to the input dimension perm[i].

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types:
bfloat16, float16, float32, double, int64, int32, uint8, uint16, uint32, uint64, int8,
int16, complex32, complex64, complex128, qint8, quint8, qint16, quint16, qint32, bool, hifloat8, float8_e5m2,
float8_e4m3fn, and the maximum dimension should not exceed 8 dimensions,
and the shape should be consistent with output.
- perm: A Tensor of type int32 or int64. A permutation of the dimensions of "x", the value
should be within the range of [0, number of dimensions for self -1].

## Outputs

y: A Tensor. Has the same type as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex32,complex64,complex128,double,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 perm: int32,int64
- output0 y: bfloat16,bool,complex32,complex64,complex128,double,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bfloat16,bool,complex32,complex64,complex128,double,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 perm: int32,int64
- output0 y: bfloat16,bool,complex32,complex64,complex128,double,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Transpose.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
