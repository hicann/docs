# Asinh

```c
REG_OP(Asinh)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Asinh)
```

## Brief

Computes inverse hyperbolic sine of x element-wise.
Given an input tensor, this function computes inverse hyperbolic sine for every element in the tensor.

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32, float64, complex64, complex128.

## Outputs

y: A tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Asinh.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
