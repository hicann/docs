# ClipByValue

```c
REG_OP(ClipByValue)
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16,
                          DT_INT16, DT_INT32, DT_INT64, DT_INT8, DT_QINT32, DT_QINT8,
                          DT_QUINT8, DT_UINT16, DT_UINT8, DT_BF16, DT_COMPLEX32}))
    .INPUT(clip_value_min, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16,
                                       DT_INT16, DT_INT32, DT_INT64, DT_INT8, DT_QINT32, DT_QINT8,
                                       DT_QUINT8, DT_UINT16, DT_UINT8, DT_BF16, DT_COMPLEX32}))
    .INPUT(clip_value_max, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16,
                                       DT_INT16, DT_INT32, DT_INT64, DT_INT8, DT_QINT32, DT_QINT8,
                                       DT_QUINT8, DT_UINT16, DT_UINT8, DT_BF16, DT_COMPLEX32}))
    .OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16,
                            DT_INT16, DT_INT32, DT_INT64, DT_INT8, DT_QINT32, DT_QINT8,
                            DT_QUINT8, DT_UINT16, DT_UINT8, DT_BF16, DT_COMPLEX32}))
    .OP_END_FACTORY_REG(ClipByValue)
```

## Brief

Clips tensor values to a specified min and max.
When the input is bfloat16, float16, float32, int32 or int64, broadcasting operations are supported.  

## Inputs

Three inputs, including:
- x: A ND tensor of type complex128, complex64, double, float32, float16, int16，
int32, int64, int8, qint32, qint8, quint8, uint16, uint8, bfloat16, complex32.
- clip_value_min: A ND tensor of the same dtype as "x".
- clip_value_max: A ND tensor of the same dtype as "x".

## Outputs

y: A ND tensor. Has the same dtype as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32,int64
- input1 clip_value_min: float16,float32,int32,int64
- input2 clip_value_max: float16,float32,int32,int64
- output0 y: float16,float32,int32,int64
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16
- input1 clip_value_min: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16
- input2 clip_value_max: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator ClipByValue.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
