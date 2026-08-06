# UnsortedSegmentSumD

```c
REG_OP(UnsortedSegmentSumD)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(segment_ids, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .REQUIRED_ATTR(num_segments, Int)
    .OP_END_FACTORY_REG(UnsortedSegmentSumD)
```

## Brief

Computes the sum along segments of a tensor. 
Computes a tensor such that (output[i] = sum_{j...} x[j...] where 
the sum is over tuples j... such that segment_ids[j...] == i.If the sum 
is empty for a given segment ID i, output[i] = 0 
for example:x = [[0,1,2],[3,4,5],[6,7,8]], segment_ids = [0,0,4] num_segments = 5 
output[0] = [3, 5, 7]
output[1] = [0, 0, 0]
output[2] = [0, 0, 0]
output[3] = [0, 0, 0]
output[4] = [0, 0, 0]

## Inputs

Two inputs, including:
- x: A Tensor of type float32, float16, int32, format is ND, Support 1D ~ 8D.
- segment_ids: The ID of the output location.
A Tensor of type int32. whose shape is a prefix, format is ND,
ids value is small than x shape rank, or equal, whose shape is a prefix of "x.shape".

## Outputs

y: type and format is the same as x type.

## Attributes

- num_segments: int. Indicates the output segment.

## Third-party framework compatibility

Compatible with the TensorFlow operator UnsortedSegmentSum.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
