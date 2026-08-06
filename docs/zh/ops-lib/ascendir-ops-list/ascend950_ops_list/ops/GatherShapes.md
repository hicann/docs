# GatherShapes

```c
REG_OP(GatherShapes)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .OUTPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(axes, ListListInt)
    .ATTR(dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(GatherShapes)
```

## Brief

Gather selected dims of input which returns the shape of tensor shape after gathershapes.

## Inputs

x: A list of input tensors. All data types are supported. It's a dynamic input. 

## Outputs

shape: The shape of tensor shape after gathershapes. Must be one of the following types: int32、int64. 

## Attributes

- axes: An 2-D list of int32 or int64 required. Select some dims of input.
- dtype: An optional int32, which indicates the data type of output. Defaults to DT_INT32.


---

[Back to Operator Specifications (Ascend950)](../README.md)
