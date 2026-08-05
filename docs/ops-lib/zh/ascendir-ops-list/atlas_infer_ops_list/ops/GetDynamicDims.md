# GetDynamicDims

```c
REG_OP(GetDynamicDims)
    .DYNAMIC_INPUT(input, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(dims, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(shape_info, ListInt)
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(GetDynamicDims)
```

## Brief

Get dynamic dims after GetNext. 

## Inputs

input: A nested structure of Tensor objects, from GetNext's output. Must be one of the following types: int32, int64. 

## Outputs

dims: GE unknow dims, a vector of int64. 

## Attributes

- shape_info: GE shape_info for each inputs, -1 means unknow dim.
- N: A int that indicates the inputs number.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 dims: int32,int64


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
