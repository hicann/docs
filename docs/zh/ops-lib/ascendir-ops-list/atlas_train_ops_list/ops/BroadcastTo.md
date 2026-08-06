# BroadcastTo

```c
REG_OP(BroadcastTo)
    .INPUT(x, TensorType({BasicType(), DT_BOOL, DT_STRING, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_STRING, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OP_END_FACTORY_REG(BroadcastTo)
```

## Brief

Broadcasts an array for a compatible shape.
 Broadcasting is the process of making arrays to have compatible shapes
 for arithmetic operations. Two shapes are compatible if for each
 dimension pair they are either equal or one of them is one. When trying
 to broadcast a Tensor to a shape, it starts with the trailing dimensions,
 and works its way forward.

## Inputs

- x: A tensor, support all dtype include(BasicType, bool, string, hifloat8, float8_e5m2, float8_e4m3fn).
- shape: A tensor.
    A 1D tensor of type int32 or int64, for the shape of the desired output.

## Outputs

y: A tensor. Has the same tensor info of "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int32,int64,uint8,uint32
- input1 shape: int32,int64
- output0 y: bool,float16,float32,int8,int32,int64,uint8,uint32
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input1 shape: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator BroadcastTo.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
