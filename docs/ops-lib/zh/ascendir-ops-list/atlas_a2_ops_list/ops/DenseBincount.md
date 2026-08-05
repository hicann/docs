# DenseBincount

```c
REG_OP(DenseBincount)
    .INPUT(input, TensorType({DT_INT32, DT_INT64}))
    .INPUT(size, TensorType({DT_INT32, DT_INT64}))
    .INPUT(weights, TensorType(DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE))
    .OUTPUT(output, TensorType(DT_INT32, DT_INT64, DT_FLOAT, DT_DOUBLE))
    .ATTR(binary_output, Bool, false)
    .OP_END_FACTORY_REG(DenseBincount)
```

## Brief

Counts the number of occurrences of each value in an integer array.

## Inputs

- input: A Tensor of type int32, int64. 1D or 2D int Tensor.
- size: A Tensor. Must have the same type as input. non-negative int scalar Tensor.
- weights: A Tensor. Must be one of the following types: int32, int64, float32, float64.
with the same shape as input,
or a length-0 Tensor, in which case it acts as all weights equal to 1. 

## Outputs

- output: A Tensor with length "size" for each stride and has the same dtype as weights.

## Attributes

binary_output: An optional bool. Defaults to False. bool;
Whether the kernel should count the appearance or number of occurrences. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input: int32,int64
- input1 size: int32,int64
- input2 weights: float32
- output0 output: float32

## Attention Constraints

The operator will use the interface set_atomic_add(), therefore weights and output should be float32 only. 

## Third-party framework compatibility

Compatible with tensorflow DenseBincount operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
