# RandomUniformIntV2

```c
REG_OP(RandomUniformIntV2)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(min, TensorType({DT_INT32, DT_INT64}))
    .INPUT(max, TensorType({DT_INT32, DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(offset, TensorType({DT_INT64}))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomUniformIntV2)
```

## Brief

Outputs random integers from a uniform distribution with a given offset. 

## Inputs

Inputs include:
- shape: A 1-D Tensor. Must be one of the following types: int32, int64. The shape of the output tensor.
- min: A 1-D Tensor. Must be one of the following types: int32, int64.
- max: A 1-D Tensor. Must be one of the following types: int32, int64.
- offset: A 1-D Tensor, should be const data. Must be one of the following types: int64.
The value of offset should not be less than 0 and will be set to the default value 0 if it is negative.  

## Outputs

- y: A Tensor. Has the same type as min.
- offset: A 1-D Tensor, should be const data. Must be one of the following types: int64.

## Attributes

- seed: An optional int. Defaults to 0. If either seed or seed2 are set to be non-zero,
the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 shape: int32,int64
- input1 min: int32,int64
- input2 max: int32,int64
- input3 offset: int64
- output0 y: int32,int64
- output1 offset: int64


---

[Back to Operator Specifications (Ascend950)](../README.md)
