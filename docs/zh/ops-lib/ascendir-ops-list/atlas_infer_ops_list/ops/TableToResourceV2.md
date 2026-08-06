# TableToResourceV2

```c
REG_OP(TableToResourceV2)
    .INPUT(table_id, TensorType({DT_INT32}))
    .OUTPUT(table_handle, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(TableToResourceV2)
```

## Brief

convert embedding hashmap table id to handle. 

## Inputs

- table_id: A scalar, dtype is int32, indicates the hash table id.

## Outputs

- table_handle: A scalar, dtype is int64, indicates the hashmap info address.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 table_id: int32
- output0 table_handle: int64


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
