# TanhGrad

```c
REG_OP(TanhGrad)
    .INPUT(y, TensorType::UnaryDataType())
    .INPUT(dy, TensorType::UnaryDataType())
    .ATTR(complex_conj, Bool, false)
    .OUTPUT(z, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(TanhGrad)
```

## Brief

Computes the gradient for the tanh of "x" .

## Inputs

Two inputs, including:
- y: A Tensor. Must be one of the following types: float16, float32, bfloat16,
    double, complex64, complex128.
- dy: A Tensor of the same type as "y" .

## Outputs

z: A Tensor. Has the same type as "y".

## Attributes

- complex_conj: An optional attribute indicates whether to use conjugate operations for complex dtype.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: bfloat16,float16,float32
- input1 dy: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32
### AI CPU
- input0 y: complex64,complex128,double,float16,float32
- input1 dy: complex64,complex128,double,float16,float32
- output0 z: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator TanhGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
