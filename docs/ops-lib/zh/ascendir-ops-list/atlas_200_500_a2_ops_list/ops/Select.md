# Select

```c
REG_OP(Select)
    .INPUT(condition, TensorType({DT_BOOL}))
    .INPUT(x1, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .INPUT(x2, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .OP_END_FACTORY_REG(Select)
```

## Brief

Selects elements from "x1" or "x2", depending on "condition" . 

## Inputs

Three inputs, including:
- condition: A tensor of type bool. Select x1 or x2 depending on this condition,
when condition is true, return x1, otherwise return x2.
- x1: A tensor. Must be one of the following types: bfloat16, float16, float32,
int32, int8, uint8, int16, uint16, double, complex64, int64, complex128, bool,
qint8, quint8, qint16, quint16, qint32, uint32, uint64, string.
Format:ND
- x2: A tensor of the same type, size, and shape as "x1". Format:ND

## Outputs

y: A Tensor. Has the same type as "x1". format:ND

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 condition: bool
- input1 x1: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input2 x2: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Select.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
