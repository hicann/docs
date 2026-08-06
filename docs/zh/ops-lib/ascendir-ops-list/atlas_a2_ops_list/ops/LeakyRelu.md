# LeakyRelu

```c
REG_OP(LeakyRelu)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_BF16}))
    .ATTR(negative_slope, Float, 0.0)
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(LeakyRelu)
```

## Brief

Computes the output as x if x > 0 and negative_slope * x if x <= 0 .

## Inputs

One input:
x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bfloat16, float32, float16, double.

## Outputs

y: A Tensor. Has the same type, format and shape as "x".

## Attributes

negative_slope: A float32. Defaults to "0.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: bfloat16,double,float16,float32
- output0 y: bfloat16,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator LeakyRelu.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
