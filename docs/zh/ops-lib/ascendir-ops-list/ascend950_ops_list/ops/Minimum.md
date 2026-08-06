# Minimum

```c
REG_OP(Minimum)
    .INPUT(x1, TensorType({DT_BF16, DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64, DT_INT8, DT_UINT8}))
    .INPUT(x2, TensorType({DT_BF16, DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64, DT_INT8, DT_UINT8}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64, DT_INT8, DT_UINT8}))
    .OP_END_FACTORY_REG(Minimum)
```

## Brief

Returns the min of "x1" and "x2" (i.e. x1 < x2 ? x1: x2) element-wise. Support broadcasting operations. 

## Inputs

Two inputs, include:
- x1: A ND Tensor. Must be one of the following types: bfloat16, float32, float16, double, int32, int64, int8, uint8.
- x2: A ND Tensor of the same dtype as "x1".

## Outputs

y: A ND Tensor of the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int8,int32,int64,uint8
- input1 x2: bfloat16,float16,float32,int8,int32,int64,uint8
- output0 y: bfloat16,float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x1: double,float16,float32,int32,int64
- input1 x2: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator Minimum.


---

[Back to Operator Specifications (Ascend950)](../README.md)
