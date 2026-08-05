# InplaceUpdate

```c
REG_OP(InplaceUpdate)
    .INPUT(x, TensorType::BasicType())
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(v, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(InplaceUpdate)
```

## Brief

Updates specified rows with values in v.
Computes y = x; y[indices[i], ...] = v[i, ...]; return y.

## Inputs

Three inputs, including:
- x: A Tensor, Format is ND, Support 1D ~ 8D.
    Type must be one of the following types:
    float16, float32, int8, int16, uint16, uint8, int32, int64, uint32,
    uint64, double, bfloat16, complex32, complex64, complex128.
- indices: A vector of type int32, Format is ND.
    Indices into the left-most dimension of "x".
- v: A Tensor of the same type as "x", Format is ND.
    Same dimension sizes as x except the first dimension,
    which must be the same as the size of "indices".

## Outputs

y: A Tensor of the same type as "x", Format is ND.
   An alias of "x". The content of "y" is undefined if there are duplicates in indices.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- input1 indices: int32
- input2 v: float16,float32,int32
- output0 y: float16,float32,int32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 indices: int32
- input2 v: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator InplaceUpdate.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
