# InitEmbeddingHashmapV2

```c
REG_OP(InitEmbeddingHashmapV2)
    .INPUT(table_id, TensorType({DT_INT32}))
    .OUTPUT(table_handle, TensorType({DT_INT64}))
    .REQUIRED_ATTR(bucket_size, Int)
    .REQUIRED_ATTR(load_factor, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(InitEmbeddingHashmapV2)
```

## Brief

init embedding hash map table. 

## Inputs

- table_id: A scalar, dtype is int32, indicates the hash table id.

## Outputs

- table_handle: A scalar, dtype is int64, indicates the hashmap info address.

## Attributes

- bucket_size: A scalar, dtype is int64, indicates the hash bucket size.
- load_factor: A scalar, dtype is int64, indicates the hash load factor.
- embedding_dim: A scalar, dtype is int64, indicates the dim of embedding value in hash table.
- dtype: An optional attribute that indicates the type of value in hash table. Must be one of the following types:float32,double,int32,int64. Defaults to float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 table_id: int32
- output0 table_handle: int64


---

[Back to Operator Specifications (Ascend950)](../README.md)
