# RngSkip

```c
REG_OP(RngSkip)
    .INPUT(x, TensorType({DT_RESOURCE}))
    .INPUT(algorithm, TensorType({DT_INT64}))
    .INPUT(delta, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(RngSkip)
```

## Brief

Advance the counter of a counter-based RNG. The state of the RNG after
`rng_skip(n)` will be the same as that after `stateful_uniform([n])`
(or any other distribution). The actual increment added to the
counter is an unspecified implementation detail . 

## Inputs

- x: The handle of the resource variable that stores the state of the RNG.
- algorithm: The RNG algorithm.
- delta: The amount of advancement .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: resource
- input1 algorithm: int64
- input2 delta: int64

## Third-party framework compatibility

Compatible with tensorflow RngSkip operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
