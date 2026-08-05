# LpNormUpdate

```c
REG_OP(LpNormUpdate)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(p, Int, 2)
    .ATTR(epsilon, Float, 1e-12f)
    .OP_END_FACTORY_REG(LpNormUpdate)
```

## Brief

Computes LpNormUpdate.

## Inputs

x: A ND tensor of type float16, bfloat16, float32.

## Outputs

y: A ND tensor has the same shape and dtype as "x".

## Attributes

- p: An optional int, "inf" or "-inf", default value is 2, p >= 0.
- epsilon: Float, default is 1e-12.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

This operator will be deprecated in the future. Replace it with LpNormUpdateV2 operator.

## Third-party framework compatibility

Compatible with the Pytorch operator LpNormUpdate.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
