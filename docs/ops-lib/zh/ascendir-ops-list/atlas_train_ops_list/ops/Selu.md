# Selu

```c
REG_OP(Selu)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(Selu)
```

## Brief

Computes scaled exponential linear: scale * alpha * (exp(x) - 1) .

## Inputs

One input:
x: A Tensor. Support 1D ~ 8D. Must be one of the following types: float16, float, double
int32, int8, bfloat16. format:ND.

## Outputs

y: A Tensor. Has the same type, shape and format as input "x". format:ND.
@see Region()

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32
- output0 y: float16,float32,int8,int32
### AI CPU
- input0 x: double,float16,float32,int8,int32
- output0 y: double,float16,float32,int8,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator Selu.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
