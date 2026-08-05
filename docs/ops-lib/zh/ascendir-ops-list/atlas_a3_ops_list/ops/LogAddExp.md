# LogAddExp

```c
REG_OP(LogAddExp)
    .INPUT(x1, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(x2, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(base, Float, -1.0)
    .ATTR(scale, Float, 1.0)
    .ATTR(shift, Float, 0.0)
    .OP_END_FACTORY_REG(LogAddExp)
```

## Brief

Computes the logarithm of the sum of exponentiations of the inputs element-wise. y = ln(e^x1 + e^x2). 

## Inputs

Two inputs, including:
- x1: A Tensor. Must be one of the following types: bfloat16, float16, float32.
- x2: A Tensor. Must be the same type and shape as "x1".

## Outputs

y: A Tensor of the same type as "x1". 

## Attributes

- base: An optional attribute of type float32, specifying the base gamma. Defaults to "-1.0".
- scale: An optional attribute of type float32, specifying the scale alpha. Defaults to "1.0".
- shift: An optional attribute of type float32, specifying the shift beta. Defaults to "0.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with pytorch operator LogAddExp.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
