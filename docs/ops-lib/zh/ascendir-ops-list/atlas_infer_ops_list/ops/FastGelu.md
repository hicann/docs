# FastGelu

```c
REG_OP(FastGelu)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(FastGelu)
```

## Inputs

One input, including:
x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32

## Outputs

y: A Tensor. Has the same type, format and shape as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator FastGelu


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
