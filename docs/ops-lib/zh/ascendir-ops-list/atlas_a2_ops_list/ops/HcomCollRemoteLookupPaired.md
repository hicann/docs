# HcomCollRemoteLookupPaired

```c
REG_OP(HcomCollRemoteLookupPaired)
    .INPUT(table_id, TensorType({DT_INT32}))
    .INPUT(keys, TensorType({DT_INT64}))
    .OUTPUT(values, TensorType({DT_FP32}))
    .OUTPUT(indices, TensorType({DT_INT64}))
    .OUTPUT(num_uniqued, TensorType({DT_INT64}))
    .OUTPUT(ps_segments, TesnorType({DT_INT64}))
    .OUTPUT(ps_segments_num, TesnorType({DT_INT64}))
    .REQUIRED_ATTR(tag, Int)
    .ATTR(insert_option, Int, 0)
    .ATTR(group, String, "hccl_world_group")
    .REQUIRED_ATTR(max_num, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .ATTR(flags, Int, 0)
    .OP_END_FACTORY_REG(HcomCollRemoteLookupPaired)
```

## Brief

Workers all find and get the corresponding value from the corresponding ps according to the keys. Used with
HcomCollRemoteUpdatePaired.

## Inputs

- table_id: A tensor. Must be int32 type.
- keys: A tensor. Must be int64 type.

## Outputs

- values: A Tensor. Must be float32 type.
- indices: A Tensor. Recovery matrix. Must be int64 type.
- num_uniqued: A Tensor. Number of Recovery matrix. Must be int64 type.
- ps_segments: A Tensor. Offset and size of buffer for pss. Must be int64 type.
- ps_segments_num: A Tensor. Number of ps_segments. Must be int64 type.

## Attributes

- tag: A required integer identifying the hccl operator tag.
- insert_option: Indicates whether lookup supports new value. Defaults to "0".
- group: A string identifying the group name of ranks participating in
the op. Defaults to "hccl_world_group".
- max_num: A required integer identifying the keys max num.
- embedding_dim: A required integer identifying Apply memory usage for output or infer shape.
- flags: An integer identifying counter filter feature.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
