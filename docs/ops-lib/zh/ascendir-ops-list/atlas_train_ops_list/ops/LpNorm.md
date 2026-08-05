# LpNorm

```c
REG_OP(LpNorm)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(p, Int, 2)
    .ATTR(axes, ListInt, {})
    .ATTR(keepdim, Bool, false)
    .ATTR(epsilon, Float, 1e-12f)
    .OP_END_FACTORY_REG(LpNorm)
```

## Brief

Computes Lp norm.

## Inputs

x: A ND tensor of type float16, bfloat16, float32.

## Outputs

y: A ND tensor has the same dtype as "x". The shape of "y" is depending on "axes" and "keepdim".

## Attributes

- p: An optional int, "inf" or "-inf", default value is 2, p >= 0.
- axes: ListInt, an optional attribute, indicates dimensions over which to compute the norm.
Default is {}, meaning all axes will be computed.
- keepdim: An optional bool. If set to true, the reduced dimensions are retained in the result
as dimensions with size one. Default is false.
- epsilon: An optional float. A value added to the denominator for numerical stability. Default is 1e-12.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

This operator will be deprecated in the future. Replace it with LpNormV2 operator.

## Third-party framework compatibility

Compatible with the Pytorch operator LpNorm.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
