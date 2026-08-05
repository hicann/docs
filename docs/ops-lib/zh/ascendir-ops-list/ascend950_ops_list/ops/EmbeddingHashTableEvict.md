# EmbeddingHashTableEvict

```c
REG_OP(EmbeddingHashTableEvict)
    .INPUT(table_handle, TensorType({DT_INT64}))
    .INPUT(keys, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(sampled_values, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(table_cap, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .ATTR(init_mode, String, "constant")
    .ATTR(const_val, Float, 0.0)
    .OP_END_FACTORY_REG(EmbeddingHashTableEvict)
```

## Brief

Evict keys and reinitialize embedding values in NPU hashtable.

## Inputs

- table_handle: A 1-D tensor of DT_INT64, which contains tables' starting addrs.
- keys: A 1-D tensor of DT_INT64, which represents keys to be evicted.
- sampled_values: A 1-D tensor of DT_FLOAT, used for reinitializing embeddings of evicted keys.

## Attributes

- table_cap: A required int attr, which indicates the capacity of table.
- embedding_dim: A required int attr, which indicates dimension of embedding value.
- init_mode: An optional string attr. which indicates reinitializing modes. Mode "random"
or "constant" are available, defaults to "constant".
- const_val: An optional float attr, which indicates the constant value in initialization.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 table_handle: int64
- input1 keys: int64
- input2 sampled_values: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
