# RandomShuffle

```c
REG_OP(RandomShuffle)
    .INPUT(x, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16,
        DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
        DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE}))
    .OUTPUT(y, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16,
        DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
        DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE}))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomShuffle)
```

## Brief

Randomly shuffles a tensor along its first dimension . 

## Inputs

Inputs include:
x: A Tensor. The tensor to be shuffled . 

## Outputs

y: A Tensor. Has the same type as x . A Tensor of type float16, float,
double, int32, int64, int16, uint16, int8, uint8, int32,int64. 

## Attributes

- seed: An optional int. Defaults to 0. If either seed or seed2 are set to be non-zero,
the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. Defaults to 0 . A second seed to avoid seed collision.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16

## Attention Constraints

The implementation for RandomShuffle on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow RandomShuffle operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
