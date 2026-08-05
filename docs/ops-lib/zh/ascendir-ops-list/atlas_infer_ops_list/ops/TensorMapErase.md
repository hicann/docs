# TensorMapErase

```c
REG_OP(TensorMapErase)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(key, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .OP_END_FACTORY_REG(TensorMapErase)
```

## Brief

Returns a tensor map with item from given key erased. 

## Inputs

- input_handle: A scalar Tensor of type variant. The original map.
- key: The key of the value to be erased. Supports int32, int64, string.

## Outputs

output_handle: A scalar Tensor of type variant. The map with value from given key removed. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 key: int32,int64,string
- output0 output_handle: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorMapErase operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
