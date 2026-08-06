# Power

```c
REG_OP(Power)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(power, Float, 1.0)
    .ATTR(scale, Float, 1.0)
    .ATTR(shift, Float, 0.0)
    .OP_END_FACTORY_REG(Power)
```

## Brief

Computes the output as (shift + scale * x) ^ power .

## Inputs

x: A tensor of type float16, float32 or bfloat16 . 

## Outputs

y: A tensor. Has the same type and shape as "x".

## Attributes

- power: Optional. Must be one of the following types: float32. Defaults to 1.0.
- scale: Optional. Must be one of the following types: float32. Defaults to 1.0.
- shift: Optional. Must be one of the following types: float32. Defaults to 0.0 .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Caffe operator Power.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
