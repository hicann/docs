# HcomBroadcast

```c
REG_OP(HcomBroadcast)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(root_rank, Int)
    .REQUIRED_ATTR(group, String)
    .ATTR(fusion, Int, 0)
    .ATTR(fusion_id, Int, -1)
    .OP_END_FACTORY_REG(HcomBroadcast)
```

## Brief

Broadcasts the input tensor in root rank to all ranks.

## Inputs

x: A list of dynamic input tensor. Must be one of the following types:
int8, int16, int32, float16, float32. It's a dynamic input.

## Outputs

y: A list of dynamic output tensor. Has the same type and length as "x".
It's a dynamic output.

## Attributes

- root_rank: A required integer identifying the root rank in the op
input of this rank will be broadcast to other ranks.
- fusion: A required integer identifying if the op need to fusion,
0: no fusion; 2(default): fusion the ops by fusion id.
- fusion_id: A required integer identifying the fusion id if para fusion
is set.
- group: A required string identifying the group name of ranks
participating in the op.

## Attention Constraints

"group" is limited to 128 characters. Use "hccl_world_group"
as the name of a world group.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
