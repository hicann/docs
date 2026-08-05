# StatelessRandomPoisson

```c
REG_OP(StatelessRandomPoisson)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .INPUT(lam, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(StatelessRandomPoisson)
```

## Brief

Outputs deterministic pseudorandom random integers from a poisson distribution . 

## Inputs

- shape: The shape of the output tensor.
- seed: 2 seeds (shape [2]).
- lam: mean value value of poisson distribution.

## Outputs

y: Returns Random values with specified shape. 

## Attributes

- dtype:Output data type. Must be one of the following types: float16, float32, double, int32, int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 seed: int32,int64
- input2 lam: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomUniformInt operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
