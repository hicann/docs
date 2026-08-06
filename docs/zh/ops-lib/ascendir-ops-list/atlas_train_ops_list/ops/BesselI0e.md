# BesselI0e

```c
REG_OP(BesselI0e)
    .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(BesselI0e)
```

## Brief

Computes the Bessel i0e function of "x" element-wise.
Exponentially scaled modified Bessel function of order 0
defined as: bessel_i0e(x) = exp(-abs(x)) bessel_i0(x).
This function is faster and numerically stabler than "bessel_i0(x)".

## Inputs

x: A tensor of type bfloat16, float16, float32, or float64.

## Outputs

y: A tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator BesselI0e.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
