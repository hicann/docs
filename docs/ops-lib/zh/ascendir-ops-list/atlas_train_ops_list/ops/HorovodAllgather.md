# HorovodAllgather

```c
REG_OP(HorovodAllgather)
    // GE not support float64 currently
    .INPUT(x, TensorType({DT_UINT8, DT_INT8, DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_UINT8, DT_INT8, DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_BOOL}))
    // add rank_size attr
    .REQUIRED_ATTR(rank_size, Int)
    .OP_END_FACTORY_REG(HorovodAllgather)
```

## Brief

Outputs a tensor gathering all input tensors.

## Inputs

x: A tensor. Must be one of the following types: uint8, int8, uint16, int16, int32,
int64, float16, bool.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- rank_size: A required integer identifying the number of ranks
participating in the op.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
