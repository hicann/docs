# Gather

```c
REG_OP(Gather)
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,   DT_INT32,
                          DT_INT64,      DT_INT8,      DT_QINT16, DT_QINT32, DT_QINT8,   DT_QUINT16, DT_QUINT8,
                          DT_UINT16,     DT_UINT32,    DT_UINT64, DT_UINT8,  DT_BOOL,    DT_BF16}))
    .INPUT(indices, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,   DT_INT32,
                           DT_INT64,      DT_INT8,      DT_QINT16, DT_QINT32, DT_QINT8,   DT_QUINT16, DT_QUINT8,
                           DT_UINT16,     DT_UINT32,    DT_UINT64, DT_UINT8,  DT_BOOL,    DT_BF16}))
    .ATTR(validate_indices, Bool, true)
    .ATTR(batch_dims, Int, 0)
    .ATTR(is_preprocessed, Bool, false)
    .ATTR(negative_index_support, Bool, false)
    .OP_END_FACTORY_REG(Gather)
```

## Brief

Gather slices from "params" according to "indices"."indices" must be
an integer tensor of any dimension(usually 0-D or 1-D).
Produces an output tensor with shape "indices.shape + params.shape[1:]" .

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: complex128, complex64, float64, float32, float16,
    int16, int32, int64, int8, qint16, qint32, qint8, quint16, quint8, uint16, uint32, uint64, uint8,
    bool, bfloat16.
- indices: A Tensor of type int32 or int64 .

## Outputs

y: A Tensor. Has the same type as "x" .

## Attributes

- validate_indices: Whether to verify the values of indices, not enabled currently.
- batch_dims: An optional int. Defaults to 0.
- is_preprocessed: An optional bool. Whether to preprocess. Defaults to false.
- negative_index_support: An optional bool. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Attention Constraints

"indices" is in the range [0, x.shape[0]) .

## Third-party framework compatibility

Compatible with the TensorFlow operator Gather .


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
