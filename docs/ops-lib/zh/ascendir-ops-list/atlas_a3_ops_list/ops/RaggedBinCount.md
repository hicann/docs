# RaggedBinCount

```c
REG_OP(RaggedBinCount)
    .INPUT(splits, TensorType(DT_INT64))
    .INPUT(values, TensorType({DT_INT32, DT_INT64}))
    .INPUT(size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(weights, TensorType(DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE))
    .OUTPUT(output, TensorType(DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE))
    .ATTR(binary_output, Bool, false)
    .OP_END_FACTORY_REG(RaggedBinCount)
```

## Brief

Counts the number of occurrences of each value in an integer array.

## Inputs

- splits: A Tensor of type int64. 1D int64 Tensor.
- values: A Tensor. Must be one of the following types: int32, int64. 2D int Tensor.
- size: A Tensor. Must have the same type as values. non-negative int scalar Tensor.
- weights: A Tensor. Must be one of the following types: float32.
is a float32 Tensor with the same shape as input,
or a length-0 Tensor, in which case it acts as all weights equal to 1. 

## Outputs

- output: A Tensor with length "size" for each stride and has the same dtype as weights.

## Attributes

binary_output: An optional bool. Defaults to False. bool;
Whether the kernel should count the appearance or number of occurrences. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 splits: int64
- input1 values: int32,int64
- input2 size: int32,int64
- input3 weights: float32
- output0 output: float32

## Attention Constraints

The operator will use the interface set_atomic_add(), therefore weights and output should be float32 only. 

## Third-party framework compatibility

Compatible with tensorflow RaggedBinCount operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
