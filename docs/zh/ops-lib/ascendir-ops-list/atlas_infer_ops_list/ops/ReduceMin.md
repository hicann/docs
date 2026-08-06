# ReduceMin

```c
REG_OP(ReduceMin)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, true)
    .OP_END_FACTORY_REG(ReduceMin)
```

## Brief

Computes the minimum of elements across dimensions of a tensor .

## Inputs

- x: A tensor. Must be the type of NumberType.
- axes: A tensor of type of IndexNumberType.(IndexNumberType
includes: int32, int64.) Specifies the dimensions to reduce.
Defaults to "None".

## Outputs

y: A tensor. Must be the type of NumberType.

## Attributes

keep_dims: An optional bool. If "True", reduced dimensions will be retained.
Defaults to "False".
noop_with_empty_axes: An optional bool. Defaults to "true" .
- If true, when axes = [], not reduce.
- If false, when axes = [], reduce all.
This attribute is valid only for Ascend950 AI Processors and later products.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32,int64,uint8
- input1 axes: int32,int64
- output0 y: float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 axes: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Attention Constraints

- If "axes = None", all dimensions will be reduced. "axes" must be in the
range [-rank(input_shape), rank(input_shape)).
- When converting ONNX to OM, if the axes of the ReduceMin operator is empty,
it is recommended to use the amin function with dim explicitly set to all axes
(e.g., dim=[0, 1, 2]) to prevent shape inference errors.

## Third-party framework compatibility

Compatible with the TensorFlow operator reduce_min.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
