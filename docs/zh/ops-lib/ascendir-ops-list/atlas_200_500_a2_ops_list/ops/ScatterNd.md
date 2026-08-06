# ScatterNd

```c
REG_OP(ScatterNd)
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(x, TensorType::BasicType())
    .INPUT(shape, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(ScatterNd)
```

## Brief

Creates a new tensor by applying sparse "x" to individual values or slices within a tensor
(initially zero for numeric, empty for string) of the given "shape" according to "indices".

## Inputs

- indices: The index tensor. Format is ND. Support 1D ~ 8D. Must be one of the following types: int32, int64.
- x: The source tensor. Format is ND. Type must be the BasicType. Support 1D ~ 8D.
- shape: The shape of "y". Format is ND. Support 1D ~ 8D. Must be one of the following types: int32, int64.

## Outputs

y: A output tensor with same type as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 indices: int32,int64
- input1 x: float16,float32,int32
- input2 shape: int32,int64
- output0 y: float16,float32,int32
### AI CPU
- input0 indices: int32,int64
- input1 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input2 shape: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Attention Constraints

- indices.shape[-1] <= shape.rank, where the range of shape.rank is [1, 7]
- x.shape = indices.shape[:-1] + shape[indices.shape[-1]:].

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterNd.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
