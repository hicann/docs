# SigmoidGrad

```c
REG_OP(SigmoidGrad)
    .INPUT(y, TensorType(UnaryDataType))
    .INPUT(dy, TensorType(UnaryDataType))
    .OUTPUT(z, TensorType(UnaryDataType))
    .ATTR(complex_conj, Bool, false)
    .OP_END_FACTORY_REG(SigmoidGrad)
```

## Brief

Computes z = (y - y*y)*dy .

## Inputs

- y: The input is Tensor, dtype is UnaryDataType.
- dy: The input is Tensor, dtype is UnaryDataType .

## Outputs

z: The shape of output, dtype is UnaryDataType.

## Attributes

- complex_conj: An optional attribute indicates whether to use conjugate operations for complex dtype. Defaults to "false"

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


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
