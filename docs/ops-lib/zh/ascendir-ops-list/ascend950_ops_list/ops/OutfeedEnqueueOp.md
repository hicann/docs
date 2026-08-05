# OutfeedEnqueueOp

```c
REG_OP(OutfeedEnqueueOp)
  .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8,
      DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_UINT32,
      DT_UINT64, DT_BOOL, DT_DOUBLE, DT_STRING}))
  .ATTR(channel_name, String, "")
  .OP_END_FACTORY_REG(OutfeedEnqueueOp)
```

## Brief

Enqueue a Tensor on the computation outfeed. 

## Inputs

Inputs include:
x: A Tensor. Must be one of the following types: float16, float32,
int8, int16, uint16, uint8, int32, int64, uint32, uint64,
bool, double, string. It's a dynamic input. 

## Attributes

channel_name: name of operator channel, defaults to "". 

## Attention Constraints

The implementation for OutfeedEnqueueOp on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow OutfeedEnqueueOp operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
