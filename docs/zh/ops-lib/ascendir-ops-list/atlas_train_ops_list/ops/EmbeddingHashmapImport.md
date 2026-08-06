# EmbeddingHashmapImport

```c
REG_OP(EmbeddingHashmapImport)
    .INPUT(file_path, TensorType({DT_STRING}))
    .INPUT(table_ids, TensorType({DT_INT32}))
    .INPUT(table_sizes, TensorType({DT_INT64}))
    .INPUT(table_names, TensorType({DT_STRING}))
    .INPUT(global_step, TensorType({DT_INT32, DT_INT64}))
    .DYNAMIC_OUTPUT(keys, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(counters, TensorType({DT_UINT64}))
    .DYNAMIC_OUTPUT(filter_flags, TensorType({DT_UINT8}))
    .DYNAMIC_OUTPUT(values, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(embedding_dims, ListInt)
    .OP_END_FACTORY_REG(EmbeddingHashmapImport)
```

## Brief

Import table data from file to embedding hashmap. 

## Inputs

- file_path: A Scalar, dtype is string, indicates the path folder of import file.
- table_ids: A Tensor, dtype is int32, indicates the hash table id.
- table_sizes: A Tensor, dtype is int64, indicates the size of hash map for each table.
- table_names: A Tensor, dtype is string, indicates the hash table names.
- global_step: A Scalar, dtype is DT_INT32/DT_INT64. 0-D. indicates the import save step.

## Outputs

- keys: Tensors which number is consistent with table's number, dtype is int64,
                indicates the original hash key for one table.
- counters: Tensors which number is consistent with table's number, dtype is uint64,
                indicates the counters of each hashmap.
- filter_flags: Tensors which number is consistent with table's number, dtype is uint8,
                indicates the filter flag of each hashmap.
- values: Tensors which number is consistent with table's number, dtype is float32.
               indicates the value of each hashmap. 

## Attributes

- embedding_dims: List of Int, indicates the length of embedding for each table.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 file_path: string
- input1 table_ids: int32
- input2 table_sizes: int64
- input3 table_names: string
- input4 global_step: int32,int64


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
