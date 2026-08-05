# Unpack

```c
REG_OP(Unpack)
    .INPUT(x, TensorType::BasicType())
    .DYNAMIC_OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(num, Int)
    .ATTR(axis, Int, 0)
    .OP_END_FACTORY_REG(Unpack)
```

## Brief

Unpacks the given dimension of a rank-R Tensor "x" into rank-(R-1)
tensors.

## Inputs

x: A rank-R tensor (R > 0) of type BasicType.(BasicType includes:
complex128, complex64, double, float32, float16, int16, int32, int64, int8,
qint16, qint32, qint8, quint16, quint8, uint16, uint32, uint64, uint8,
bfloat16, complex32.) 

## Outputs

y: Dynamic output. The list of Tensor objects unpacked from "x", of type BasicType . 

## Attributes

- num: A required int, specifying the number of tensors to be unpacked to.
Defaults to "None".
- axis: An optional int, specifying the axis to unpack along. The value range
is [-R, R). Defaults to "0". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

For the ND format, "axis" is in the range [-R, R). 

## Third-party framework compatibility

Compatible with the TensorFlow operator Unstack.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
