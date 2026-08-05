# Xlog1py

```c
REG_OP(Xlog1py)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
                          DT_COMPLEX128}))
    .INPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
                          DT_COMPLEX128}))
    .OUTPUT(z, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Xlog1py)
```

## Brief

Computes "x" multiplied by the logarithm of y element-wise,
if "x" == 0, return "0". Support broadcasting operations.

## Inputs

Two inputs, including:
- x: A ND Tensor. Must be one of the following types: bfloat16, float16, float32,
double, complex64, complex128.
- y: A ND Tensor. Has the same dtype as "x".

## Outputs

z: A ND Tensor. Has the same dtype as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 y: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Xlog1py.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
