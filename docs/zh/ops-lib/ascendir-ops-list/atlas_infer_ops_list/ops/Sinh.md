# Sinh

```c
REG_OP(Sinh)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Sinh)
```

## Brief

Computes hyperbolic sine of "x" element-wise.

## Inputs

x: An NCHW, NHWC,or ND Tensor that supports the data type UnaryDataType. 

## Outputs

y: A ND Tensor with the same dtype and shape of input "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Sinh. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
