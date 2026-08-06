# Acos

```c
REG_OP(Acos)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
                          DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
                           DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Acos)
```

## Brief

Computes acos of x element-wise.

## Inputs

x: A tensor. Must be one of the following types: float16, bfloat16, float32,
    double, int32, int64, complex64, complex128.

## Outputs

y: A tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Acos.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
