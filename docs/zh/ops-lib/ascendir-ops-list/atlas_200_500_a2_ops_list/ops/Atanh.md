# Atanh

```c
REG_OP(Atanh)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Atanh)
```

## Brief

Computes inverse hyperbolic tangent of x element-wise.
Given an input tensor, this function computes inverse hyperbolic tangent for every element in the tensor. 
Input range is [-1,1] and output range is [-inf, inf]. If input is -1, 
output will be -inf and if the input is 1, output will be inf.
Values outside the range will have nan as output.

## Inputs

x: A tensor. Must be one of the following types: bfloat16, float16, float32, float64,
complex32, complex64, complex128.

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

Compatible with the TensorFlow operator Atanh.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
