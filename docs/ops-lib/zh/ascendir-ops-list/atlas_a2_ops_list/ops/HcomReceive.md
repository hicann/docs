# HcomReceive

```c
REG_OP(HcomReceive)
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(group, String)
    .REQUIRED_ATTR(sr_tag, Int)
    .REQUIRED_ATTR(src_rank, Int)
    .REQUIRED_ATTR(shape, ListInt)
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(HcomReceive)
```

## Brief

Receives the tensor from source rank.

## Inputs

None.

## Outputs

y: A tensor with type identified in "dtype".

## Attributes

- sr_tag: A required integer identifying the send/recv message tag. The
message will be send by the HcomSend op with the same "sr_tag".
- src_rank: A required integer identifying the source rank.
- group: A required string identifying the group name of ranks
participating in the op.
- shape: A required list identifying the shape of the tensor to be
received.
- dtype: A required integer identifying the type of the tensor to be
received. The supported types are: int8, int16, int32, float16, float32.

## Attention Constraints

- "group" is limited to 128 characters. Use
"hccl_world_group" as the name of a world group.
- Operators HcomSend and HcomReceive have the same "sr_tag".
- "shape" should be same as the input tensor of HcomSend.
- "dtype" should be same as the input tensor of HcomSend.
@see HcomSend


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
