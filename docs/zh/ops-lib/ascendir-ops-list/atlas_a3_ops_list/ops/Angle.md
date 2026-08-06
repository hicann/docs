# Angle

```c
REG_OP(Angle)
    .INPUT(input, TensorType({DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_DOUBLE}))
    .ATTR(Tout, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(Angle)
```

## Brief

deal complex.

## Inputs

- input: An ND tensor of type complex64, complex128.

## Outputs

- output: An ND tensor of type float32, double.

## Attributes

Tout: representing the output of type. Default is float32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128
- output0 output: double,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
