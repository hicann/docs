# Tanh

```c
REG_OP(Tanh)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Tanh)
```

## Brief

Computes hyperbolic tangent of "x" element-wise . 

## Inputs

One input: 
x: A Tensor that supports the data type UnaryDataType. 

## Outputs

y: A Tensor with the same dtype and shape of input "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Tanh.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
