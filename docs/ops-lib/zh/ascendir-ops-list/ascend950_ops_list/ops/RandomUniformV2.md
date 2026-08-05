# RandomUniformV2

```c
REG_OP(RandomUniformV2)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(offset, TensorType({DT_INT64}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomUniformV2)
```

## Brief

Outputs random values from a uniform distribution. 

## Inputs

Inputs include:
- shape: A 1-D Tensor. Must be one of the following types: int32, int64. The shape of the output tensor.
- offset: A 1-D Tensor， should be const data. Must be one of the following types: int64.

## Outputs

- y: A Tensor of type float32, float16, bfloat16.
- offset: A 1-D Tensor， should be const data. Must be one of the following types: int64.

## Attributes

- dtype: An required int. The data type of y. It supports 1(float16), 27(bfloat16) and 0(float32).
- seed: An optional int. Defaults to 0. If either seed or seed2 are set to be non-zero,
the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 shape: int32,int64
- input1 offset: int64
- output0 y: bfloat16,float16,float32
- output1 offset: int64


---

[Back to Operator Specifications (Ascend950)](../README.md)
