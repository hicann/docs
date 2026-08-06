# StatefulUniformInt

```c
REG_OP(StatefulUniformInt)
    .INPUT(x, TensorType({DT_RESOURCE}))
    .INPUT(algorithm, TensorType({DT_INT64}))
    .INPUT(shape, TensorType({DT_INT32,DT_INT64}))
    .INPUT(minval, TensorType({DT_INT64}))
    .INPUT(maxval, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(StatefulUniformInt)
```

## Brief

Outputs random integers from a uniform distribution.
The generated values are uniform integers in the range `[minval, maxval)`.
The lower bound `minval` is included in the range, while the upper bound
`maxval` is excluded.
The random integers are slightly biased unless `maxval - minval` is an exact
power of two.  The bias is small for values of `maxval - minval` significantly
smaller than the range of the output (either `2^32` or `2^64`) . 

## Inputs

- x: The handle of the resource variable that stores the state of the RNG.
- algorithm: The RNG algorithm.
- shape: The shape of the output tensor.
- minval: Minimum value (inclusive, scalar).
- maxval: Maximum value (exclusive, scalar) .

## Outputs

y:A Returns Random values with specified shape . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: resource
- input1 algorithm: int64
- input2 shape: int32,int64
- input3 minval: int64
- input4 maxval: int64
- output0 y: int64

## Third-party framework compatibility

Compatible with tensorflow StatefulUniformInt operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
