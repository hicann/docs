# Equal

```c
REG_OP(Equal)
    .INPUT(x1, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT32, DT_INT8, DT_UINT8,
                           DT_DOUBLE, DT_INT16, DT_INT64, DT_COMPLEX64,
                           DT_COMPLEX128, DT_QUINT8, DT_QINT8, DT_QINT32,
                           DT_STRING, DT_BOOL}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT32, DT_INT8, DT_UINT8,
                           DT_DOUBLE, DT_INT16, DT_INT64, DT_COMPLEX64,
                           DT_COMPLEX128, DT_QUINT8, DT_QINT8, DT_QINT32,
                           DT_STRING, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(Equal)
```

## Brief

Returns the truth value of (x = y) element-wise. Support broadcasting operations. 

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types:
   bfloat16, float16, float32, int32, int8, uint8, double, int16, int64, complex64,
   complex128, quint8, qint8, qint32, string, bool. the format can be [NCHW, NHWC, ND]
- x2: A ND Tensor of the same dtype and format as "x1".

## Outputs

y: A ND Tensor. Has the bool dtype. True means x1 == x2, false means x1 != x2.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bool,float16,float32,int8,int32,int64,uint8,uint64
- input1 x2: bool,float16,float32,int8,int32,int64,uint8,uint64
- output0 y: bool
### AI CPU
- input0 x1: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16,uint32,uint64
- input1 x2: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16,uint32,uint64
- output0 y: bool

## Third-party framework compatibility

Compatible with the TensorFlow operator Equal.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
