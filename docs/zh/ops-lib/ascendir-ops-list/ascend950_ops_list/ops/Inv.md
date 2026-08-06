# Inv

```c
REG_OP(Inv)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(Inv)
```

## Brief

Computes the reciprocal of "x".

## Inputs

x: An ND tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32, int32, int64, double, complex64, complex128.

## Outputs

y: A ND Tensor. Must be one of the following type: float16, bfloat16, float32, int32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Inv.


---

[Back to Operator Specifications (Ascend950)](../README.md)
