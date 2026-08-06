# StatelessRandperm

```c
REG_OP(StatelessRandperm)
    .INPUT(n, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT64, DT_INT32, DT_INT16,
        DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(layout, Int, 0)
    .ATTR(dtype, Type, DT_INT64)
    .OP_END_FACTORY_REG(StatelessRandperm)
```

## Brief

Returns the random permutation of integers from 0 to n-1. 

## Inputs

Inputs include:
- n: A 1-dimensional int64 tensor, shape must be [1].
- seed: A 1-dimensional int64 tensor, shape must be [1]. If seed is set to be -1,
and offset is set to be 0, the random number generator is seeded by a random seed.
Otherwise, it is seeded by the given seed.
- offset: A 1-dimensional int64 tensor, shape must be [1]. To avoid seed collision.

## Outputs

- y: A mutable tensor, shape is [n]. Must be one of the following types:
float16, float32, double, int8, uint8, int16, int32, int64, bfloat16. 

## Attributes

- layout: An optional int. Defaults to 0.
- dtype: An optional type, used to specify the data type of output y. Defaults to int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 n: int64
- input1 seed: int64
- input2 offset: int64
- output0 y: bfloat16,double,float16,float32,int8,int16,int32,int64,uint8

## Attention Constraints

The implementation for Randperm on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

Compatible with Pytorch Randperm operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
