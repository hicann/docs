# ReduceProd

```c
REG_OP(ReduceProd)
    .INPUT(x,TensorType::NumberType())
    .INPUT(axes, TensorType::IndexNumberType())
    .OUTPUT(y,TensorType::NumberType())
    .ATTR(keep_dims, Bool, false)
    .ATTR(noop_with_empty_axes, Bool, true)
    .OP_END_FACTORY_REG(ReduceProd)
```

## Brief

Reduce a tensor on a certain axis based on product.

## Inputs

Two inputs, including:
- x: A Tensor. Must be the type of NumberType.(NumberType
includes: complex128, complex64, double, float32, float16, int16,
int32, int64,int8, qint32, qint8, quint8, uint16, uint32, uint64,
uint8, bfloat16, complex32).Supported format list ["ND"].
- axes: A Tensor. Must be the type of IndexNumberType(
includes: int32, int64). The dimensions to reduce.Supported format list ["ND"]. 

## Outputs

y: A Tensor. Has the same type and format as input "x" . 

## Attributes

keep_dims: A bool. If true, retains reduced dimensions with length 1.
Optional and defaults to "False" . 
noop_with_empty_axes: An optional bool. Defaults to "true" .
- If true, when axes = [], not reduce.
- If false, when axes = [], reduce all.
This attribute is valid only for Ascend950 AI Processors and later products.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int32,int64,uint8
- input1 axes: int32,int64
- output0 y: bfloat16,float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 axes: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ReduceProd.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
