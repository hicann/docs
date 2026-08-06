# TensorMapStackKeys

```c
REG_OP(TensorMapStackKeys)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .OUTPUT(keys, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .REQUIRED_ATTR(key_dtype, Type)
    .OP_END_FACTORY_REG(TensorMapStackKeys)
```

## Brief

Return TensorMapStackKeys. 

## Inputs

input_handle: A Tensor. Must be one of the following types: variant. 

## Outputs

keys: A Tensor. Must be one of the following types: int32, int64, string. 

## Attributes

key_dtype: An required param. It is the dtype of the key.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- output0 keys: int32,int64,string


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
