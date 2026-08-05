# MulNoNan

```c
REG_OP(MulNoNan)
     .INPUT(x1, TensorType::NumberType())
     .INPUT(x2, TensorType::NumberType())
     .OUTPUT(y, TensorType::NumberType())
     .OP_END_FACTORY_REG(MulNoNan)
```

## Brief

Computes the product of x and y and returns 0 if the y is zero,
even if x is NaN or infinite. Support broadcasting operations.

## Inputs

Two inputs, including: 
- x1: A ND Tensor. Must be one of the following types: bfloat16, float16, float32,
double, complex64, complex128.
- x2: A ND Tensor. Has the same dtype and shape as "x1".

## Outputs

y: A ND Tensor. Has the same dtype and shape as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32
- input1 x2: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32
- input1 x2: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator MulNoNan.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
