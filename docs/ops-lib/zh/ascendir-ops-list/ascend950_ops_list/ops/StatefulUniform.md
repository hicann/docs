# StatefulUniform

```c
REG_OP(StatefulUniform)
    .INPUT(x, TensorType({DT_RESOURCE}))
    .INPUT(algorithm, TensorType({DT_INT64}))
    .INPUT(shape, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(StatefulUniform)
```

## Brief

Outputs random values from a uniform distribution.
The generated values follow a uniform distribution in the range `[0, 1)`. The
lower bound 0 is included in the range, while the upper bound 1 is excluded.

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

Compatible with tensorflow StatefulUniform operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
