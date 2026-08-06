# Rint

```c
REG_OP(Rint)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(Rint)
```

## Brief

Return element-wise integer closest to x.

## Inputs

One input, include:
x: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
float16, float32, double, bfloat16.

## Outputs

y: A mutable Tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Rint.


---

[Back to Operator Specifications (Ascend950)](../README.md)
