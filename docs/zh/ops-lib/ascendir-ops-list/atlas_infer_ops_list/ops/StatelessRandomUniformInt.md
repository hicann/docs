# StatelessRandomUniformInt

```c
REG_OP(StatelessRandomUniformInt)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .INPUT(minval, TensorType({DT_INT32, DT_INT64}))
    .INPUT(maxval, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(StatelessRandomUniformInt)
```

## Brief

Outputs deterministic pseudorandom random integers from a uniform distribution. 

## Inputs

- shape: The shape of the output tensor.
- seed: 2 seeds (shape [2]).
- minval: Minimum value (inclusive, scalar).
- maxval: Maximum value (exclusive, scalar).

## Outputs

y: Returns Random values with specified shape. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 seed: int32,int64
- input2 minval: int32,int64
- input3 maxval: int32,int64
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomUniformInt operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
