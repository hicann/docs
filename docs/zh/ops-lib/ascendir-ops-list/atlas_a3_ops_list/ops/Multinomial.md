# Multinomial

```c
REG_OP(Multinomial)
    .INPUT(logits, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(num_samples, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(dtype, Type, DT_INT64)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(Multinomial)
```

## Brief

Draws samples from a multinomial distribution .

## Inputs

Inputs include:
- logits: A Tensor. Must be one of the following types: float16, float, double.
2-D Tensor with shape [batch_size, num_classes].
- num_samples: A Tensor of type int32. 0-D. Number of independent samples to draw for each row slice .

## Outputs

y_indices: A Tensor of type output_dtype . 

## Attributes

- output_dtype: An optional type from: int32, int64. Defaults to int64.
- seed: An optional int. Defaults to 0.
- seed2: An optional int. Defaults to 0 .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 logits: double,float16,float32
- input1 num_samples: int32
- output0 y: int32,int64

## Attention Constraints

The implementation for Multinomial on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow Multinomial operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
