# StatefulUniformFullInt

```c
REG_OP(StatefulUniformFullInt)
    .INPUT(x, TensorType({DT_RESOURCE}))
    .INPUT(algorithm, TensorType({DT_INT64}))
    .INPUT(shape, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_UINT64}))
    .OP_END_FACTORY_REG(StatefulUniformFullInt)
```

## Brief

Outputs random integers from a uniform distribution.
The generated values are uniform integers covering the whole range of `dtype` . 

## Inputs

- x: The handle of the resource variable that stores the state of the RNG.
- algorithm: The RNG algorithm.
- shape: The shape of the output tensor .

## Outputs

y:A  Returns Random values with specified shape . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: resource
- input1 algorithm: int64
- input2 shape: int32,int64
- output0 y: uint64

## Third-party framework compatibility

Compatible with tensorflow StatefulUniformFullInt operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
