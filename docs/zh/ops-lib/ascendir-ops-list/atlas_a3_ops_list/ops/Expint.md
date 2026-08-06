# Expint

```c
REG_OP(Expint)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(Expint)
```

## Brief

Computes the expint(x).

## Inputs

One input:
x: An ND tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32, double.

## Outputs

y: A ND Tensor of the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with TensorFlow operator Expint.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
