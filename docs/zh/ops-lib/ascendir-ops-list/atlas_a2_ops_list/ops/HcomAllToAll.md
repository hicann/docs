# HcomAllToAll

```c
REG_OP(HcomAllToAll)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64, DT_UINT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_FLOAT64}))
    .REQUIRED_ATTR(group, String)
    .OP_END_FACTORY_REG(HcomAllToAll)
```

## Brief

All ranks send the same amount of data to each other, and receive the same amount of data from each other.

## Inputs

- x: A tensor. Must be one of the following types: float32, int32, int8, int16, float16,
int64, uint64, uint8, uint16, uint32, float64.

## Outputs

- y: A Tensor. Has the same type as "x".

## Attributes

- group: A string identifying the group name of ranks participating in
the op.

## Attention all ranks participating in the op should be full-mesh networking

using the RDMA.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
