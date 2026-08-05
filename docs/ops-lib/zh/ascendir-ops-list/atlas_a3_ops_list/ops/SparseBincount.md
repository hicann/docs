# SparseBincount

```c
REG_OP(SparseBincount)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_INT32, DT_INT64}))
    .INPUT(dense_shape, TensorType({DT_INT64}))
    .INPUT(size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(weights, TensorType({DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE}))
    .ATTR(binary_output, Bool, false)
    .OUTPUT(output, TensorType({DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(SparseBincount)
```

## Brief

Counts the number of occurrences of each value in an integer array.

## Inputs

- indices: A 2D tensor of type int64.
- values: A 1D tensor of type int32 or int64.
- dense_shape: A 1D tensor of type int64.
- size: A non-negative scalar tensor of type int32 or int64.
- weights: A tensor of type int32 or int64 or float32 or double.

## Outputs

output: A tensor. Must have the same type as input "weights".

## Attributes

binary_output: An optional bool. Defaults to False.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 indices: int64
- input1 values: int32,int64
- input2 dense_shape: int64
- input3 size: int32,int64
- input4 weights: float32
- output0 output: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseBincount.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
