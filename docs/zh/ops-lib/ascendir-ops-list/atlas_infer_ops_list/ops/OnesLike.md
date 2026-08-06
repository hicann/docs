# OnesLike

```c
REG_OP(OnesLike)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8,
                          DT_UINT8, DT_INT16, DI_UINT16, DT_INT32,
                          DT_INT64, DT_COMPLEX128, DT_BOOL, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8,
                           DT_UINT8, DT_INT16, DI_UINT16, DT_INT32,
                           DT_INT64, DT_COMPLEX128, DT_BOOL, DT_BF16}))
    .OP_END_FACTORY_REG(OnesLike)
```

## Brief

Returns a tensor of the same shape and type with all elements set to one.

## Inputs

One input:
x: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types: float16,
float32, int8, uint8, int16, uint16, int32, int64, complex128, bool, double, bfloat16.

## Outputs

y: A ND Tensor of the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x: di_uint16,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: di_uint16,double,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with TensorFlow operator OnesLike.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
