# HcomReduceScatter

```c
REG_OP(HcomReduceScatter)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64}))
    .REQUIRED_ATTR(reduction, String)
    .ATTR(fusion, Int, 0)
    .ATTR(fusion_id, Int, -1)
    .REQUIRED_ATTR(group, String)
    .REQUIRED_ATTR(rank_size, Int)
    .OP_END_FACTORY_REG(HcomReduceScatter)
```

## Brief

Performs reduction across all input tensors, scattering in equal
blocks among ranks, each rank getting a chunk of data based on its rank
index.

## Inputs

x: A tensor. Must be one of the following types: int8, int16, int32, int64, float16,
float32.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- reduction: A required string identifying the reduction operation to
perform. The supported operation are: "sum", "max", "min", "prod".
- fusion: An optional integer identifying the fusion flag of the op.
0: no fusion; 2: fusion the ops by fusion id.
- fusion_id: An optional integer identifying the fusion id of the op.
The HcomReduceScatter ops with the same fusion id will be fused.
- group: A required string identifying the group name of ranks
participating in the op.
- rank_size: A required integer identifying the number of ranks
participating in the op.

## Attention Constraints

"group" is limited to 128 characters. Use "hccl_world_group"
as the name of a world group.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
