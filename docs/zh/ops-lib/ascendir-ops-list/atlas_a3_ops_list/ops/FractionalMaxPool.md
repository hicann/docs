# FractionalMaxPool

```c
REG_OP(FractionalMaxPool)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .OUTPUT(row_pooling_sequence, TensorType({DT_INT64}))
    .OUTPUT(col_pooling_sequence, TensorType({DT_INT64}))
    .ATTR(pooling_ratio, ListFloat, {})
    .ATTR(pseudo_random, Bool, false)
    .ATTR(overlapping, Bool, false)
    .ATTR(deterministic, Bool, false)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(FractionalMaxPool)
```

## Brief

Performs fractional max pooling on the input .

## Inputs

Inputs include:
x: A Tensor. Must be one of the following types: float32, double, int32, int64.
4-D with shape [batch, height, width, channels]. 

## Outputs

- y: A Tensor. Has the same type as x.
- row_pooling_sequence: A Tensor of type int64.
- col_pooling_sequence: A Tensor of type int64.

## Attributes

- pooling_ratio: A list of floats that has length >= 4. Pooling ratio for each dimension of value.
- pseudo_random: An optional bool. Defaults to False.
- overlapping: An optional bool. Defaults to False.
- deterministic: An optional bool. Defaults to False.
- seed: An optional int. Defaults to 0.
- seed2: An optional int. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float32,int32,int64
- output0 y: double,float32,int32,int64
- output1 row_pooling_sequence: int64
- output2 col_pooling_sequence: int64

## Attention Constraints

The implementation for FractionalMaxPool on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow FractionalMaxPool operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
