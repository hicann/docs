# HorovodAllreduce

```c
REG_OP(HorovodAllreduce)
    .INPUT(x, TensorType({DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(reduce_op, Int)
    .OP_END_FACTORY_REG(HorovodAllreduce)
```

## Brief

Outputs a tensor containing the reduction across all input tensors
passed to op.

## Inputs

x: A tensor. Must be one of the following types: int32, int64, float16, float32

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes:

- reduce_op: A required int identifying the reduction operation to
perform.The supported operation are: "sum", "max", "min", "prod".


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
