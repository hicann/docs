# RaggedRange

```c
REG_OP(RaggedRange)
    .INPUT(starts, TensorType({DT_FLOAT,DT_DOUBLE,DT_INT32,DT_INT64}))
    .INPUT(limits, TensorType({DT_FLOAT,DT_DOUBLE,DT_INT32,DT_INT64}))
    .INPUT(deltas, TensorType({DT_FLOAT,DT_DOUBLE,DT_INT32,DT_INT64}))
    .OUTPUT(rt_nested_splits, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(rt_dense_values, TensorType({DT_FLOAT,DT_DOUBLE,DT_INT32,DT_INT64}))
    .REQUIRED_ATTR(Tsplits, Type)
    .OP_END_FACTORY_REG(RaggedRange)
```

## Brief

Returns a `RaggedTensor` containing the specified sequences of numbers . 

## Inputs

- starts: The starts of each range.
- limits: The limits of each range.
- deltas: The deltas of each range .

## Outputs

- rt_dense_values:The `flat_values` for the returned `RaggedTensor`.
- rt_nested_splits:The `row_splits` for the returned `RaggedTensor`.

## Attributes

Tsplits:A type of rt_nested_splits.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 starts: double,float32,int32,int64
- input1 limits: double,float32,int32,int64
- input2 deltas: double,float32,int32,int64
- output0 rt_nested_splits: int32,int64
- output1 rt_dense_values: double,float32,int32,int64

## Attention Constraints

The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors.
The vector inputs must all have the same size.  Scalar inputs are broadcast
to match the size of the vector inputs . 

## Third-party framework compatibility

Compatible with tensorflow RaggedRange operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
