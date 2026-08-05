# SegmentSum

```c
REG_OP(SegmentSum)
    .INPUT(x, TensorType::NumberType())
    .INPUT(segment_ids, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .OP_END_FACTORY_REG(SegmentSum)
```

## Brief

Computes the sum along segments of a tensor.

## Inputs

Two inputs, including:
- x: A Tensor of type NumberType. Support 1D ~ 8D.
- segment_ids: A 1D Tensor of type IndexNumberType, whose shape is same
with "x.shape[0]".

## Outputs

y: A Tensor of type NumberType. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,int32
- input1 segment_ids: int32
- output0 y: float16,int32

## Attention Constraints

- segment_ids.dimNum = 1, and segment_ids.shape[0] = x.shape[0].
- segment_ids should sorted in ascending order, and segment_ids.value >= 0.
- y.type must be same with x.type.
- y.dimNum = x.dimNum, and y.shape = [max(segment_ids) + 1, x.shape[1:]]

## Third-party framework compatibility

Compatible with the TensorFlow operator SegmentSum.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
