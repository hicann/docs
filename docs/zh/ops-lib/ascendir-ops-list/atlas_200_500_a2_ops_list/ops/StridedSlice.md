# StridedSlice

```c
REG_OP(StridedSlice)
    .INPUT(x, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(begin, TensorType::IndexNumberType())
    .INPUT(end, TensorType::IndexNumberType())
    .INPUT(strides, TensorType::IndexNumberType())
    .ATTR(begin_mask, Int, 0)
    .ATTR(end_mask, Int, 0)
    .ATTR(ellipsis_mask, Int, 0)
    .ATTR(new_axis_mask, Int, 0)
    .ATTR(shrink_axis_mask, Int, 0)
    .OUTPUT(y, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OP_END_FACTORY_REG(StridedSlice)
```

## Brief

Extracts a strided slice of a tensor. Roughly speaking, this op
extracts a slice of size (end-begin)/stride from the given input tensor.
Starting at the location specified by begin the slice continues by
adding stride to the index until all dimensions are not less than end.

## Inputs

Four inputs, including:
- x: A tensor. Must be one of the BasicType: complex128, complex64,
double, float32, float16, int16, int32, int64, int8, qint16, qint32, qint8,
quint16, quint8, uint16, uint32, uint64, uint8, bfloat16, complex32,
hifloat8, float8_e5m2, float8_e4m3fn.Supported format list ["ND"].
- begin: A tensor of IndexNumberType: int32 or int64,
for the index of the first value to select.Supported format list ["ND"].
- end: A tensor of IndexNumberType: int32 or int64,
for the index of the last value to select.Supported format list ["ND"].
- strides: A tensor of IndexNumberType: int32 or int64,
for the increment.Supported format list ["ND"].

## Outputs

y: A tensor. Has the same type as "x".Supported format list ["ND"].

## Attributes

- begin_mask: A tensor of type int includes all types of int.
A bitmask where a bit "i" being "1" means to ignore the begin
value and instead use the largest interval possible.Default value is 0.
- end_mask: A tensor of type int includes all types of int.
Analogous to "begin_mask".Default value is 0.
- ellipsis_mask: A tensor of type int includes all types of int.
A bitmask where bit "i" being "1" means the "i"th position
is actually an ellipsis.Default value is 0.
- new_axis_mask: A tensor of type int includes all types of int.
A bitmask where bit "i" being "1" means the "i"th
specification creates a new shape 1 dimension.Default value is 0.
- shrink_axis_mask: A tensor of type int includes all types of int.
A bitmask where bit "i" implies that the "i"th
specification should shrink the dimensionality.Default value is 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float8_e4m3fn,float8_e5m2,hifloat8
- input1 begin: int32,int64
- input2 end: int32,int64
- input3 strides: int32,int64
- output0 y: float8_e4m3fn,float8_e5m2,hifloat8
### AI CPU
- input0 x: float8_e4m3fn,float8_e5m2,hifloat8
- input1 begin: int32,int64
- input2 end: int32,int64
- input3 strides: int32,int64
- output0 y: float8_e4m3fn,float8_e5m2,hifloat8

## Third-party framework compatibility

Compatible with the TensorFlow operator StridedSlice.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
