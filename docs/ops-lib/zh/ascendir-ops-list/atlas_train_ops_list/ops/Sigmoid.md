# Sigmoid

```c
REG_OP(Sigmoid)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Sigmoid)
```

## Brief

Compute sigmoid of "x" element-wise .

## Inputs

A Tensor of type complex64, complex128, bfloat16, float16, float32 or double . 

## Outputs

A Tensor. Has the same type as "x" . 
@see Relu()

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Sigmoid.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
