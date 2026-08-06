# GatherV2

```c
REG_OP(GatherV2)
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,       DT_FLOAT16,     DT_INT16,
                          DT_INT32,      DT_INT64,     DT_INT8,   DT_QINT16,      DT_QINT32,      DT_QINT8,
                          DT_QUINT16,    DT_QUINT8,    DT_UINT16, DT_UINT32,      DT_UINT64,      DT_UINT8,
                          DT_BOOL,       DT_STRING,    DT_BF16,   DT_FLOAT8_E5M2, DT_FLOAT8_E8M0, DT_FLOAT8_E4M3FN}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(axis, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,       DT_FLOAT16,     DT_INT16,
                           DT_INT32,      DT_INT64,     DT_INT8,   DT_QINT16,      DT_QINT32,      DT_QINT8,
                           DT_QUINT16,    DT_QUINT8,    DT_UINT16, DT_UINT32,      DT_UINT64,      DT_UINT8,
                           DT_BOOL,       DT_STRING,    DT_BF16,   DT_FLOAT8_E5M2, DT_FLOAT8_E8M0, DT_FLOAT8_E4M3FN}))
    .ATTR(batch_dims, Int, 0)
    .ATTR(is_preprocessed, Bool, false)
    .ATTR(negative_index_support, Bool, false)
    .OP_END_FACTORY_REG(GatherV2)
```

## Brief

Gather slices from "x" according to "indices" by corresponding axis, produces a output tensor
with shape(x.shape[:axis]+indices.shape[batch_dims:]+x.shape[axis+1:]). When the impl_mode is set
as "support out of bound index", if the indices data is out of bound, the corresponding results
will be set as 0. Otherwise, an aic_error will occur.

## Inputs

- x: A ND (Support 1D~8D) tensor. Must be one of the following types: complex128, complex64, float64, float32,
float16,
    int16, int32, int64, int8, qint16, qint32, qint8, quint16, quint8, uint16, uint32, uint64, uint8,
    bool, FLOAT8_E5M2, FLOAT8_E8M0, FLOAT8_E4M3FN, string, bfloat16.
- indices: A ND (Support 1D~8D) tensor of type int32 or int64.
- axis: A Scalar with type as int32 or int64. Must be in the range [-rank(input_tensor), rank(input_tensor)).

## Outputs

y: A ND Tensor which has the same type as "x".

## Attributes

- batch_dims: An optional int which means the number of data to be deal with. Defaults to 0.
- is_preprocessed: An optional bool. Whether to preprocess, wihch is true means need to be preprocess and false
means not. Defaults to false.
- negative_index_support: An optional bool, which is true means support index is negative, and false means not.
Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex64,complex128,double,float8_e4m3fn,float8_e5m2,float8_e8m0,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 axis: int32,int64
- output0 y: bfloat16,bool,complex64,complex128,double,float8_e4m3fn,float8_e5m2,float8_e8m0,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
### AI CPU
- input1 indices: int32,int64
- input2 axis: int32,int64

## Attention Constraints

- Value in indices must be in range [0, x.shape[axis]).
- Default mode is HIGH_PERCISION.
Only HIGH_PERCISION mode support negative index, and negative index in HIGH_PERFORMANCE mode may cause precision
abnormal or aicore error.
- Batch_dims must be in the range [max(-rank(input_tensor),-rank(indices)), min(rank(input_tensor), rank(indices))).
- (batch_dims + rank(input_tensor)) % rank(input_tensor) must be less than or equal to (axis + rank(input_tensor)) %
rank(input_tensor).
- The first batch_dims dimensions of params and indices are same.

## Third-party framework compatibility

Compatible with the TensorFlow operator GatherV2 .


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
