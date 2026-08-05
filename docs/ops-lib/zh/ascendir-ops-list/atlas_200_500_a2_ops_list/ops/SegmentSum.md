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

## Attention Constraints

- segment_ids.dimNum = 1, and segment_ids.shape[0] = x.shape[0].
- segment_ids should sorted in ascending order, and segment_ids.value >= 0.
- y.type must be same with x.type.
- y.dimNum = x.dimNum, and y.shape = [max(segment_ids) + 1, x.shape[1:]]

## Third-party framework compatibility

Compatible with the TensorFlow operator SegmentSum.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
