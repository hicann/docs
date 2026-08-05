# Lgamma

```c
REG_OP(Lgamma)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16}))
    .OP_END_FACTORY_REG(Lgamma)
```

## Brief

Computes the log of the absolute value of Gamma(x) element-wise.

## Inputs

- x:A Tensor. Must be one of the following types: float, double, float16.

## Outputs

y:A Tensor. Has the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility.

Compatible with tensorflow Lgamma operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
