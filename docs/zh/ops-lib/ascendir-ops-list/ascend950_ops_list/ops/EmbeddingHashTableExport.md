# EmbeddingHashTableExport

```c
REG_OP(EmbeddingHashTableExport)
    .INPUT(table_handles, TensorType({DT_INT64}))
    .INPUT(table_sizes, TensorType({DT_INT64}))
    .INPUT(embedding_dims, TensorType({DT_INT64}))
    .INPUT(bucket_sizes, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(keys, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(counters, TensorType({DT_UINT64}))
    .DYNAMIC_OUTPUT(filter_flags, TensorType({DT_UINT8}))
    .DYNAMIC_OUTPUT(values, TensorType({DT_FLOAT}))
    .ATTR(export_mode, String, "all")
    .ATTR(filtered_export_flag, Bool, false)
    .OP_END_FACTORY_REG(EmbeddingHashTableExport)
```

## Brief

embedding hashtable export. 

## Inputs

- table_handles: A Tensor, dtype is DT_INT64, 1-D. indicates the table handle address.
- table_sizes: A Tensor, dtype is DT_INT64,  1-D. indicates the size of hash map for each table.
- embedding_dims: A Tensor, dtype is DT_INT64,  1-D. indicates the dim of embedding value in hashtable.
- bucket_sizes: A Tensor, dtype is DT_INT64. 1-D. indicates the hash bucket size.

## Outputs

- keys: A list of Tensor objects, dtype is DT_INT64. indicates the hashtable keys. It's a dynamic output.
- counters: A list of Tensor objects, dtype is DT_UINT64. indicates the hashtable counter. It's a dynamic output.
- filter_flags: A list of Tensor objects, dtype is DT_UINT8. indicates the hashtable filter flag. It's a dynamic
    output.
- values: A list of Tensor objects, dtype is DT_FLOAT. indicates the hashtable value. It's a dynamic output.

## Attributes

- export_mode: An optional String. Represents export mode, can be either "all" or "new". Defaults to "all".
- filtered_export_flag: An optional Bool. Represents filter export flag on counter filter scenario.
Defaults to false. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 table_handles: int64
- input1 table_sizes: int64
- input2 embedding_dims: int64
- input3 bucket_sizes: int64
- output0 keys: int64
- output1 counters: uint64
- output2 filter_flags: uint8
- output3 values: float32

## Attention Constraints

- table_handles, table_sizes, embedding_dims and bucket_sizes have same shape len.
- the number of tensors in each dynamic output tensor list (keys/counters/filter_flags/values) shall be equal to
the shape len of table_handles. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
