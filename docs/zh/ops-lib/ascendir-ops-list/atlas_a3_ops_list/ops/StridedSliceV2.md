# StridedSliceV2

```c
REG_OP(StridedSliceV2)
    .INPUT(x, TensorType({BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0}))
    .INPUT(begin, TensorType::IndexNumberType())
    .INPUT(end, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(axes, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(strides, TensorType::IndexNumberType())
    .ATTR(begin_mask, Int, 0)
    .ATTR(end_mask, Int, 0)
    .ATTR(ellipsis_mask, Int, 0)
    .ATTR(new_axis_mask, Int, 0)
    .ATTR(shrink_axis_mask, Int, 0)
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0}))
    .OP_END_FACTORY_REG(StridedSliceV2)
```

## Brief

Extracts a strided slice of a tensor. Roughly speaking, this op
  extracts a slice of size (end-begin)/stride from the given input tensor.
  Starting at the location specified by begin the slice continues by
  adding stride to the index until all dimensions are not less than end. 

## Inputs

Five inputs, including:
- x: A Tensor. 1-8 dimensions. Must be one of the following types:
double, float32, float16, bfloat16, complex32, complex64, complex128,
int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint16, quint16, qint32, bool, hifloat8,
float8_e5m2, float8_e4m3fn, float8_e8m0.
- begin: A Tensor of type int32 or int64, for the index of the first value to select.
    Elements in begin with negative values are interpreted as indices from the end of the dimension.
- end: A Tensor of type int32 or int64, for the index of the last value to select.
    Elements in end with negative values are interpreted as indices from the end of the dimension.
- axes: A Tensor of type int32 or int64, indicate axis to be select.
    When not provided, slices all dimensions.
- strides: A Tensor of type int32 or int64, for the increment.
    When not provided, stride defaults to 1. All elements in strides must be non-zero integers. 

## Outputs

y: A Tensor that has the same type as "x".

## Attributes

- begin_mask: An attribute of type Int.
    A bitmask where a bit "i" being "1" means to ignore the begin
    value and instead use the largest interval possible. Default value is 0.
- end_mask: An attribute of type Int.
    Analogous to "begin_mask". Default value is 0.
- ellipsis_mask: An attribute of type Int.
    A bitmask where bit "i" being "1" means the "i"th position
    is actually an ellipsis. Default value is 0.
- new_axis_mask: An attribute of type Int.
    A bitmask where bit "i" being "1" means the "i"th
    specification creates a new shape 1 dimension. Default value is 0.
- shrink_axis_mask: An attribute of type Int.
    A bitmask where bit "i" implies that the "i"th
    specification should shrink the dimensionality. Default value is 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8
- input1 begin: int32,int64
- input2 end: int32,int64
- input3 axes: int32,int64
- input4 strides: int32,int64
- output0 y: bool,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8

## Third-party framework compatibility

Compatible with the onnx operator Slice.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
