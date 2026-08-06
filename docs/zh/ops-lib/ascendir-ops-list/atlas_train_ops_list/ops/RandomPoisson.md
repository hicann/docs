# RandomPoisson

```c
REG_OP(RandomPoisson)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(rate, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_INT32, DT_INT64}))
    .ATTR(dtype, Type, DT_INT64)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomPoisson)
```

## Brief

Outputs random values from the Poisson distribution(s) described by rate . 

## Inputs

Inputs include:
- shape: A Tensor. Must be one of the following types: int32, int64. 1-D integer tensor.
- rate: A Tensor. Must be one of the following types: float16, float32, double, int32, int64 .

## Outputs

y: A Tensor of type dtype float16, float, double, int32, int64. 

## Attributes

- dtype: An optional type from: float16, float32, double, int32, int64. Defaults to int64.
- seed: An optional int. Defaults to 0. If either seed or seed2 are set to be non-zero,
the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 rate: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Attention Constraints

The implementation for RandomPoisson on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow RandomPoisson operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
