# Swish

```c
REG_OP(Swish)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(scale, Float, 1.0)
    .OP_END_FACTORY_REG(Swish)
```

## Brief

Computes the for the Swish of "x" .

## Inputs

One input, including:
x: A tensor, which supports 1D-8D defaultly and must be one of the following types: float16, bfloat16, float32. 

## Outputs

y: A tensor of the same type, shape and format as "x", and y = x / (1 + e ^ (-scale * x)). 

## Attributes

scale: scalar parameter, the multiplier of x. Must be one of the following types: float. Default value = 1.0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Torch operator Swish


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
