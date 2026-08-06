# Tril

```c
REG_OP(Tril)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16,
                          DT_INT8, DT_INT64, DT_QINT8, DT_QUINT8, DT_QINT32, DT_QUINT16, DT_QINT16,
                          DT_UINT16, DT_UINT32, DT_UINT64, DT_BOOL}))
    .ATTR(diagonal, Int, 0)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16,
                          DT_INT8, DT_INT64, DT_QINT8, DT_QUINT8, DT_QINT32, DT_QUINT16, DT_QINT16,
                          DT_UINT16, DT_UINT32, DT_UINT64, DT_BOOL}))
    .OP_END_FACTORY_REG(Tril)
```

## Brief

Returns the upper triangular part of a matrix (2-D tensor) or batch of matrices input 

## Inputs

x: A tensor, which supports 2-8 dimensions or be empty. Must be one of the following types:
float16, bfloat16, float32, double, int32, uint8, int16, int8, int64,
qint8, quint8, qint32, quint16, qint16, uint16, uint32, uint64, bool. 

## Outputs

y: A tensor. Has the same type as "x" . 

## Attributes

diagonal: An optional attribute indicates the diagonal to consider. Defaults to 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the Pytorch operator Tril.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
