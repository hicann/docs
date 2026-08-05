# MatrixDiag

```c
REG_OP(MatrixDiag)
    .INPUT(x, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(MatrixDiag)
```

## Brief

Returns a batched diagonal tensor with a given batched diagonal values . 

## Inputs

x: A Tensor. Must be one of the following types:
  double, float32, float16, bfloat16, complex32, complex64, complex128,
  int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint16, quint16, qint32. 

## Outputs

y: A Tensor. Has the same type as "x" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator MatrixDiag.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
