# Pack

```c
REG_OP(Pack)
    .DYNAMIC_INPUT(x, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .ATTR(axis, Int, 0)
    .ATTR(N, Int, 1)
    .OP_END_FACTORY_REG(Pack)
```

## Brief

Packs the list of tensors in values into a tensor with rank one higher
than each tensor in values, by packing them along the axis dimension.
Given a list of length N of tensors of shape (A, B, C); if axis == 0 then
the output tensor will have the shape (N, A, B, C) .

## Inputs

x: A list of N Tensors. Must be one of the following types: complex128,
complex64, double, float32, float16, int16, int32, int64, int8, qint16,
qint32, qint8, quint16, quint8, uint16, uint32, uint64, uint8, bfloat16,
complex32. It's a dynamic input.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- axis: An optional int, default value is 0.
    Dimension along which to pack. The range is [-(R+1), R+1).
- N: An optional int, default value is 1. Number of tensors.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int64
- output0 y: float16,float32,int8,int64
### AI CPU
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Pack.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
