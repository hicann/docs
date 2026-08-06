# TruncateDiv

```c
REG_OP(TruncateDiv)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_INT32,
                           DT_DOUBLE, DT_UINT16, DT_INT16, DT_INT64}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_INT32,
                           DT_DOUBLE, DT_UINT16, DT_INT16, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_UINT8, DT_INT32,
                           DT_DOUBLE, DT_UINT16, DT_INT16, DT_INT64}))
    .OP_END_FACTORY_REG(TruncateDiv)
```

## Brief

Returns x1/x2 element-wise for integer types. Support broadcasting operations.

## Inputs

- x1: A ND Tensor. Must be one of the following types:
    float32, float16, bfloat16, int8, uint8, int32, int16,
    uint16, double, int64, complex64, complex128.
- x2: A ND Tensor of the same data type as "x1".

## Outputs

y: A ND Tensor. Has the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int32,uint8
- input1 x2: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x1: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 x2: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Attention Constraints

Broadcasting is supported. 

## Third-party framework compatibility

Compatible with the TensorFlow operator TruncateDiv. 


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
