# MatrixSetDiagV3

```c
REG_OP(MatrixSetDiagV3)
    .INPUT(input, TensorType::BasicType())
    .INPUT(diagonal, TensorType::BasicType())
    .INPUT(k, TensorType({DT_INT32}))
    .OUTPUT(output, TensorType::BasicType())
    .ATTR(align, String, "RIGHT_LEFT")
    .OP_END_FACTORY_REG(MatrixSetDiagV3)
```

## Brief

Returns a batched matrix tensor with new batched diagonal values .

## Inputs

Three inputs, including:
- input: Rank `r+1`, where `r >= 1`.
- diagonal: Rank `r` when `k` is an integer or `k[0] == k[1]`. Otherwise, it has rank `r+1`.
- k:
Diagonal offset(s). Positive value means superdiagonal, 0 refers to the main
diagonal, and negative value means subdiagonals. `k` can be a single integer
(for a single diagonal) or a pair of integers specifying the low and high ends
of a matrix band. `k[0]` must not be larger than `k[1]`. 

## Outputs

output: Rank `r+1`, with `output.shape = input.shape`. 

## Attributes

- align: An optional string. Defaults to RIGHT_LEFT. It is a string specifying.
how superdiagonals and subdiagonals should be aligned, respectively. 
other optional: LEFT_RIGHT, LEFT_LEFT, and RIGHT_RIGHT.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 diagonal: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input2 k: int32
- output0 output: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterUpdate.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
