# StatelessParameterizedTruncatedNormal

```c
REG_OP(StatelessParameterizedTruncatedNormal)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .INPUT(means, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(stdevs, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(min, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(max, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(StatelessParameterizedTruncatedNormal)
```

## Brief

Outputs random values from a normal distribution. 

## Inputs

Inputs include:
- shape: A Tensor. Must be one of the following types: int32, int64.
The shape of the output tensor. Batches are indexed by the 0th dimension.
- seed: 2 seeds (shape [2]).
- means: A Tensor. Must be one of the following types: float16, float32, double.
- stdevs: A Tensor. Must have the same type as means.
- min: A Tensor. Must have the same type as means. The minimum cutoff. May be -infinity.
- max: A Tensor. Must have the same type as means.

## Outputs

y: A Tensor. Has the same type as means. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 seed: int32,int64
- input2 means: double,float16,float32
- input3 stdevs: double,float16,float32
- input4 min: double,float16,float32
- input5 max: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

The implementation for StatelessParameterizedTruncatedNormal on Ascend uses AICPU, with bad performance. 

## Third-party framework compatibility

- compatible with tensorflow StatelessParameterizedTruncatedNormal operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
