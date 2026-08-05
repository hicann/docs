# Betainc

```c
REG_OP(Betainc)
    .INPUT(a, TensorType({DT_DOUBLE, DT_FLOAT}))
    .INPUT(b, TensorType({DT_DOUBLE, DT_FLOAT}))
    .INPUT(x, TensorType({DT_DOUBLE, DT_FLOAT}))
    .OUTPUT(z, TensorType({DT_DOUBLE, DT_FLOAT}))
    .OP_END_FACTORY_REG(Betainc)
```

## Brief

Compute the regularized incomplete beta integral.

## Inputs

The input b and x must have the same types as a. Inputs include:
- a:A Tensor. Must be one of the following types: float32, double.
- b:A Tensor. Must have the same type as a.
- x:A Tensor. Must have the same type as a.

## Outputs

z:A Tensor. Has the same type as a. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 a: double,float32
- input1 b: double,float32
- input2 x: double,float32
- output0 z: double,float32

## Third-party framework compatibility.

Compatible with tensorflow Betainc operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
