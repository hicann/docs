# LpNormV2

```c
REG_OP(LpNormV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(p, Float, 2.0)
    .ATTR(axes, ListInt, {})
    .ATTR(keepdim, Bool, false)
    .ATTR(epsilon, Float, 1e-12f)
    .OP_END_FACTORY_REG(LpNormV2)
```

## Brief

Computes Lp norm.

## Inputs

x: A ND tensor of dtype float16, bfloat16, float32.

## Outputs

y: A ND tensor has the same dtype as "x". The shape of "y" is depending on "axes" and "keepdim".

## Attributes

- p: An optional float, "inf" or "-inf", indicates the order of norm. Default is 2.0.
- axes: ListInt, an optional attribute, indicates dimensions over which to compute the norm.
Default is {}, meaning all axes will be computed.
- keepdim: An optional bool. If set to true, the reduced dimensions are retained in the result
as dimensions with size one. Default is false.
- epsilon: An optional float. A value added to the denominator for numerical stability. Default is 1e-12.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

- When the attribute "p" is negative, there may be precision difference in the calculation results.
- When the attribute "axes" is specified as the axis with a shape dimension value of 1 in the input tensor,
there may be precision difference in the calculation results.
- When the tensor "x" is empty and "p" < 0 or "p" is infinity, we cannot reduce the whole tensor or reduce
over an empty dimension.

## Third-party framework compatibility

Compatible with the Pytorch operator LpNorm.


---

[Back to Operator Specifications (Ascend950)](../README.md)
