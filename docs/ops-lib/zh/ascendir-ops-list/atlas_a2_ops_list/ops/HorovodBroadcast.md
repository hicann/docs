# HorovodBroadcast

```c
REG_OP(HorovodBroadcast)
    .INPUT(x, TensorType({DT_UINT8, DT_INT8, DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_UINT8, DT_INT8, DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_BOOL}))
    .REQUIRED_ATTR(root_rank, Int)
    .OP_END_FACTORY_REG(HorovodBroadcast)
```

## Brief

Broadcasts the input tensor in root rank to all ranks.

## Inputs

x: A list of dynamic input tensor. Must be one of the following types:
int8, int32, float16, float32.

## Outputs

y: A list of dynamic output tensor. Has the same type and length as "x".

## Attributes

- root_rank: A required integer identifying the root rank in the op
input of this rank will be broadcast to other ranks.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
