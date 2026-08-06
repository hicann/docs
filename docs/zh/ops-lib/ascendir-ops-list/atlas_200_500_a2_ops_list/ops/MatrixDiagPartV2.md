# MatrixDiagPartV2

```c
REG_OP(MatrixDiagPartV2)
    .INPUT(input, TensorType::BasicType())
    .INPUT(k, TensorType({DT_INT32}))
    .INPUT(padding_value, TensorType::BasicType())
    .OUTPUT(diagonal, TensorType::BasicType())
    .OP_END_FACTORY_REG(MatrixDiagPartV2)
```

## Brief

Returns a tensor with the `k[0]`-th to `k[1]`-th diagonals of the batched `input`.

## Inputs

Three inputs, including:
- input: Rank `r` tensor where `r >= 2`.
- k:
Diagonal offset(s). Positive value means superdiagonal, 0 refers to the main
diagonal, and negative value means subdiagonals. `k` can be a single integer
(for a single diagonal) or a pair of integers specifying the low and high ends
of a matrix band. `k[0]` must not be larger than `k[1]`. 
- padding_value: The value to fill the area outside the specified diagonal band with.

## Outputs

diagonal: The extracted diagonal(s). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 k: int32
- input2 padding_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 diagonal: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterUpdate.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
