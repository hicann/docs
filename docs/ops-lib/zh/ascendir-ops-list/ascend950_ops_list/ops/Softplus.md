# Softplus

```c
REG_OP(Softplus)
    .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(Softplus)
```

## Brief

Computes softplus: log(exp(x) + 1) .

## Inputs

One input:
x: A Tensor of type bfloat16, float16 or float32. Up to 8D . 

## Outputs

y: The activations tensor. Has the same type and format as input "x"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Softplus.


---

[Back to Operator Specifications (Ascend950)](../README.md)
