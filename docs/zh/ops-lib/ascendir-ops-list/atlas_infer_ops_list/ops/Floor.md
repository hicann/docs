# Floor

```c
REG_OP(Floor)
  .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
  .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
  .OP_END_FACTORY_REG(Floor)
```

## Brief

Returns element-wise largest integer not greater than "x".

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16, float32, double.

## Outputs

y: A ND Tensor of the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Floor.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
