# Erfc

```c
REG_OP(Erfc)
    .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(Erfc)
```

## Brief

Computes the Gauss complementary error function of "x" element-wise.

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
bfloat16, float16 ,float32, double.

## Outputs

y: A Tensor. Has the same type as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Erfc.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
