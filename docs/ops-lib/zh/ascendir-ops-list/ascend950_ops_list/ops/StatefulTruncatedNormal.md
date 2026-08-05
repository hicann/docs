# StatefulTruncatedNormal

```c
REG_OP(StatefulTruncatedNormal)
    .INPUT(x, TensorType({DT_RESOURCE}))
    .INPUT(algorithm, TensorType({DT_INT64}))
    .INPUT(shape, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(StatefulTruncatedNormal)
```

## Brief

Outputs random values from a truncated normal distribution.
The generated values follow a normal distribution with mean 0 and standard
deviation 1, except that values whose magnitude is more than 2 standard
deviations from the mean are dropped and re-picked . 

## Inputs

- x: The handle of the resource variable that stores the state of the RNG.
- algorithm: The RNG algorithm.
- shape: The shape of the output tensor .

## Outputs

y:A Returns Random values with specified shape . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: resource
- input1 algorithm: int64
- input2 shape: int32,int64
- output0 y: float32

## Third-party framework compatibility

Compatible with tensorflow StatefulTruncatedNormal operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
