# AscendPadding

```c
REG_OP(AscendPadding)
    .INPUT(x, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .ATTR(pad_dim_size, Int, 8)
    .OP_END_FACTORY_REG(AscendPadding)
```

## Brief

Ascend Padding, pad the last dimension of input.

## Inputs

One input, include:
x: Tensor which last dimension must be 1. For example: [624000, 1]. 

## Outputs

y: Padding the last dimension of x to padDimSize, [624000, padDimSize]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Diag.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
