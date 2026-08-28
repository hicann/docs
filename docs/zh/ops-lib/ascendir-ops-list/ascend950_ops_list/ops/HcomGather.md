# HcomGather

```c
REG_OP(HcomGather)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64}))
    .REQUIRED_ATTR(root_rank, Int)
    .REQUIRED_ATTR(group, String)
    .REQUIRED_ATTR(rank_size, Int)
    .OP_END_FACTORY_REG(HcomGather)
```

## Brief

Calculate that aggregates input data

## Inputs

- x: A tensor of type float32, int32, int8, int16, float16, int64, uint64

## Outputs

- y: A tensor of type float32, int32, int8, int16, float16, int64, uint64.

## Attributes

- tag: A required integer identifying the hccl operator root_rank.
- group: A string identifying the group name of ranks participating in
the op.
- rank_size: A required integer identifying the rank size.


---

[Back to Operator Specifications (Ascend950)](../README.md)
