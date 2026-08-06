# Sinc

```c
REG_OP(Sinc)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(Sinc)
```

## Brief

Computes sinc of "x" element-wise.

## Inputs

One input: 
x: An ND Tensor that supports the data type UnaryDataType. 

## Outputs

y: An ND Tensor with the same dtype and shape of input "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Sinc.


---

[Back to Operator Specifications (Ascend950)](../README.md)
