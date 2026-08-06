# LpNormUpdateV2

```c
REG_OP(LpNormUpdateV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(p, Float, 2.0)
    .ATTR(epsilon, Float, 1e-12f)
    .OP_END_FACTORY_REG(LpNormUpdateV2)
```

## Brief

Computes LpNormUpdate.

## Inputs

x: A ND tensor of dtype float16, bfloat16, float32.

## Outputs

y: A ND tensor has the same shape and dtype as "x".

## Attributes

- p: An optional float, "inf" or "-inf", indicates the order of norm. Default is 2.0.
- epsilon: An optional float. A value added to the denominator for numerical stability. Default is 1e-12.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

When the attribute "p" is negative, there may be precision difference in the calculation results.

## Third-party framework compatibility

Compatible with the Pytorch operator LpNormUpdate.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
