# Ndtri

```c
REG_OP(Ndtri)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(Ndtri)
```

## Brief

Computes ndtri element-wise (y = sqrt(2) * erfinv(2 * x - 1)).

## Inputs

One input, including: 
x: A ND Tensor. Must be one of the following types: bfloat16, float16,
float32, double. 

## Outputs

y: A ND Tensor. Has the same dtype and format as input "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Ndtri.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
