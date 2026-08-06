# Cummin

```c
REG_OP(Cummin)
    .INPUT(x, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .OUTPUT(indices, TensorType::BasicType())
    .REQUIRED_ATTR(axis, Int)
    .OP_END_FACTORY_REG(Cummin)
```

## Brief

Returns a namedtuple (values, indices) where values is the cumulative
the cumulative minimum of elements of input in the dimension dim.
And indices is the index location of each maximum value found in the dimension dim. 

## Inputs

One inputs, including:
x: A tensor . Must be one of the types in BasicType:
complex128, complex64, double, float32, float16, int16, int32, int64, int8, qint16,
qint32, qint8, quint16, quint8, quint16, uint32, uint64, uint8, bfloat16, complex32.

## Outputs

- y: A Tensor with the same type and shape of x's. Must be one of the types in BasicType:
complex128, complex64, double, float32, float16, int16, int32, int64, int8, qint16,
qint32, qint8, quint16, quint8, quint16, uint32, uint64, uint8, bfloat16, complex32.
- indices: A Tensor with the int32 type and the same shape of x's. Must be one of the types in BasicType:
complex128, complex64, double, float32, float16, int16, int32, int64, int8, qint16,
qint32, qint8, quint16, quint8, quint16, uint32, uint64, uint8, bfloat16, complex32.

## Attributes

axis: Axis along which to cummin. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 indices: int32,int64

## Third-party framework compatibility

Compatible with the Pytorch operator Cummin. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
