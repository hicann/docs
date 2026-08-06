# SparseSegmentMeanGrad

```c
REG_OP(SparseSegmentMeanGrad)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BFLOAT16}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(segment_ids, TensorType({DT_INT32, DT_INT64}))
    .INPUT(output_dim0, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BFLOAT16}))
    .OP_END_FACTORY_REG(SparseSegmentMeanGrad)
```

## Brief

Computes gradients for SparseSegmentMean.

## Inputs

- x: A Tensor. Must be one of the following types: float16, float, double, bfloat16.
gradient propagated to the SparseSegmentMean op.
- indices: A Tensor. Must be one of the following types: int32, int64.
indices passed to the corresponding SparseSegmentMean op.
- segment_ids: A Tensor. Must be one of the following types: int32, int64. segment_ids passed to the
corresponding SparseSegmentMean op.
- output_dim0: A Tensor of type int32. dimension 0 of "x" passed to
SparseSegmentMean op. 

## Outputs

y:A Tensor. Has the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- input1 indices: int32,int64
- input2 segment_ids: int32,int64
- input3 output_dim0: int32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with tensorflow SparseSegmentMeanGrad operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
