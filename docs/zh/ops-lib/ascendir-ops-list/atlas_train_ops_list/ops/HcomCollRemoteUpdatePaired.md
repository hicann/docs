# HcomCollRemoteUpdatePaired

```c
REG_OP(HcomCollRemoteUpdatePaired)
    .INPUT(table_id, TensorType({DT_INT32}))
    .INPUT(keys, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_FP32}))
    .INPUT(indices, TesnorType({DT_INT64}))
    .INPUT(num_uniqued, TesnorType({DT_INT64}))
    .INPUT(ps_segments, TesnorType({DT_INT64}))
    .INPUT(ps_segments_num, TesnorType({DT_INT64}))
    .OPTIONAL_INPUT(global_step, TesnorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(tag, Int)
    .ATTR(group, String, "hccl_world_group")
    .ATTR(padding_key, Int, 0)
    .ATTR(flags, Int, 0)
    .REQUIRED_ATTR(max_num, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .OP_END_FACTORY_REG(HcomCollRemoteUpdatePaired)
```

## Brief

Workers send the keys and values to ps according to keys. Used with HcomCollRemoteLookupPaired.

## Inputs

- table_id: A tensor. Must be int32 type.
- keys: A tensor. Must be int64 type.
- values: A Tensor. Must be float32 type.
- indices: A Tensor. Recovery matrix. Must be int64 type.
- num_uniqued: A Tensor. Number of Recovery matrix. Must be int64 type.
- ps_segments: A Tensor. Offset and size of buffer for pss. Must be int64 type.
- ps_segments_num: A Tensor. Number of ps_segments. Must be int64 type.

## Attributes

- tag: A required integer identifying the hccl operator tag.
- group: A string identifying the group name of ranks participating in
the op. Defaults to "hccl_world_group".
- max_num: A required integer identifying the keys max num.
- embedding_dim: Apply memory usage for output or infer shape.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
