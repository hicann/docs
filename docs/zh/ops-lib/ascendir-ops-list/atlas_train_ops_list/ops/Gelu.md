# Gelu

```c
REG_OP(Gelu)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(Gelu)
```

## Brief

The GELU activation function is x*Φ(x),
where Φ(x) the standard Gaussian cumulative distribution function.

## Inputs

x: A Tensor. Must be one of the following types: bfloat16, float16, float32. 

## Outputs

y: A Tensor. Has the same type as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Gelu.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
