# Ceil

```c
REG_OP(Ceil)
  .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
  .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
  .OP_END_FACTORY_REG(Ceil)
```

## Brief

Returns element-wise smallest integer not less than "x".

## Inputs

x: A ND Tensor of type bfloat16 or float16 or float32 or float64. 

## Outputs

y: A ND Tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Ceil.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
