# IgammaGradA

```c
REG_OP(IgammaGradA)
    .INPUT(a, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(z, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(IgammaGradA)
```

## Brief

Computes the gradient of igamma(a, x) wrt a.

## Inputs

The input a and x must have the same type. Inputs include:
- a:A Tensor. Must be one of the following types: float32, double.
- x:A Tensor. Must have the same type as a.

## Outputs

y:A Tensor. Has the same type as a. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 a: double,float32
- input1 x: double,float32
- output0 z: double,float32

## Third-party framework compatibility

Compatible with tensorflow IgammaGradA operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
