# StatelessRandom

```c
REG_OP(StatelessRandom)
    .INPUT(shape, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(from, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(to, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT64, DT_INT32, DT_INT16, DT_INT8, DT_UINT8, DT_BOOL}))
    .ATTR(dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(StatelessRandom)
```

## Brief

Outputs deterministic pseudorandom random integers from a uniform distribution. 

## Inputs

- shape: 1-D or empty tensor. The shape of the output tensor. Must be one of the following types: int64.
- seed: 0-D. seed for the counter-based RNG algorithm. Must be one of the following types: int64.
- offset: 0-D. offset for the counter-based RNG algorithm. Must be one of the following types: int64.
- from: 0-D scalar. Lower bound of the random range (inclusive). Must be one of the following types: int64.
- to: 0-D scalar. Upper bound of the random range (exclusive). Must be one of the following types: int64.

## Outputs

y: Returns Random values with specified shape.
Must be one of the following types: float16, bfloat16, float32, int64, int32, int16, int8, uint8, bool. 

## Attributes

dtype:Output data type. Must be one of the following types: float16, bfloat16, float32, int64, int32,
int16, int8, uint8, bool. Defaults to int32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 shape: int64
- input1 seed: int64
- input2 offset: int64
- input3 from: int64
- input4 to: int64
- output0 y: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandom operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
