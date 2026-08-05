# MultinomialAliasDraw

```c
REG_OP(MultinomialAliasDraw)
    .INPUT(q, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(j, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT64}))
    .REQUIRED_ATTR(num_samples, Int)
    .ATTR(seed, Int, 0)
    .OP_END_FACTORY_REG(MultinomialAliasDraw)
```

## Brief

Creates a multinomial distribution.

## Inputs

Inputs include:
- q: A Tensor. Must be one of the following types: float, double.
1-D Tensor with shape [num_classes].
- j: A Tensor. Must be one of the following types: int64.
1-D Tensor with shape [num_classes].
- num_samples: A Tensor of type int32. 0-D. Number of independent samples to draw for each row slice .

## Outputs

y: A Tensor of type int32 or int64. 

## Attributes

- output_dtype: An optional type from: int32, int64. Defaults to int64.
- seed: An optional int. Defaults to 0.
- seed2: An optional int. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 q: double,float32
- input1 j: int64
- output0 y: int64

## Attention Constraints

The implementation for MultinomialAliasDraw on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with torch _multinomial_alias_draw operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
