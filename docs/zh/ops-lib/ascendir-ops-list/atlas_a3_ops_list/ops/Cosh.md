# Cosh

```c
REG_OP(Cosh)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Cosh)
```

## Brief

Computes cosine of "x" element-wise.

## Inputs

x: A ND Tensor of type bfloat16, float16, float32, double, complex64, complex128.
the format can be [NCHW,NHWC,ND]. 

## Outputs

y: A ND Tensor. Has the same dtype as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Cosh. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
