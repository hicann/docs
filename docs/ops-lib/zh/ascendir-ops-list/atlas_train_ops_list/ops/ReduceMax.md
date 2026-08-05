# ReduceMax

```c
REG_OP(ReduceMax)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, true)
    .OP_END_FACTORY_REG(ReduceMax)
```

## Brief

Returns the maximum of elements across dimensions of a Tensor .

## Inputs

Two inputs, including:
- x: A multi-dimensional Tensor of Must be the type of NumberType. Supported format list ["ND"]
- axes: A Scalar of type in IndexNumberType(IndexNumberType includes the
following types: int32, int64.), specifying the axes information
of the index with the maximum value. Supported format list ["ND"] 

## Outputs

y: A multi-dimensional Tensor, specifying the maximum value of the
corresponding axis in the tensor.
Has the same type as "x". (If "keep_dims" is set to "false",
the output dimensions are reduced by "dimension" compared with that of "x".
Otherwise, the output has one fewer dimension than "x").Supported format list ["ND"]

## Attributes

keep_dims: A bool, specifying whether to keep dimensions for the output Tensor.
Optional and defaults to "false". 
noop_with_empty_axes: An optional bool. Defaults to "true" .
- If true, when axes = [], not reduce.
- If false, when axes = [], reduce all.
This attribute is valid only for Ascend950 AI Processors and later products.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32,uint8
- input1 axes: int32,int64
- output0 y: float16,float32,int32,uint8
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 axes: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Attention Constraints

- The value range of "axes" is [-dims, dims - 1]. "dims"
indicates the dimension length of "x".
- When converting ONNX to OM, if the axes of the ReduceMax operator is empty,
it is recommended to use the amax function with dim explicitly set to all axes
(e.g., dim=[0, 1, 2]) to prevent shape inference errors.

## Third-party framework compatibility

Compatible with TensorFlow operator Max.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
