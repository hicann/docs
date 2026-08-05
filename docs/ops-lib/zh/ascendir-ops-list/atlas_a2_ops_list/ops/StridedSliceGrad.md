# StridedSliceGrad

```c
REG_OP(StridedSliceGrad)
    .INPUT(shape, TensorType::IndexNumberType())
    .INPUT(begin, TensorType::IndexNumberType())
    .INPUT(end, TensorType::IndexNumberType())
    .INPUT(strides, TensorType::IndexNumberType())
    .INPUT(dy, TensorType::BasicType())
    .OUTPUT(output, TensorType::BasicType())
    .ATTR(begin_mask, Int, 0)
    .ATTR(end_mask, Int, 0)
    .ATTR(ellipsis_mask, Int, 0)
    .ATTR(new_axis_mask, Int, 0)
    .ATTR(shrink_axis_mask, Int, 0)
    .OP_END_FACTORY_REG(StridedSliceGrad)
```

## Brief

Since StridedSlice cuts out pieces of its "input" which is size "dy",
its gradient will have the same shape (which is passed here as "shape").
The gradient will be zero in any element that the slice does not select .

## Inputs

Five inputs, including:
- shape: A Tensor of type int32 or int64.
- begin: A Tensor of type int32 or int64.
The index of the first value to select.
- end: A Tensor of type int32 or int64.
The index of the last value to select.
- strides: A Tensor of type int32 or int64, for the increment.
- dy: A Tensor. Supported dtype is BasicType.

## Outputs

output: A Tensor has the same type as "dy" . 

## Attributes

- begin_mask: A Tensor of type int32.
A bitmask where a bit "i" being "1" means to ignore the begin
value and instead use the largest interval possible.
- end_mask: A Tensor of type int32.
Analogous to "begin_mask".
- ellipsis_mask: A Tensor of type int32.
A bitmask where bit "i" being "1" means the "i"th position
is actually an ellipsis.
- new_axis_mask: A Tensor of type int32.
A bitmask where bit "i" being "1" means the "i"th
specification creates a new shape 1 dimension.
- shrink_axis_mask: A Tensor of type int32.
A bitmask where bit "i" implies that the "i"th
specification should shrink the dimensionality . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 shape: int32,int64
- input1 begin: int32,int64
- input2 end: int32,int64
- input3 strides: int32,int64
- input4 dy: bfloat16,float16,float32,int32
- output0 output: bfloat16,float16,float32,int32
### AI CPU
- input0 shape: int32,int64
- input1 begin: int32,int64
- input2 end: int32,int64
- input3 strides: int32,int64
- input4 dy: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- output0 output: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator StridedSliceGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
