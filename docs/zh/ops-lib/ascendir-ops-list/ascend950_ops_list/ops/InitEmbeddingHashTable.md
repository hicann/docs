# InitEmbeddingHashTable

```c
REG_OP(InitEmbeddingHashTable)
    .INPUT(table_handle, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(sampled_values, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(bucket_size, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .ATTR(initializer_mode, String, "random")
    .ATTR(constant_value, Float, 0.0)
    .OP_END_FACTORY_REG(InitEmbeddingHashTable)
```

## Brief

Init EmbeddingHashTable.

## Inputs

Inputs include:
table_handle: A Tensor. Dtype support: int64
sampled_values: A Tensor. Dtype support: float32

## Attributes

- bucket_size: An required attribute indicates hashtable size.
- embedding_dim: An required attribute indicates hashtable value size.
- initializer_mode: An optional attribute indicates init hashtable mode.
- constant_value: An optional attribute indicates hashtable constant mode const value.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 table_handle: int64
- input1 sampled_values: float32

## Attention Constraints

Only support value's dtype is float32.


---

[Back to Operator Specifications (Ascend950)](../README.md)
