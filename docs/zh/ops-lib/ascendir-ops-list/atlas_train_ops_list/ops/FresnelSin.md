# FresnelSin

```c
REG_OP(FresnelSin)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(FresnelSin)
```

## Brief

Computes fresnel_sin of x element-wise.

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
 bfloat16, float16, float32, double.

## Outputs

y: A tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator FresnelSin.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
