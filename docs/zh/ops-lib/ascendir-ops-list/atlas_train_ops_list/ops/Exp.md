# Exp

```c
REG_OP(Exp)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .ATTR(base, Float, -1.0)
    .ATTR(scale, Float, 1.0)
    .ATTR(shift, Float, 0.0)
    .OP_END_FACTORY_REG(Exp)
```

## Brief

Computes the exponential of "x" element-wise.

## Inputs

One input:
x: A ND tensor. Must be one of the following types: bfloat16, float16, float32, double, complex64, complex128.
Only when x's dtype is bfloat16, float16 or float32, attributes are valid and can be set.
When x's dtype is double, complex64, complex128, attributes are invalid.

## Outputs

y: A ND tensor of the same dtype as "x".

## Attributes

- base: An optional attribute of type float32, specifying the base gamma. Must be positive or "-1.0", defaults to "-1.0".
- scale: An optional attribute of type float32, specifying the scale alpha. Defaults to "1.0".
- shift: An optional attribute of type float32, specifying the shift beta. Defaults to "0.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64
- output0 y: complex64

## Third-party framework compatibility

Compatible with TensorFlow operator Exp.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
