# SparseSegmentMean

```c
REG_OP(SparseSegmentMean)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(segment_ids, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BFLOAT16}))
    .OP_END_FACTORY_REG(SparseSegmentMean)
```

## Brief

Computes the mean along sparse segments of a tensor.

## Inputs

The input indices and segment_ids must have same rank. Inputs include:
- x: A tensor. Must be one of the following types: float16, float32, double, bfloat16.
- indices: A tensor. Must be one of the following types: int32, int64.
A 1-D tensor. Has same rank as segment_ids.
- segment_ids: A tensor. Must be one of the following types: int32, int64. A 1-D tensor. Values should be
sorted and can be repeated. 

## Outputs

y:A tensor. Has the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- input1 indices: int32,int64
- input2 segment_ids: int32,int64
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow SparseSegmentMean operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
