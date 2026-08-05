# SparseReshape

```c
REG_OP(SparseReshape)
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(new_shape, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y_indices, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y_shape, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(SparseReshape)
```

## Brief

Reshapes a sparse tensor from input shape to output shape.

## Inputs

Three inputs, including:
- indices: A 2D Tensor. Must be one of the following types: int32, int64. Shape [nnz, input_rank].
- shape: A 1D Tensor. Must be one of the following types: int32, int64. Shape [input_rank].
- new_shape: A 1D Tensor. Must be one of the following types: int32, int64. Shape [output_rank].

## Outputs

Two outputs, including:
- y_indices: A 2D Tensor. Must be one of the following types: int32, int64. Shape [nnz, output_rank].
- y_shape: A 1D Tensor. Must be one of the following types: int32, int64. Shape [output_rank].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 indices: int32
- input1 shape: int32
- input2 new_shape: int32
- output0 y_indices: int32
- output1 y_shape: int32
### AI CPU
- input0 indices: int64
- input1 shape: int64
- input2 new_shape: int64
- output0 y_indices: int64
- output1 y_shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseReshape.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
