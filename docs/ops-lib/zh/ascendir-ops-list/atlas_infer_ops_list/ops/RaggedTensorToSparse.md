# RaggedTensorToSparse

```c
REG_OP(RaggedTensorToSparse)
    .DYNAMIC_INPUT(rt_nested_splits, TensorType({DT_INT32, DT_INT64}))
    .INPUT(rt_dense_values, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(sparse_indices, TensorType({DT_INT64}))
    .OUTPUT(sparse_values, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(sparse_dense_shape, TensorType({DT_INT64}))
    .ATTR(RAGGED_RANK, Int, 1)
    .ATTR(Tsplits, Type, DT_INT64)
    .OP_END_FACTORY_REG(RaggedTensorToSparse)
```

## Brief

Converts a RaggedTensor into a SparseTensor with the same values. 

## Inputs

Two inputs, including:
- rt_nested_splits: A list of at least 1 Tensor objects with the same type
in: int32, int64. The row_splits for the RaggedTensor. It's a dynamic input.
- rt_dense_values: A Tensor. The flat_values for the RaggedTensor
Must be one of the following types: bool, int8, uint8, int16, uint16, int32,
int64, double, float32, float16. 

## Outputs

- sparse_indices: A Tensor of type int64.
- sparse_values: A Tensor. Has the same type as rt_dense_values.
- sparse_dense_shape: A Tensor of type int64.

## Attributes

- RAGGED_RANK: An optional int that the dynamic of input rt_nested_splits with type int. Default value is 1.
- Tsplits: A required attribute, the type is int64 .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 rt_dense_values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 sparse_indices: int64
- output1 sparse_values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output2 sparse_dense_shape: int64

## Third-party framework compatibility

Compatible with TensorFlow operator RaggedTensorToSparse.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
