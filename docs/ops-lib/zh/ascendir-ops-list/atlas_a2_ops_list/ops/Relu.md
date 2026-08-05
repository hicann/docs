# Relu

```c
REG_OP(Relu)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE,
                          DT_INT8, DT_INT32, DT_INT16, DT_INT64,
                          DT_UINT8, DT_UINT16, DT_QINT8, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE,
                           DT_INT8, DT_INT32, DT_INT16, DT_INT64,
                           DT_UINT8, DT_UINT16, DT_QINT8, DT_BF16}))
    .OP_END_FACTORY_REG(Relu)
```

## Brief

Computes rectified linear: "max(x, 0)".

## Inputs

x: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
float32, float64, int32, uint8, int16, int8, int64, uint16, float16, qint8, bfloat16.

## Outputs

y: A tensor. Has the same type as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int32,int64
- output0 y: bfloat16,float16,float32,int8,int32,int64
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

- Compatible with the TensorFlow operator Relu.
- Compatible with the Caffe operator ReLULayer.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
