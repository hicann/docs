# Erf

```c
REG_OP(Erf)
    .INPUT(x, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(y, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(Erf)
```

## Brief

Computes the Gauss error function of 'x' element-wise. 

## Inputs

x: A Tensor of type bfloat16, float16, float32 or double. the format can be
   [NCHW,NHWC,ND]

## Outputs

y: A Tensor. Has the same type, format and shape as 'x'. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Erf.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
