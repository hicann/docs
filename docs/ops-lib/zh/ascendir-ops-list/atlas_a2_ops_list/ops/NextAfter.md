# NextAfter

```c
REG_OP(NextAfter)
    .INPUT(x1, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(NextAfter)
```

## Brief

Returns the next representable value of x1 in the direction of x2, element-wise. 

## Inputs

The input X1 and x2 must have the same type. Inputs include:
- x1:A Tensor. Must be one of the following types: float32, double.
- x2:A Tensor. Must have the same type as x1.

## Outputs

output:A Tensor. Has the same type as x1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: double,float32
- input1 x2: double,float32
- output0 output: double,float32

## Third-party framework compatibility

Compatible with tensorflow NextAfter operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
