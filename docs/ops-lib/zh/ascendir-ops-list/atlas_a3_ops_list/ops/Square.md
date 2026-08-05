# Square

```c
REG_OP(Square)
    .INPUT(x, TensorType({DT_DOUBLE, DT_FLOAT16, DT_FLOAT, DT_BF16,
                          DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_DOUBLE, DT_FLOAT16, DT_FLOAT, DT_BF16,
                           DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Square)
```

## Brief

Computes square of "x" element-wise.

## Inputs

One input:
x: A ND Tensor. Must be one of the following types: float16, bfloat16, float32, float64, int32, int64, complex64,
   complex128.

## Outputs

y: An ND or 5HD tensor. Support 1D ~ 8D. Shape and dtype of output, should be same shape and type as input.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32,int64
- output0 y: bfloat16,float16,float32,int32,int64
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int32,int64
- output0 y: complex64,complex128,double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with TensorFlow operator Square.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
