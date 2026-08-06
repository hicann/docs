# EmbeddingHashmapSize

```c
REG_OP(EmbeddingHashmapSize)
    .INPUT(table_ids, TensorType({DT_INT32}))
    .OUTPUT(table_sizes, TensorType({DT_INT64}))
    .ATTR(filter_export_flag, Bool, false)
    .ATTR(export_mode, String, "all")
    .OP_END_FACTORY_REG(EmbeddingHashmapSize)
```

## Brief

get export size of the embedding hashmap. 

## Inputs

- table_ids: A Tensor, dtype is int32, indicates the hash table id.

## Outputs

- table_sizes: A Tensor, dtype is int64, indicates the size of hash map for each table.

## Attributes

- filter_export_flag: An optional bool that represents filter export flag on counter filter scenario. Defaults to "false".
- export_mode: An optional string that is export mode. The value of export mode has two values:
    "all" and "new". Defaults to "all". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 table_ids: int32
- output0 table_sizes: int64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
