# RandomUniformInt

```c
REG_OP(RandomUniformInt)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(min, TensorType({DT_INT32, DT_INT64}))
    .INPUT(max, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomUniformInt)
```

## Brief

Outputs random integers from a uniform distribution. 

## Inputs

Inputs include:
- shape: A Tensor. Must be one of the following types: int32, int64. The shape of the output tensor.
- min: A Tensor. Must be one of the following types: int32, int64. 0-D.
- max: A Tensor. Must have the same type as min. 0-D .

## Outputs

y: A Tensor. Has the same type as min. 

## Attributes

- seed: An optional int. Defaults to 0. If either seed or seed2 are set to be non-zero,
the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 min: int32,int64
- input2 max: int32,int64
- output0 y: int32,int64

## Attention Constraints

The implementation for RandomUniformInt on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow RandomUniformInt operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
