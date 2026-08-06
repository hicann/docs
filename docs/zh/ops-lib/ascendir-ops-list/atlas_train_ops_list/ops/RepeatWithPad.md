# RepeatWithPad

```c
REG_OP(RepeatWithPad)
    .INPUT(x, TensorType::BasicType())
    .INPUT(repeats, TensorType({DT_INT64, DT_INT32, DT_INT16, DT_INT8}))
    .INPUT(pad_value, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(capacity, Int)
    .ATTR(axis, Int, -1)
    .OP_END_FACTORY_REG(RepeatWithPad)
```

## Brief

Repeat elements of input with copies of data then pad or cut to certain capacity along a specified dimension

## Inputs

Three inputs:
- x: A tensor with ND format. Support float, float16, bfloat16, int8, int16, int32, int64,
uint8, uint16, uint32, uint64, bool.
- repeats: A tensor with 0-D / 1-D or a Scalar. Support int8, int16, int32, int64.
- pad_value: A tensor with ND format. Support float, float16, bfloat16, int8, int16, int32, int64,
uint8, uint16, uint32, uint64, bool.

## Outputs

y: A tensor, which is the same dtype as x.

## Attributes

- capacity: A required int, specifying the capacity to pad or cut to.
- axis: An optional int, specifying the axis to repeat. Defaults to -1.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
