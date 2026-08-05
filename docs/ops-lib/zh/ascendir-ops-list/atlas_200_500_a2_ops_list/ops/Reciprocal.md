# Reciprocal

```c
REG_OP(Reciprocal)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16,
                          DT_COMPLEX64, DT_COMPLEX128, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16,
                           DT_COMPLEX64, DT_COMPLEX128, DT_BF16}))
    .OP_END_FACTORY_REG(Reciprocal)
```

## Brief

Computes the reciprocal of "x".

## Inputs

One inputs, include:
x:A ND Tensor of type float16, float32, double,
    complex64, complex128, bfloat16. the format can be [NCHW,NHWC,ND]

## Outputs

y:A ND Tensor with same type as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Reciprocal.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
