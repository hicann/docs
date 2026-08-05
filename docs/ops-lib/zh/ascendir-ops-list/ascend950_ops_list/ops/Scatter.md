# Scatter

```c
REG_OP(Scatter)
    .INPUT(var, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8, DT_BF16}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8, DT_BF16}))
    .OUTPUT(var, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8, DT_BF16}))
    .REQUIRED_ATTR(reduce, String)
    .ATTR(axis, Int, -1)
    .OP_END_FACTORY_REG(Scatter)
```

## Brief

Applies sparse updates into a variable reference.

## Inputs

- var: The rewritten tensor. Format is ND. Support 2D ~ 8D, when axis is -1 the last dim of var should be 32B align.
Must be one of the following types:float16, float32, int32, int8, uint8, bfloat16.
- indices: The index tensor. Format is ND. Support 1D ~ 2D, when discrete, 1-dim of indices should be 2.
Must be one of the following types: int32, int64.
Index out of bounds is not supported.
- updates: The source tensor. Format is ND. The number of dimensions should be equal to "var", and the dimension of
"axis" should not be greather than "var", other dimensions should be equal to "var"
and 0-dim of updates should be equal 0-dim of indices. Must have the same type of "var".

## Outputs

var: An ND tensor. Must have the same type, format and shape as input "var".

## Attributes

- reduce: An required string. Can be "none" or "update".
- axis: An optional int. Defaults to -1, if axis < 0, it should be -1 or -2.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int32,uint8
- output0 var: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int8,int32,uint8

## Third-party framework compatibility

Compatible with the Mindspore operator Scatter.


---

[Back to Operator Specifications (Ascend950)](../README.md)
