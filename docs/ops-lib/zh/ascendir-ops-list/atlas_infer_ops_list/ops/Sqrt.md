# Sqrt

```c
REG_OP(Sqrt)
    .INPUT(x, TensorType{(DT_BF16, DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128)})
    .OUTPUT(y, TensorType{(DT_BF16, DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128)})
    .OP_END_FACTORY_REG(Sqrt)
```

## Brief

Computes square root of x element-wise.

## Inputs

 x: A ND Tensor. Must be one of the following types:bfloat16 float16, float32, complex128, complex64, float64. 

## Outputs

y: A ND Tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Sqrt.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
