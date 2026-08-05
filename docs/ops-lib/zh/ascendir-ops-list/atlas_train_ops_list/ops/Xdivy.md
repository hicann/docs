# Xdivy

```c
REG_OP(Xdivy)
    .INPUT(x1, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128}))
    .INPUT(x2, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Xdivy)
```

## Brief

Computes x1/x2 element-wise, if x1 == 0, return 0. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types: bfloat16, float16, float32,
double, complex64, complex128.
- x2: A ND Tensor. Has the same dtype as "x1".

## Outputs

y: A ND Tensor. Has the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32
- input1 x2: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32
- input1 x2: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Xdivy.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
