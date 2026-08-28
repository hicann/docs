# HcomSend

```c
REG_OP(HcomSend)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(group, String)
    .REQUIRED_ATTR(sr_tag, Int)
    .REQUIRED_ATTR(dest_rank, Int)
    .OP_END_FACTORY_REG(HcomSend)
```

## Brief

Sends the input tensor to destination rank.

## Inputs

x: A tensor. Must be one of the following types: int8, int16, int32, float16,
float32.

## Outputs

None.

## Attributes

- sr_tag: A required integer identifying the send/recv message tag. The
message will be received by the HcomReceive op with the same "sr_tag".
- dest_rank: A required integer identifying the destination rank.
- group: A string identifying the group name of ranks participating in
the op.

## Attention Constraints

- "group" is limited to 128 characters. Use
"hccl_world_group" as the name of a world group.
- Operators HcomSend and HcomReceive have the same "sr_tag".
@see HcomReceive


---

[Back to Operator Specifications (Ascend950)](../README.md)
