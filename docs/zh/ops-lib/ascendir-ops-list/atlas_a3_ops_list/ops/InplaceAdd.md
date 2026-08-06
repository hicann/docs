# InplaceAdd

```c
REG_OP(InplaceAdd)
    .INPUT(x, TensorType::BasicType())
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(v, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(InplaceAdd)
```

## Brief

Adds "v" into specified rows of "x".
Computes y = x; y[i, :] += v.

## Inputs

Three inputs, including:
- x: A Tensor.
    TensorType::BasicType(), Format is ND.
- indices: A vector of type int32.
    Indices into the left-most dimension of "x".
- v: A Tensor of the same type as "x".
    Same dimension sizes as x except the first dimension,
    which must be the same as the size of "indices" . 

## Outputs

y: A Tensor of the same type as "x".
 An alias of "x". The content of "y" is undefined if there are duplicates in indices.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 indices: int32
- input2 v: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator InplaceAdd.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
