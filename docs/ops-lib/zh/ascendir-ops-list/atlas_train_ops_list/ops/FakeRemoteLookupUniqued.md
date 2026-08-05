# FakeRemoteLookupUniqued

```c
REG_OP(FakeRemoteLookupUniqued)
    .INPUT(table_id, TensorType({DT_INT32}))
    .INPUT(keys, TensorType({DT_INT64}))
    .INPUT(actual_keys_num, TensorType({DT_INT64}))
    .INPUT(unique_indices, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(key_count, TensorType({DT_INT64}))
    .OUTPUT(values, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(embedding_dim, ListInt)
    .REQUIRED_ATTR(value_total_len, ListInt)
    .ATTR(initializer_mode, ListString, {"random_uniform"})
    .ATTR(constant_value, ListFloat, {0})
    .ATTR(min, ListFloat, {-2})
    .ATTR(max, ListFloat, {2})
    .ATTR(mu, ListFloat, {0})
    .ATTR(sigma, ListFloat, {1})
    .ATTR(seed, ListInt, {0})
    .ATTR(seed2, ListInt, {0})
    .ATTR(filter_mode, ListString, {"no_filter"})
    .ATTR(filter_freq, ListInt, {0})
    .ATTR(default_key_or_value, ListInt, {0})
    .ATTR(default_key, ListInt, {0})
    .ATTR(default_value, ListFloat, {0})
    .ATTR(completion_key, ListInt, {0})
    .ATTR(completion_key_mask, ListInt, {1})
    .ATTR(optimizer_mode, ListString, {})
    .ATTR(optimizer_params, ListFloat, {})
    .OP_END_FACTORY_REG(FakeRemoteLookupUniqued)
```

## Brief

fake remote lookup host unique. 

## Inputs

- table_id: A Tensor, dtype is DT_INT32. 0-D. indicates the id of hashtable.
- keys: A Tensor, dtype is DT_INT64. 1-D. indicates the hashtable key.
- actual_keys_num: dtype is DT_INT64. 1-D. indicates the actual hashtable key to host.
- unique_indices: A Tensor, dtype is DT_INT32. indicates the unique indices.
- key_count: An optional input Tensor, dtype is DT_INT64. 1-D. indicates the count of each key.

## Outputs

- values: indicates the hashtable value.

## Attributes

- embedding_dim: Int list, indicates the dim of embedding var value in hashtable.
- value_total_len: Int list, indicates the dim of embedding var+m+v or var+accum values in hashtable.
- initializer_mode: An optional string list of "random_uniform", "truncated_normal" or "constant".
indicates the algo of init method. Defaults to "random_uniform".
- constant_value: An optional float List, used when initializer_mode is "constant". Defaults to "0".
- min: An optional float list, used when initializer_mode is "truncated_normal", the minimum value of the random number.
Defaults to "-2".
- max: An optional float list, used when initializer_mode is "truncated_normal", the maximum value of the random number.
Defaults to "2".
- mu: An optional float List, used when initializer_mode is "truncated_normal", The mean of the truncated_normal.
Defaults to "0".
- sigma: An optional float list, used when initializer_mode is "truncated_normal", The variance of the truncated_normal.
Defaults to "1".
- seed: An optional int list, used to create a random seed. Defaults to "0".
- seed2: An optional int list, used to create a random seed. Defaults to "0".
- filter_mode: An optional string list of "no_filter" or "counter". indicates the type of the hashmap, Defaults to "no_filter".
- filter_freq: An optional int list, used to set the threshold of the tal. Defaults to "0".
- default_key_or_value: An optional int list, indicates the default value get way.
- default_key: An optional int list, when default_key_or_value is true, use the default_key corresponding value as default value.
- default_value: An optional int list, when default_key_or_value is false, use the default_value as default value.
- completion_key: An optional int list, indicates the completion hashtable key.
- completion_key_mask: An optional int list, whether to perform no-update interception when key==completion_key.
- optimizer_mode: An optional string list of "adam" or "adamw" or "adagrad". indicates the type of the optimizer_mode,
Defaults to "".
- optimizer_params: An optional float list, when optimizer_mode is "adagrad", the initialize value of the optimizer.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
