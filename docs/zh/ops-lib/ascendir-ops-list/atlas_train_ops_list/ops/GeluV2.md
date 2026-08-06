# GeluV2

```c
REG_OP(GeluV2)
    .INPUT(x, "T")
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(approximate, String, "none")
    .OP_END_FACTORY_REG(GeluV2)
```

## Brief

The GELUV2 activation function is x*Φ(x),
where Φ(x) the standard Gaussian cumulative distribution function.

## Inputs

One input, including:
x: A Tensor. Must be one of the following types: bfloat16, float16, float32.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

approximate: A optional string. The gelu approximation algorithm to use: 'none' or 'tanh', default is 'none'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Gelu.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
