# OneHot

```c
REG_OP(OneHot)
    .INPUT(x, TensorType({DT_UINT8, DT_INT32, DT_INT64}))
    .INPUT(depth, TensorType({DT_INT32, DT_INT64}))
    .INPUT(on_value, TensorType::BasicType())
    .INPUT(off_value, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .ATTR(axis, Int, -1)
    .OP_END_FACTORY_REG(OneHot)
```

## Brief

Returns a one-hot tensor. The locations represented by index in "x" take value "on_value",
        while all other locations take value "off_value" .

## Inputs

Four inputs, including:
- x: A 1-7D tensor of indices, format supports ND, and data type must be one of the following types: int32, uint8, int64.
- depth: A scalar which is the depth of the one hot dimension, format supports ND, and data type must be int32 or int64
    Its shape can be 1-8D, but only the first element make sense.
- on_value: A scalar. The value to fill in output when indices[j] = i, format supports ND.
    Must be one of the following types: float16, float32, int64, int32, int8, uint8.
    Its shape can be 1-8D, but only the first element make sense.
- off_value: A scalar. The value to fill in output when indices[j] != i, format supports ND.
    Has the same type as "on_value". Its shape can be 1-8D, but only the first element make sense.

## Outputs

y: A 1-8D tensor. Has the same type as "on_value" . 

## Attributes

axis: The axis to fill. An int with a minimum value of -1 and a maximum value of dims of x. Defaults to "-1"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int32,int64
- input1 depth: int32,int64
- input2 on_value: float16,float32,int32,int64
- input3 off_value: float16,float32,int32,int64
- output0 y: float16,float32,int32,int64
### AI CPU
- input0 x: int32,int64,uint8
- input1 depth: int32
- input2 on_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input3 off_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator OneHot.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
