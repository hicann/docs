# AddV2

```c
REG_OP(AddV2)
    .INPUT(x1, TensorType({DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX64, DT_BF16,
                           DT_COMPLEX128}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX64, DT_BF16,
                           DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX64, DT_BF16,
                           DT_COMPLEX128}))
    .OP_END_FACTORY_REG(AddV2)
```

## Brief

Returns x1 + x2 element-wise. Support broadcasting operations.

## Inputs

- x1: A tensor. Must be one of the following types: bfloat16, float16, float32, float64,
    uint8, int8, int16, int32, int64, complex64, complex128.
- x2: A tensor of the same dtype as "x1".

## Outputs

y: A tensor. Has the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32,int64
- input1 x2: float16,float32,int32,int64
- output0 y: float16,float32,int32,int64
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8
- input1 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8

## Attention Constraints

AddV2 supports broadcasting.

## Third-party framework compatibility

Compatible with the TensorFlow operator AddV2.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
