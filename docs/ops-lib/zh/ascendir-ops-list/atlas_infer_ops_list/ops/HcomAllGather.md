# HcomAllGather

```c
REG_OP(HcomAllGather)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_BFLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_BFLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(rank_size, Int)
    .REQUIRED_ATTR(group, String)
    .ATTR(fusion, Int, 0)
    .ATTR(fusion_id, Int, -1)
    .OP_END_FACTORY_REG(HcomAllGather)
```

## Brief

Outputs a tensor gathering all input tensors.

## Inputs

x: A tensor. Must be one of the following types: int8, int16, int32, int64, float16, bfloat16,
float32, uint8, uint16, uint32, float64.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- rank_size: A required integer identifying the number of ranks
participating in the op.
- group: A required string identifying the group name of ranks
participating in the op.
- fusion: An optional integer identifying the fusion flag of the op.
0: no fusion; 2: fusion the ops by fusion id.
- fusion_id: An optional integer identifying the fusion id of the op.
The HcomAllGather ops with the same fusion id will be fused.

## Attention Constraints

"group" is limited to 128 characters. Use "hccl_world_group"
as the name of a world group.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
