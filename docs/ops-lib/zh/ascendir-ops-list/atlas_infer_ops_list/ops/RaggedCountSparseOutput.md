# RaggedCountSparseOutput

```c
REG_OP(RaggedCountSparseOutput)
    .INPUT(splits, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_INT32,DT_INT64}))
    .INPUT(weights, TensorType({DT_INT32,DT_INT64,DT_FLOAT,DT_DOUBLE}))
    .OUTPUT(output_indices, TensorType({DT_INT64}))
    .OUTPUT(output_values, TensorType({DT_INT32,DT_INT64,DT_FLOAT,DT_DOUBLE}))
    .OUTPUT(output_dense_shape, TensorType({DT_INT64}))
    .ATTR(minlength, Int, -1)
    .ATTR(maxlength, Int, -1)
    .REQUIRED_ATTR(binary_output, Bool)
    .OP_END_FACTORY_REG(RaggedCountSparseOutput)
```

## Brief

Count the number of occurrences of each value in the input ragged integer array,
and output it according to the sparse matrix.

## Inputs

- splits: A 1D tensor of type int64.
- values: A 1D or 2D tensor of type int32 or int64.
- weights: A tensor of type int32 or int64 or float or double.

## Outputs

- output_indices: A tensor of type int64.
- output_values: A tensor of the same type as "weights".
- output_dense_shape: A tensor of type int64.

## Attributes

- minlength: An optional int >=-1. Defaults to -1.
- maxlength: An optional int >=-1. Defaults to -1.
- binary_output: A required bool.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 splits: int64
- input1 values: int32,int64
- input2 weights: double,float32,int32,int64
- output0 output_indices: int64
- output1 output_values: double,float32,int32,int64
- output2 output_dense_shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator RaggedCountSparseOutput. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
