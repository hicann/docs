# HcomCollRemoteUpdate

```c
REG_OP(HcomCollRemoteUpdate)
    .INPUT(table_id, TensorType({DT_INT32}))
    .INPUT(keys, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_FP32}))
    .REQUIRED_ATTR(tag, Int)
    .ATTR(group, String, "hccl_world_group")
    .REQUIRED_ATTR(max_num, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .OP_END_FACTORY_REG(HcomCollRemoteUpdate)
```

## Brief

Workers send the keys and values to ps according to keys

## Inputs

- table_id: A tensor. Must be int32 type.
- keys: A tensor. Must be int64 type.
- values: A Tensor. Must be float32 type.

## Attributes

- tag: A required integer identifying the hccl operator tag.
- group: A string identifying the group name of ranks participating in
the op. Defaults to "hccl_world_group".
- max_num: A required integer identifying the keys max num.
- embedding_dim: Apply memory usage for output or infer shape.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
