# ReciprocalGrad

```c
REG_OP(ReciprocalGrad)
    .INPUT(y, TensorType::UnaryDataType())
    .INPUT(dy, TensorType::UnaryDataType())
    .OUTPUT(z, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(ReciprocalGrad)
```

## Brief

Computes the gradient for the inverse of "x" with regard its input. Support broadcasting operations.

## Inputs

- y: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
bfloat16, float, double, complex32, complex64, complex128, float16.
- dy: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
bfloat16, float, double, complex32, complex64, complex128, float16.

## Outputs

z: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
float, double, complex32, complex64, complex128, float16.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: float16,float32
- input1 dy: float16,float32
- output0 z: float16,float32
### AI CPU
- input0 y: complex64,complex128,double,float16,float32
- input1 dy: complex64,complex128,double,float16,float32
- output0 z: complex64,complex128,double,float16,float32

## Attention Constraints

"dy" has the same shape and type as "y".

## Third-party framework compatibility

Compatible with the TensorFlow operator reciprocal_grad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
