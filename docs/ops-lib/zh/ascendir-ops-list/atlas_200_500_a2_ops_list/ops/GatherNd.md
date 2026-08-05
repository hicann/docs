# GatherNd

```c
REG_OP(GatherNd)
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,   DT_INT32,
                          DT_INT64,      DT_INT8,      DT_QINT16, DT_QINT32, DT_QINT8,   DT_QUINT16, DT_QUINT8,
                          DT_UINT16,     DT_UINT32,    DT_UINT64, DT_UINT8,  DT_BOOL,    DT_STRING,  DT_BF16}))
    .INPUT(indices, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,   DT_INT32,
                           DT_INT64,      DT_INT8,      DT_QINT16, DT_QINT32, DT_QINT8,   DT_QUINT16, DT_QUINT8,
                           DT_UINT16,     DT_UINT32,    DT_UINT64, DT_UINT8,  DT_BOOL,    DT_STRING,  DT_BF16}))
    .ATTR(negative_index_support, Bool, false)
    .OP_END_FACTORY_REG(GatherNd)
```

## Brief

Gather slices from "x" into a tensor with shape specified by
"indices". "indices" is an K-dimensional integer tensor, best thought of as a
(K-1)-dimensional tensor of "indices" into "params", where each element
defines a slice of "params":
  output[\\(i_0, ..., i_{K-2}\\)] = params[indices[\\(i_0, ..., i_{K-2}\\)]]
"indices" defines slices into the first N dimensions of
"params", where
          N = indices.shape[-1]
    indices = [[0, 0], [1, 1]]
     x = [['a', 'b'], ['c', 'd']]
     output = ['a', 'd']
When the impl_mode is set as "support out of bound index", if the indices
data is out of bound, the corresponding results will be set as 0. Otherwise,
an aic_error will occur.

## Inputs

- x: A ND(Support 1D~8D) Tensor. Must be one of the following types:
    complex128, complex64, float64, float32, float16, int16, int32, int64,
    int8, qint16, qint32, qint8, quint16, quint8, uint16, uint32, uint64,
    uint8, bool, string, bfloat16.
- indices: A ND(Support 1D) Tensor of type int32 or int64.

## Outputs

y: A ND(Support 1D~8D) Tensor which has the same type as "x".

## Attributes

negative_index_support: An optional bool. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int32,int64,uint8
- input1 indices: int32,int64
- output0 y: bool,float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator GatherNd.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
