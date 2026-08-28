# HcomAllToAllVC

```c
REG_OP(HcomAllToAllVC)
    .INPUT(send_data, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .INPUT(send_count_matrix, TensorType({DT_INT64})) // [ranksize, ranksize]
    .OUTPUT(recv_data, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(rank, Int)
    .REQUIRED_ATTR(group, String)
    .ATTR(fusion, Int, 0)
    .ATTR(fusion_id, Int, -1)
    .OP_END_FACTORY_REG(HcomAllToAllVC)
```

## Brief

All ranks send different amount of data to, and receive different
amount of data from, all ranks.

## Inputs

Two inputs, including:
- send_data: A tensor. the memory to send.
- send_count_matrix: A two dimensional matrix, where entry [i][j] specifies
the number of elements in the send_data that rank i to rank j.
- fusion: An optional integer identifying the fusion flag of the op.
0(default): no fusion; 2: fusion the ops by fusion id.
- fusion_id: An optional integer identifying the fusion id of the op.
The HcomAllToAllVC ops with the same fusion id will be fused.

## Outputs

recv_data: A Tensor  has same element type as send_data.

## Attributes

- rank: A required integer identifying the self rank.
- group: A string identifying the group name of ranks participating in
the op.


---

[Back to Operator Specifications (Ascend950)](../README.md)
