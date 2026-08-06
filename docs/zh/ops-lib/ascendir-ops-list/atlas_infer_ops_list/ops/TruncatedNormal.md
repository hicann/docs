# TruncatedNormal

```c
REG_OP(TruncatedNormal)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_DOUBLE}))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(TruncatedNormal)
```

## Brief

Outputs random values from a truncated normal distribution . 

## Inputs

Inputs include:
shape: A Tensor. Must be one of the following types: int32, int64 . 

## Outputs

y: A Tensor of types: float16, float32, double, bfloat16 . A tensor of the specified shape
filled with random truncated normal values. 

## Attributes

- seed: An optional int. Defaults to 0.If either `seed` or `seed2`
are set to be non-zero, the random number generator is seeded by the given
seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.
- dtype: An optional attribute, a type from: float16, float32, double, bfloat16. The default type is float32.
The corresponding relationshape between the enumeration values and real output type is :
0(float32), 1(float16), 11(double), 27(bfloat16).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- output0 y: double,float16,float32

## Attention Constraints

The implementation for TruncatedNormal on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow TruncatedNormal operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
