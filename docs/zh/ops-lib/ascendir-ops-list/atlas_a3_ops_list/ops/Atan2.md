# Atan2

```c
REG_OP(Atan2)
    .INPUT(x1, TensorType({FloatingDataType, DT_BF16}))
    .INPUT(x2, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(Atan2)
```

## Brief

Computes arctangent of x1/x2 element-wise, respecting signs of the arguments. Support broadcasting operations.

## Inputs

- x1: A ND tensor. Must be one of the following types: bfloat16, float16, float32, float64
- x2: A ND tensor of the same dtype as "x1".

## Outputs

y: A ND tensor. Has the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x1: double,float16,float32
- input1 x2: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Atan2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
