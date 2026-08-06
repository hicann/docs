# RngReadAndSkipV2

```c
REG_OP(RngReadAndSkipV2)
    .INPUT(value, TensorType({DT_INT64}))
    .INPUT(algorithm, TensorType({DT_INT32}))
    .INPUT(delta, TensorType({DT_UINT64}))
    .OUTPUT(value, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(RngReadAndSkipV2)
```

## Brief

Advance the counter of a counter-based RNG. The state of the RNG after
`rng_skip(n)` will be the same as that after `stateful_uniform([n])`
(or any other distribution). The actual increment added to the
counter is an unspecified implementation detail . 

## Inputs

- value: Stores the state of the RNG.
- algorithm: The RNG algorithm.
- delta: The amount of advancement .

## Outputs

value:A Returns Random values with specified shape . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 value: int64
- input1 algorithm: int32
- input2 delta: uint64
- output0 value: int64

## Third-party framework compatibility

Compatible with tensorflow RngReadAndSkipV2 operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
