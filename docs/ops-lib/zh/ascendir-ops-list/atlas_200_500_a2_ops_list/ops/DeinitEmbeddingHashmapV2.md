# DeinitEmbeddingHashmapV2

```c
REG_OP(DeinitEmbeddingHashmapV2)
    .INPUT(table_id, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(DeinitEmbeddingHashmapV2)
```

## Brief

uninit embedding hash map table. 

## Inputs

- table_id: A scalar, dtype is int32, indicates the hash table id.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 table_id: int32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
