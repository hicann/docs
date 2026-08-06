# ReduceMean

```c
REG_OP(ReduceMean)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, true)
    .OP_END_FACTORY_REG(ReduceMean)
```

## Brief

Reduces "x" along the dimensions according to "axis".

## Inputs

Two inputs, including:
- x: A tensor. Must be one of the following types:
complex128, complex64, double, float32, float16, int64, int32, int16, int8,
uint64, uint32, uint16, uint8, bfloat16. The data format supports ND.
- axes: The dimensions to reduce. Must be one of the following types:
int, list, tuple, NoneType. Data type must be int32 or int64.
If None (the default), reduces all dimensions.
Must be in the range [-rank(x), rank(x)).

## Outputs

y: A tensor. Has the same type and format as "x".

## Attributes

- keep_dims: An optional bool. Defaults to false.
If true, retains reduced dimensions with length 1.
If false, the rank of the tensor is reduced by 1 for each entry in axis.
- noop_with_empty_axes: An optional bool. Defaults to true.
If true, when axes = [], not reduce.
If false, when axes = [], reduce all.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 axes: int32,int64
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 axes: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- When converting ONNX to OM, if the axes of the ReduceMean operator is empty,
and noop_with_empty_axes is true, it is recommended to use the mean function with dim explicitly
set to all axes(e.g., dim=[0, 1, 2]) to prevent shape inference errors.

## Third-party framework compatibility

Compatible with the TensorFlow operator ReduceMean.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
