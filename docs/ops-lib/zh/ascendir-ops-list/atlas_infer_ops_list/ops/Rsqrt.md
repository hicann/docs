# Rsqrt

```c
REG_OP(Rsqrt)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Rsqrt)
```

## Brief

Computes reciprocal of square root of "x" element-wise: y = 1/sqrt{x}.

## Inputs

x: An ND or 5HD tensor. Must be one of the following types: bfloat16, float, double, float16,
complex64, complex128.

## Outputs

y: An ND or 5HD tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Rsqrt.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
