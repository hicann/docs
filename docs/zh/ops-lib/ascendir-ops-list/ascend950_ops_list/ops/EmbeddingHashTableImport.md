# EmbeddingHashTableImport

```c
REG_OP(EmbeddingHashTableImport)
.INPUT(table_handles, TensorType({DT_INT64}))
.INPUT(embedding_dims, TensorType({DT_INT64}))
.INPUT(bucket_sizes, TensorType({DT_INT64}))
.DYNAMIC_INPUT(keys, TensorType({DT_INT64}))
.DYNAMIC_INPUT(counters, TensorType({DT_UINT64}))
.DYNAMIC_INPUT(filter_flags, TensorType({DT_UINT8}))
.DYNAMIC_INPUT(values, TensorType({DT_FLOAT}))
.OP_END_FACTORY_REG(EmbeddingHashTableImport)
```

## Brief

embedding hashtable data import. 

## Inputs

- table_handles: A Tensor, dtype is DT_INT64. 1-D. Indicates addr of hashtable.
- embedding_dims: A Tensor, dtype is DT_INT64. 1-D. Indicates the length of values.
- bucket_sizes: A Tensor, dtype is DT_INT64. 1-D. Indicates the hash bucket size.
- keys: A list of Tensor, dtype is DT_INT64, dynamic input. Indicates the hashtable keys number.
- counters: A list of Tensor, dtype is DT_UINT64, dynamic input. Indicates the hashtable counters.
- filter_flags: A list of Tensor, dtype is DT_UINT8, dynamic input. Indicates filter_flags.
- values: A list of Tensor, dtype is DT_FLOAT32, dynamic input. Indicates the import values .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 table_handles: int64
- input1 embedding_dims: int64
- input2 bucket_sizes: int64
- input3 keys: int64
- input4 counters: uint64
- input5 filter_flags: uint8
- input6 values: float32

## Attention Constraints

- table_handles, embedding_dims and bucket_sizes have same shape len.
- actual kernel compute filter_flags be 64 bit.
- single struct contains keys、counters、filter_flags and values, should be algin to 8 bytes.


---

[Back to Operator Specifications (Ascend950)](../README.md)
