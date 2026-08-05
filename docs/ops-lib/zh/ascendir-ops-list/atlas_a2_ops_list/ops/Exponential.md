# Exponential

```c
REG_OP(Exponential)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(lambda, Float, 1)
    .ATTR(seed, Int, 0)
    .OP_END_FACTORY_REG(Exponential)
```

## Brief

Outputs random values from the Exponential distribution(s) described by rate . 

## Inputs

Inputs include:
- x: A Tensor. Must be one of the following types: float16, float32, double.

## Outputs

y: A Tensor of type dtype float16, float32, double. 

## Attributes

- lambda: An optional float. Defaults to 1.
- seed: An optional int. Defaults to 0.The random number generator is seeded by the given seed.
Otherwise, it is seeded by a random seed. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

The implementation for Exponential on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow Exponential operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
