# HcomReduceScatterV

```c
REG_OP(HcomReduceScatterV)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT16, DT_INT8}))
    .INPUT(recv_count, TensorType({DT_INT64}))
    .INPUT(send_counts, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(send_displacements, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT16, DT_INT8}))
    .REQUIRED_ATTR(reduction, String)
    .REQUIRED_ATTR(group, String)
    .OP_END_FACTORY_REG(HcomReduceScatterV)
```

## Brief

Performs reduction across all input tensors, scattering in vary size
blocks among ranks, each rank getting a chunk of data based on its rank
index.

## Inputs

- x: A tensor. Must be one of the following types: int8, int16, int32, float16, float32.
- send_counts: int64 array, where entry i specifies the first dimension number of elements to send to rank i.
- send_displacesments: int64 array, optional, where entry i specifies the displacement from which to send data to rank i.
If not provided, it is assumed to be contiguous memory by default.
- recv_count: int64 array, only one entry which specifies the first dimension number of elements of the output data.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- reduction: A required string identifying the reduction operation to
perform. The supported operation are: "sum", "max", "min".
- group: A required string identifying the group name of ranks
participating in the op.

## Attention Constraints

- "group" is limited to 128 characters. Use "hccl_world_group"
as the name of a world group.
- Only the single-node system scenario of the Atlas A2 Training Series Product is supported.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
