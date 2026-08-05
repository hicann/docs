# StatelessRandomUniformFullInt

```c
REG_OP(StatelessRandomUniformFullInt)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64, DT_UINT32, DT_UINT64}))
    .ATTR(dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(StatelessRandomUniformFullInt)
```

## Brief

Outputs deterministic pseudorandom random integers from a uniform distribution. 

## Inputs

- shape: The shape of the output tensor.
- seed: 2 seeds (shape [2]).

## Outputs

y: Returns Random values with specified shape. 

## Attributes

- dtype:Output data type. Must be one of the following types: int32, int64, uint32, uint64.
Defaults to int32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 seed: int32,int64,uint32,uint64
- output0 y: int32,int64,uint32,uint64

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomUniformFullInt operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
