# TensorMapHasKey

```c
REG_OP(TensorMapHasKey)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(key, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(has_key, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(TensorMapHasKey)
```

## Brief

Returns whether the given key exists in the map. 

## Inputs

- input_handle: A scalar Tensor of type variant. The original map.
- key: The key to check. Supports int32, int64, string.

## Outputs

has_key: A scalar Tensor of type bool. Whether the key is already in the map or not. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 key: int32,int64,string
- output0 has_key: bool

## Third-party framework compatibility.

Compatible with tensorflow TensorMapHasKey operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
