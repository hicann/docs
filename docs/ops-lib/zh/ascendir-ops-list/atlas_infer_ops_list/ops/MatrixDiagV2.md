# MatrixDiagV2

```c
REG_OP(MatrixDiagV2)
    .INPUT(diagonal, TensorType::BasicType())
    .INPUT(k, TensorType({DT_INT32}))
    .INPUT(num_rows, TensorType({DT_INT32}))
    .INPUT(num_cols, TensorType({DT_INT32}))
    .INPUT(padding_value, TensorType::BasicType())
    .OUTPUT(output, TensorType::BasicType())
    .OP_END_FACTORY_REG(MatrixDiagV2)
```

## Brief

Returns a batched diagonal tensor with given batched diagonal values .

## Inputs

Five inputs, including:
- diagonal: Rank `r`, where `r >= 1`.
- k:
Diagonal offset(s). Positive value means superdiagonal, 0 refers to the main
diagonal, and negative value means subdiagonals. `k` can be a single integer
(for a single diagonal) or a pair of integers specifying the low and high ends
of a matrix band. `k[0]` must not be larger than `k[1]`. 
- num_rows:
The number of rows of the output matrix. If it is not provided, the op assumes
the output matrix is a square matrix and infers the matrix size from k and the
innermost dimension of `diagonal`. 
- num_cols: An NCHW, NHWC, or ND Tensor.
The number of columns of the output matrix. If it is not provided, the op
assumes the output matrix is a square matrix and infers the matrix size from
k and the innermost dimension of `diagonal`. 
- padding_value: The number to fill the area outside the specified diagonal band with.

## Outputs

output: Has rank `r+1` when `k` is an integer or `k[0] == k[1]`, rank `r` otherwise . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 diagonal: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 k: int32
- input2 num_rows: int32
- input3 num_cols: int32
- input4 padding_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 output: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterUpdate.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
