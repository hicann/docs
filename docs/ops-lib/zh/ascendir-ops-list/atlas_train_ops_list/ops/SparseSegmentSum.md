# SparseSegmentSum

```c
REG_OP(SparseSegmentSum)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
        DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(segment_ids, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
        DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(SparseSegmentSum)
```

## Brief

Computes the sum along sparse segments of a tensor.

## Inputs

The input indices and segment_ids must have same rank. Inputs include:
- x:A Tensor. Must be one of the following types: float16, float, double, int32,
uint8, int16, int8, int64, uint16, uint32, uint64.
- indices: A Tensor. Must be one of the following types: int32, int64.
A 1-D tensor. Has same rank as segment_ids.
- segment_ids: A Tensor of type int32. A 1-D tensor. Values should be
sorted and can be repeated. 

## Outputs

y:A Tensor. Has the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 segment_ids: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with tensorflow SparseSegmentSum operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
