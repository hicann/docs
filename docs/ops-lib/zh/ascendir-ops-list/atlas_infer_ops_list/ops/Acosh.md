# Acosh

```c
REG_OP(Acosh)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Acosh)
```

## Brief

Computes inverse hyperbolic cosine of x element-wise.

## Inputs

x: A ND tensor. Dtype must in TensorType::UnaryDataType().

## Outputs

y: A ND tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Attention Constraints

x Given an input tensor, the function computes inverse hyperbolic cosine of every element.
  Input range must be [1, inf]. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Acosh.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
