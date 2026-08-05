# FeedsRepeat

```c
REG_OP(FeedsRepeat)
    .INPUT(feeds, TensorType::BasicType())
    .INPUT(feeds_repeat_times, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(output_feeds_size, Int)
    .OP_END_FACTORY_REG(FeedsRepeat)
```

## Brief

Repeat every row of input 'feeds' different times with padding in the end.

## Inputs

Two inputs:
- feeds: A Tensor with ND format. Only support float, float16, bfloat16 for now. Other types include int8, int16,
int32, int64, uint8, uint16, uint32, uint64, bool will be supported later.
- feeds_repeat_times: A Tensor with ND format. Support int32, int64. Describe repeat times for every row of input
'feeds'.

## Outputs

y: A Tensor, which is the same dtype as feeds. Dim0 is output_feeds_size, other dims are same as feeds.

## Attributes

output_feeds_size: An required int, specifying the dim0 of y, describing padding space.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 feeds: bfloat16,float16,float32
- input1 feeds_repeat_times: int32,int64
- output0 y: bfloat16,float16,float32

## Attention Constraints

- The length of feeds_repeat_times must be same as feeds' dim0 size.
- The byte of feeds_repeat_times cannot reach about 64KB.


---

[Back to Operator Specifications (Ascend950)](../README.md)
