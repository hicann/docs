# ScatterList

```c
REG_OP(ScatterList)
    .DYNAMIC_INPUT(var, "T")
    .INPUT(indice, TensorType::IndexNumberType())
    .INPUT(updates, "T")
    .OPTIONAL_INPUT(mask, TensorType({DT_UINT8}))
    .DYNAMIC_OUTPUT(var, "T")
    .ATTR(reduce, String, "update")
    .ATTR(axis, Int, -2)
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8,
                             DT_UINT16, DT_UINT32, DT_UINT64}))
    .OP_END_FACTORY_REG(ScatterList)
```

## Brief

Applies sparse updates into a variable reference.

## Inputs

- var: The rewritten tensor list. Format is ND. Support 1D ~ 7D. Must be one of the following types:
float16, bfloat16, float32, int8, int16, int32, int64, uint8, uint16, uint32, uint64.
- indice: The index tensor. Format is ND. Support 1D ~ 2D, the first dimension should be equal to "updates", the
second dimension should be 2. Must be one of the following types: int32, int64. Index out of bounds is not supported.
- updates: The source tensor. Format is ND. Support 2D ~ 8D, the first dimension should be equal to the number of
tensors of "var", and the dimension of "axis" should not be greather than "var", other dimensions should be equal to
"var". Must have the same type of "var".
- mask: The mask tensor. Format is ND. Support 1D, the first dimension should be equal to "updates". Type should be
uint8.

## Outputs

var: A tensor list. Must have the same type, shape and format as input "var".

## Attributes

- reduce: An optional string. Defaults to "update".
- axis: An optional int. Defaults to -2.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32,int8,int16,int32,uint8,uint16,uint32
- input1 indice: int32,int64
- input2 updates: float16,float32,int8,int16,int32,uint8,uint16,uint32
- input3 mask: uint8
- output0 var: float16,float32,int8,int16,int32,uint8,uint16,uint32

## Third-party framework compatibility

Compatible with the Mindspore operator ScatterList.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
