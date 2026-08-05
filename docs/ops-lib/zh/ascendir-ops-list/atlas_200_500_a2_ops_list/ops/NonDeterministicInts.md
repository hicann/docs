# NonDeterministicInts

```c
REG_OP(NonDeterministicInts)
    .INPUT(shape, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32,DT_INT64}))
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(NonDeterministicInts)
```

## Brief

Non-deterministically generates some integers . 

## Inputs

This op may use some OS-provided source of non-determinism (e.g. an RNG),
so each execution will give different results. Inputs included:
shape: The shape of the output tensor . 

## Outputs

y:A Returns Non-deterministic integer values with specified shape . 

## Attributes

- dtype: required, output data typetype. Must be one of the following types: int32, int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with tensorflow NonDeterministicInts operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
