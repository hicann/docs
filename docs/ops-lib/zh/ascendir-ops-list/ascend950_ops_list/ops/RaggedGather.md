# RaggedGather

```c
REG_OP(RaggedGather)
    .DYNAMIC_INPUT(params_nested_splits, TensorType({DT_INT32, DT_INT64}))
    .INPUT(params_dense_values, TensorType({DT_INT32, DT_INT64}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .DYNAMIC_OUTPUT(output_nested_splits, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(output_dense_values, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(Tsplits, Type)
    .ATTR(PARAMS_RAGGED_RANK, Int, 1)
    .ATTR(OUTPUT_RAGGED_RANK, Int, 0)
    .OP_END_FACTORY_REG(RaggedGather)
```

## Brief

Gather ragged slices from `params` axis `0` according to `indices`. 

## Inputs

- params_nested_splits: The `nested_row_splits` tensors that define the row-partitioning for the
params` RaggedTensor input. It's a dynamic input.
- params_dense_values: The `flat_values` for the `params` RaggedTensor. There was a terminology change
at the python level from dense_values to flat_values, so dense_values is the
deprecated name.
- indices: Indices in the outermost dimension of `params` of the values that should be
gathered.

## Outputs

- output_nested_splits: A Returns The `nested_row_splits` tensors that define the row-partitioning for the
returned RaggedTensor.The `flat_values` for the returned RaggedTensor .
- output_dense_values: The `flat_values` for the returned RaggedTensor.

## Attributes

- PARAMS_RAGGED_RANK: An optional int, defaults to 1. The ragged rank of the params_nested_splits.
- Tsplits: A type of output_nested_splits.
- OUTPUT_RAGGED_RANK: An optional int, defaults to 0. The ragged rank of the output RaggedTensor. `output_nested_splits` will contain
this number of `row_splits` tensors. This value should equal
`indices.shape.ndims + params.ragged_rank - 1`. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 params_dense_values: int32,int64
- input1 indices: int32,int64
- output0 output_dense_values: int32,int64

## Third-party framework compatibility

Compatible with tensorflow RaggedGather operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
