# RandomGamma

```c
REG_OP(RandomGamma)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(alpha, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomGamma)
```

## Brief

Outputs random values from the Gamma distribution(s) described by alpha. 

## Inputs

Inputs include:
- shape: A Tensor. Must be one of the following types: int32, int64. 1-D integer tensor.
- alpha: A Tensor. Must be one of the following types: float16, float32, double.

## Outputs

y: A Tensor. Has the same type as alpha. 

## Attributes

- seed: An optional int. Defaults to 0.
- seed2: An optional int. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 alpha: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

The implementation for RandomGamma on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow RandomGamma operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
