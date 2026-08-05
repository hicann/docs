# EmbeddingHashmapExport

```c
REG_OP(EmbeddingHashmapExport)
    .INPUT(file_path, TensorType({DT_STRING}))
    .INPUT(table_ids, TensorType({DT_INT32}))
    .INPUT(table_names, TensorType({DT_STRING}))
    .INPUT(global_step, TensorType({DT_INT32, DT_INT64}))
    .DYNAMIC_INPUT(keys, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(counters, TensorType({DT_UINT64}))
    .DYNAMIC_INPUT(filter_flags, TensorType({DT_UINT8}))
    .DYNAMIC_INPUT(values, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(EmbeddingHashmapExport)
```

## Brief

Export table data from the embedding table to file. 

## Inputs

- file_path: A Scalar, dtype is string, indicates the file path to export.
There are two types of paths: folder path with a file name prefix such as /home/path/ckpt
and folder path without a file name prefix such as /home/path/.
- table_ids: A Tensor, dtype is int32, indicates the hash table id.
- table_names: A Tensor, dtype is string, indicates the hash table names.
- global_step: A Scalar, dtype is DT_INT32/DT_INT64. 0-D. indicates the export save step.
- keys: Tensors which number is consistent with table's number, dtype is int64,
                indicates the original hash key for one table.
- counters: Tensors which number is consistent with table's number, dtype is uint64,
                indicates the counters of each hashmap.
- filter_flags: Tensors which number is consistent with table's number, dtype is uint8,
                indicates the filter flag of each hashmap.
- values: Tensors which number is consistent with table's number, dtype is float32.
               indicates the value of each hashmap. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 file_path: string
- input1 table_ids: int32
- input2 table_names: string
- input3 global_step: int32,int64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
