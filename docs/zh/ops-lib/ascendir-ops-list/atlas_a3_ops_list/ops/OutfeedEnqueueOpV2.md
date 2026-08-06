# OutfeedEnqueueOpV2

```c
REG_OP(OutfeedEnqueueOpV2)
  .DYNAMIC_INPUT(x, TensorType({TensorType::BasicType(), DT_BOOL, DT_STRING}))
  .INPUT(tensor_name, TensorType({DT_STRING}))
  .ATTR(channel_name, String, "")
  .ATTR(slice_size, Int, 0)
  .ATTR(wait_time, Int, 0)
  .ATTR(slice_sync, Bool, false)
  .OP_END_FACTORY_REG(OutfeedEnqueueOpV2)
```

## Brief

Enqueue a Tensor on the computation outfeed. 

## Inputs

Inputs include:
x: A Tensor. Must be one of the following types: double, float32, float16, bfloat16, complex32, complex64, complex128,
int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint16, quint16, qint32, bool, string. It's a dynamic input. 
tensor_name: A Tensor. Must be string types. 

## Attributes

- channel_name: name of operator channel, defaults to "".
- slice_size: the size of one dataset. default 0, do not slice.
- wait_time: op phase 2 event wait timeout. default 0, use system default timeout.
- slice_sync: whether to add a synchronization dataset. default false, do not add.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input1 tensor_name: string

## Attention Constraints

The implementation for OutfeedEnqueueOpV2 on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow OutfeedEnqueueOpV2 operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
