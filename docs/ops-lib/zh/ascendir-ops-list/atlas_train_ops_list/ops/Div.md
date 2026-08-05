# Div

```c
REG_OP(Div)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT32,
                           DT_DOUBLE, DT_INT64, DT_UINT16, DT_INT16,
                           DT_COMPLEX64, DT_COMPLEX128, DT_BF16, DT_COMPLEX32}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT32,
                           DT_DOUBLE, DT_INT64, DT_UINT16, DT_INT16,
                           DT_COMPLEX64, DT_COMPLEX128, DT_BF16, DT_COMPLEX32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT32,
                           DT_DOUBLE, DT_INT64, DT_UINT16, DT_INT16,
                           DT_COMPLEX64, DT_COMPLEX128, DT_BF16, DT_COMPLEX32}))
    .OP_END_FACTORY_REG(Div)
```

## Brief

Returns x1/x2 element-wise. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types:
   float16, float32, int32, int8, uint8, float64, int64, uint16, int16,
   complex32, complex64, complex128, bfloat16, the format can be [NCHW,NHWC,ND].
- x2: A ND Tensor. Has the same dtype and format as input "x1".

## Outputs

y: A ND Tensor. Has the same dtype and format as input "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int32,uint8
- input1 x2: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator Div.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
