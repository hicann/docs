# Log1p

```c
REG_OP(Log1p)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Log1p)
```

## Brief

Computes the logarithm of (x + 1) element-wise, y = ln(x + 1).

## Inputs

One input:
x: A ND Tensor. Must be one of the following types: bfloat16, float16, float32, double, complex64, complex128. 

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

Compatible with TensorFlow operator Log1p.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
