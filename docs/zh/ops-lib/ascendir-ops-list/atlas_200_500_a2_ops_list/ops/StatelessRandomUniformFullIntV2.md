# StatelessRandomUniformFullIntV2

```c
REG_OP(StatelessRandomUniformFullIntV2)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(key, TensorType({DT_UINT64}))
    .INPUT(counter, TensorType({DT_UINT64}))
    .INPUT(alg, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64, DT_UINT32, DT_UINT64}))
    .ATTR(dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(StatelessRandomUniformFullIntV2)
```

## Brief

Outputs deterministic pseudorandom random integers from a uniform distribution. 

## Inputs

- shape: The shape of the output tensor.
- key: Key for the counter-based RNG algorithm.
- counter: Initial counter for the counter-based RNG algorithm.
- alg: 0-D. The RNG algorithm.

## Outputs

y: Returns Random values with specified shape. 

## Attributes

- dtype:Output data type. Must be one of the following types: int32, int64, uint32, uint64.
Defaults to int32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 key: uint64
- input2 counter: uint64
- input3 alg: int32
- output0 y: int32,int64,uint32,uint64

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomUniformFullIntV2 operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
