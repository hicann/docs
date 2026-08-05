# TensorMapSize

```c
REG_OP(TensorMapSize)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .OUTPUT(size, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(TensorMapSize)
```

## Brief

return TensorMap Size. 

## Inputs

input_handle: A Tensor. Must be one of the following types: variant. 

## Outputs

size: A Tensor. Must be one of the following types: int32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- output0 size: int32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
