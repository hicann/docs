# EmbeddingHashmapFileSize

```c
REG_OP(EmbeddingHashmapFileSize)
    .INPUT(file_path, TensorType({DT_STRING}))
    .INPUT(table_ids, TensorType({DT_INT32}))
    .INPUT(table_names, TensorType({DT_STRING}))
    .INPUT(global_step, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(table_sizes, TensorType({DT_INT64}))
    .REQUIRED_ATTR(embedding_dims, ListInt)
    .OP_END_FACTORY_REG(EmbeddingHashmapFileSize)
```

## Brief

get import size of the embedding hashmap file. 

## Inputs

- file_path: A Scalar, dtype is string, indicates the path of import file.
- table_ids: A Tensor, dtype is int32, indicates the hash table id.
- table_names: A Tensor, dtype is string, indicates the hash table names.
- global_step: A Scalar, dtype is DT_INT32/DT_INT64. 0-D. indicates the save step.

## Outputs

- table_sizes: A Tensor, dtype is int64, indicates the size of hash map for each table.

## Attributes

- embedding_dims: List of Int, indicates the length of embedding for each table.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 file_path: string
- input1 table_ids: int32
- input2 table_names: string
- input3 global_step: int32,int64
- output0 table_sizes: int64


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
