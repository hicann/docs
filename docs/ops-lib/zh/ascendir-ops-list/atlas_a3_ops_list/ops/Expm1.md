# Expm1

```c
REG_OP(Expm1)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Expm1)
```

## Brief

Computes the exp(x) - 1 element-wise, y = e^x - 1.

## Inputs

One input:
x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32, double, complex64, complex128.

## Outputs

y: A ND Tensor of the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Expm1.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
