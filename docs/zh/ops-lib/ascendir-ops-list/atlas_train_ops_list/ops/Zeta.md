# Zeta

```c
REG_OP(Zeta)
    .INPUT(x, TensorType({DT_DOUBLE, DT_FLOAT}))
    .INPUT(q, TensorType({DT_DOUBLE, DT_FLOAT}))
    .OUTPUT(z, TensorType({DT_DOUBLE, DT_FLOAT}))
    .OP_END_FACTORY_REG(Zeta)
```

## Brief

Compute the Hurwitz zeta function.

## Inputs

The input q must be the same type as x. Inputs include:
- x:A Tensor. Must be one of the following types: float32, double.
- q:A Tensor. Must have the same type as x.

## Outputs

z:A Tensor. Has the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float32
- input1 q: double,float32
- output0 z: double,float32

## Attention Constraints

The implementation for Zeta on Ascend uses ai cpu, with bad performance.

## Third-party framework compatibility.

Compatible with tensorflow Zeta operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
