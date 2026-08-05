# RandomStandardNormal

```c
REG_OP(RandomStandardNormal)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .REQUIRED_ATTR(dtype, Type)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomStandardNormal)
```

## Brief

Outputs random values from a normal distribution. 

## Inputs

Inputs include:
shape: A Tensor. Must be one of the following types: int32, int64. The shape of the output tensor. 

## Outputs

y: A Tensor of type float32, float16, double, bfloat16. 

## Attributes

- dtype: A type from: float16, float32, double, bfloat16. The type of the output.
- seed: An optional int. Defaults to 0. If either seed or seed2 are set to be non-zero,
the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- output0 y: double,float16,float32

## Attention Constraints

The implementation for RandomStandardNormal on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow RandomStandardNormal operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
