# HcomCollRemoteLookup

```c
REG_OP(HcomCollRemoteLookup)
    .INPUT(table_id, TensorType({DT_INT32}))
    .INPUT(keys, TensorType({DT_INT64}))
    .OUTPUT(values, TensorType({DT_FP32}))
    .REQUIRED_ATTR(tag, Int)
    .ATTR(insert_option, Int, 0)
    .ATTR(group, String, "hccl_world_group")
    .REQUIRED_ATTR(max_num, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .ATTR(flags, Int, 0)
    .OP_END_FACTORY_REG(HcomCollRemoteLookup)
```

## Brief

Workers all find and get the corresponding value from the corresponding ps according to the keys

## Inputs

- table_id: A tensor. Must be int32 type.
- keys: A tensor. Must be int64 type.

## Outputs

- values: A Tensor. Must be float32 type.

## Attributes

- tag: A required integer identifying the hccl operator tag.
- insert_option: Indicates whether lookup supports new value. Defaults to "0".
- group: A string identifying the group name of ranks participating in
the op. Defaults to "hccl_world_group".
- max_num: A required integer identifying the keys max num.
- embedding_dim: A required integer identifying Apply memory usage for output or infer shape.
- flags: An integer identifying counter filter feature.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
