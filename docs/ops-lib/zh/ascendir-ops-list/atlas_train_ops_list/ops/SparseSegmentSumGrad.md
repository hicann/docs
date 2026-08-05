# SparseSegmentSumGrad

```c
REG_OP(SparseSegmentSumGrad)
    .INPUT(grad, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(segment_ids, TensorType({DT_INT32, DT_INT64}))
    .INPUT(output_dim0, TensorType({DT_INT32}))
    .OUTPUT(output, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(SparseSegmentSumGrad)
```

## Brief

Computes gradients for SparseSegmentSum .

## Inputs

- grad: A ND(Support 1D~8D) Tensor. Must be one of the following types: bfloat16,
float16, float32, double. gradient propagated to the SparseSegmentSum op.
- indices: A ND(Support 1D) Tensor. Must be one of the following types: int32, int64.
indices passed to the corresponding SparseSegmentSum op.
- segment_ids: A ND(Support 1D) Tensor of type int32, int64. segment_ids passed to the
corresponding SparseSegmentSum op, has save rank as indices.
- output_dim0: A Scalar of type int32. dimension 0 of "x" passed to
SparseSegmentSum op . 

## Outputs

output:A ND(Support 1D) Tensor. Has the same type as grad . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: float16,float32
- input1 indices: int32
- input2 segment_ids: int32
- input3 output_dim0: int32
- output0 output: float16,float32

## Third-party framework compatibility

Compatible with tensorflow SparseSegmentSumGrad operator


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
