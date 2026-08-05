# StatelessRandomUniformV2

```c
REG_OP(StatelessRandomUniformV2)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(key, TensorType({DT_UINT64}))
    .INPUT(counter, TensorType({DT_UINT64}))
    .INPUT(alg, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_DOUBLE}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(StatelessRandomUniformV2)
```

## Brief

Outputs deterministic pseudorandom random integers from a uniform distribution. 

## Inputs

- shape: 1-D or empty tensor. The shape of the output tensor. Must be one of the following types: int32, int64.
- key: shape[1]. Key for the counter-based RNG algorithm. Must be one of the following types: uint64.
- counter: 1-D. Initial counter for the counter-based RNG algorithm. Must be one of the following types: uint64.
- alg: 0-D. The RNG(random number generator) algorithm. Must be one of the following types: int32.

## Outputs

y: Returns Random values with specified shape.
Must be one of the following types: float16, bfloat16, float32, double. 

## Attributes

dtype:Output data type. Must be one of the following types: float16, bfloat16, float32, double.
Defaults to float32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 key: uint64
- input2 counter: uint64
- input3 alg: int32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomUniformV2 operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
