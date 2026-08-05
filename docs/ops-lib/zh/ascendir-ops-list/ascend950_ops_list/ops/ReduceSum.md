# ReduceSum

```c
REG_OP(ReduceSum)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, true)
    .OP_END_FACTORY_REG(ReduceSum)
```

## Brief

Computes the sum of elements across dimensions of a tensor.

## Inputs

Two inputs, including:
- x: A tensor. Must be one of the following types:
complex128, complex64, double, float32, float16, int16, int32, int64,
int8, qint32, qint8, quint8, uint16, uint32, uint64, uint8, bfloat16,
complex32.
- axes: A 1D list or tuple of IndexNumberType(int32 or int64).
Specifies the dimensions to reduce.

## Outputs

y: The reduced tensor. Has the same type and format as input "x".

## Attributes

keep_dims: An optional bool. If "true", retains reduced dimensions with
length 1. Defaults to "false".
noop_with_empty_axes: An optional bool. Defaults to "true" .
- If true, when axes = [], not reduce.
- If false, when axes = [], reduce all.
This attribute is valid only for Ascend950 AI Processors and later products.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int32,int64
- input1 axes: int32,int64
- output0 y: bfloat16,float16,float32,int32,int64
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 axes: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- The value range of "axes" is [-dims, dims - 1]. "dims"
indicates the dimension length of "x".
- When converting ONNX to OM, if the axes of the ReduceSum operator is empty,
it is recommended to use the sum function with dim explicitly set to all axes
(e.g., dim=[0, 1, 2]) to prevent shape inference errors.

## Third-party framework compatibility

Compatible with the TensorFlow operator Sum.


---

[Back to Operator Specifications (Ascend950)](../README.md)
