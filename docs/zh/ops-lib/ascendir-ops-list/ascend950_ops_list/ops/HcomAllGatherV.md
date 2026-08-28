# HcomAllGatherV

```c
REG_OP(HcomAllGatherV)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_BFLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .INPUT(send_count, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_BFLOAT16, DT_INT64, DT_UINT64,
                           DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .INPUT(recv_counts, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(recv_displacements, TensorType({DT_INT64}))
    .REQUIRED_ATTR(group, String)
    .OP_END_FACTORY_REG(HcomAllGatherV)
```

## Brief

Outputs a tensor gathering all input tensors.

## Inputs

- x: A tensor. Must be one of the following types: int8, int16, int32, int64, float16, bfloat16,
float32, uint8, uint16, uint32, uint64, float64.
- send_count: A data. specifies current rank the the number of
elements to receive to send, only support int64.
- recv_counts: A list, where entry i specifies the first dimension of
elements to receive from rank i, only support int64.
- recv_displacements: A list, where entry i specifies the displacement
(offset from recv_data) to which data from rank i should be written, only support int64.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

group: A required string identifying the group name of ranks
participating in the op.

## Attention Constraints

- "group" is limited to 128 characters. Use "hccl_world_group"
as the name of a world group.
- Only the single-node system scenario of the Atlas A2 Training Series Product is supported.


---

[Back to Operator Specifications (Ascend950)](../README.md)
