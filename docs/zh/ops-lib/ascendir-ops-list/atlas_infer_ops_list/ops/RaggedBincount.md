# RaggedBincount

```c
REG_OP(RaggedBincount)
    .INPUT(splits, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_INT32, DT_INT64}))
    .INPUT(size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(weights, TensorType({DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(output, TensorType({DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE}))
    .ATTR(binary_output, Bool, false)
    .OP_END_FACTORY_REG(RaggedBincount)
```

## Brief

Counts the number of occurrences of each value in an integer array.

## Inputs

Four inputs, including:
- splits: A 1D tensor of dtype int64.
- values: A 2D tensor of dtype int32, int64.
- size: A non-negative scalar Tensor, has the same type as values.
- weights: A Tensor. Must be one of the following types: int32, int64, float32, double.

## Outputs

- output: Must be one of the following types: int32, int64, float, double.

## Attributes

- binary_output: An optional bool. Defaults to False.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 splits: int64
- input1 values: int32,int64
- input2 size: int32,int64
- input3 weights: double,float32,int32,int64
- output0 output: double,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator RaggedBincount.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
