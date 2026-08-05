# HcomRemoteLookup

```c
REG_OP(HcomRemoteLookup)
    .INPUT(keys, TensorType({DT_INT64}))
    .INPUT(table_id, Int)
    .OUTPUT(values, TensorType({DT_FP32}))
    .REQUIRED_ATTR(tag, Int)
    .ATTR(insert_option, Int, 0)
    .REQUIRED_ATTR(max_num, Int)
    .REQUIRED_ATTR(embedding_dim, Int)
    .OP_END_FACTORY_REG(HcomRemoteLookup)
```

## Brief

Find and get the corresponding value from the corresponding ps according to the keys

## Inputs

- keys: A tensor. Must be int64 type.
- table_id: A tensor. Must be int32 type.

## Outputs

- values: A Tensor. Must be float32 type.

## Attributes

- tag: A required integer identifying the hccl operator tag.
- insert_option: Indicates whether lookup supports new value. Defaults to "0".
- max_num: A required integer identifying the keys max num.
- embedding_dim: Apply memory usage for output or infer shape.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
