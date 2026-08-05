# EmbeddingHashTableLookupOrInsert

```c
REG_OP(EmbeddingHashTableLookupOrInsert)
.INPUT(table_handle, TensorType({DT_INT64}))
.INPUT(keys, TensorType({DT_INT64}))
.OUTPUT(values, TensorType({DT_FLOAT32}))
.REQUIRED_ATTR(bucket_size, Int)
.REQUIRED_ATTR(embedding_dim, Int)
.ATTR(filter_mode, String, "no_filter")
.ATTR(filter_freq, Int, 0)
.ATTR(default_key_or_value, Bool, false)
.ATTR(default_key, Int, 0)
.ATTR(default_value, Float, 0)
.ATTR(filter_key_flag, Bool, false)
.ATTR(filter_key, Int, -1)
.OP_END_FACTORY_REG(EmbeddingHashTableLookupOrInsert)
```

## Brief

insert keys in NPU hashtable and return coresponding value.

## Inputs

Inputs include:
- table_handle: A tensor. Must be int64. Contains addr of table's infos. shape of [5].
- keys: A tensor. Must be int64. Keys to be insert.

## Outputs

values: A tensor. Must be float32. N-D with shape [N, embedding_dim].

## Attributes

- bucket_size: Required, int, table capacity.
- embedding_dim: Required, int, value dims.
- filter_mode: Optional, string, set to "no_filter" or "counter", set "counter" to enable the counter-based filter mode, set "no_filter" to disable the filter function. default is "no_filter".
- filter_freq: Optional, int, filter threshold. default is 0.
- default_key_or_value: Optional, bool, set true will return the value of default_key, set false will return default_value. default is false.
- default_key: Optional, int, default key set by customer,  default is 0.
- default_value: Optional, float, default value set by customer. default is 0.
- filter_key_flag: Optional, bool, set true to enable filter_key, set false to disable the function of filter key. default is false.
- filter_key: Optional, int, filter input key and return default_value when flag is true. default is -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 table_handle: int64
- input1 keys: int64
- output0 values: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
