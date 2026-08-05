# IndexByTensor

```c
REG_OP(IndexByTensor)
    .INPUT(x, TensorType({TensorType::BasicType(), DT_BOOL}))
    .DYNAMIC_INPUT(indices, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({TensorType::BasicType(), DT_BOOL}))
    .ATTR(indices_mask, ListInt, {})
    .OP_END_FACTORY_REG(IndexByTensor)
```

## Brief

According to the indices and indices_mask, return the value.

## Inputs

Four inputs, including:
- x: A ND tensor. Must be one of the following types:
    float, float16, int64, int32, bool, uint8, int8.
- indices: Dynamic input. A ND tensor of int64. return the value according to the indices.

## Outputs

- y: The indexed output tensor. Has the same type and format as input "x".

## Attributes

- indices_mask: A list int. Indicates which dimensions of input needs to be indexed.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int32,int64,uint8
- input1 indices: int64
- output0 y: bool,float16,float32,int8,int32,int64,uint8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
