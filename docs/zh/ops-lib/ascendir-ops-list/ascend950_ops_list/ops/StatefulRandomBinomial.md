# StatefulRandomBinomial

```c
REG_OP(StatefulRandomBinomial)
    .INPUT(x, TensorType({DT_RESOURCE}))
    .INPUT(algorithm, TensorType({DT_INT64}))
    .INPUT(shape, TensorType({DT_INT32}))
    .INPUT(counts, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(probs, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(StatefulRandomBinomial)
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
- counts: A 0/1-D Tensor or Python value. The counts of the binomial
distribution.  Must be broadcastable with the leftmost dimension defined by `shape`.
- probs: A 0/1-D Tensor or Python value. The probability of success for the
binomial distribution.  Must be broadcastable with the leftmost dimension defined by `shape`.

## Outputs

y:A Returns Random values with specified shape . 

## Attributes

- dtype: required, output data type. Must be one of the following types: float16, float32, double, int32, int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: resource
- input1 algorithm: int64
- input2 shape: int32
- input3 counts: double,float16,float32
- input4 probs: double,float16,float32
- output0 y: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with tensorflow StatefulRandomBinomial operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
