# StatelessRandomBinomial

```c
REG_OP(StatelessRandomBinomial)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .INPUT(counts, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .INPUT(probs, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(StatelessRandomBinomial)
```

## Brief

Outputs deterministic pseudorandom random integers from a binomial distribution. 

## Inputs

- shape: The shape of the output tensor.
- seed: 2 seeds (shape [2]).
- counts: The counts of the binomial distribution. Must be broadcastable with probs,
and broadcastable with the rightmost dimensions of shape.
- probs: The probability of success for the binomial distribution.
Must be broadcastable with counts and broadcastable with the rightmost dimensions of shape. 

## Outputs

- y: Returns Random values with specified shape.

## Attributes

- dtype: A optional int32, specifying the output data type. Defaults to "DT_INT32".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 seed: int32,int64
- input2 counts: double,float16,float32,int32,int64
- input3 probs: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomBinomial operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
