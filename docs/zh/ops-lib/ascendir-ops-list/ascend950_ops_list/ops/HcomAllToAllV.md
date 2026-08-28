# HcomAllToAllV

```c
REG_OP(HcomAllToAllV)
    .INPUT(send_data, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .INPUT(send_counts, TensorType({DT_INT64}))
    .INPUT(send_displacements, TensorType({DT_INT64}))
    .INPUT(recv_counts, TensorType({DT_INT64}))
    .INPUT(recv_displacements, TensorType({DT_INT64}))
    .OUTPUT(recv_data, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(group, String)
    .OP_END_FACTORY_REG(HcomAllToAllV)
```

## Brief

All ranks send different amount of data to, and receive different
amount of data from, all ranks.

## Inputs

Five inputs, including:
- send_data: A tensor. the memory to send.
- send_counts: A list, where entry i specifies the number of elements in
send_data to send to rank i.
- send_displacements: A list, where entry i specifies the displacement
(offset from sendbuf) from which to send data to rank i.
- recv_counts: A list, where entry i specifies the number of
elements to receive from rank i.
- recv_displacements: A list, , where entry i specifies the displacement
(offset from recv_data) to which data from rank i should be written.

## Outputs

recv_data: A Tensor  has same element type as send_data.

## Attributes

- group: A string identifying the group name of ranks participating in
the op.

## Attention all ranks participating in the op should be full-mesh networking

using the RDMA.


---

[Back to Operator Specifications (Ascend950)](../README.md)
