# Conj

```c
REG_OP(Conj)
    .INPUT(input, TensorType({DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(output, TensorType({DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Conj)
```

## Brief

Returns the complex conjugate of a complex number.

## Inputs

input:A Tensor.

## Outputs

output:A Tensor. Has the same shape as input.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU

## Third-party framework compatibility.

Compatible with tensorflow output operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
