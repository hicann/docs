# UnsortedSegmentMinD

```c
REG_OP(UnsortedSegmentMinD)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(segment_ids, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .REQUIRED_ATTR(num_segments, Int)
    .OP_END_FACTORY_REG(UnsortedSegmentMinD)
```

## Brief

Computes the minimum along segments of a tensor. 
Computes a tensor such that (output[i] = min_{j...} x[j...]. 
the value of value must be  in [0, num_segments] 
for example:x = [[0,1,2],[3,4,5],[6,7,8]], segment_ids = [0,0,1] num_segments = 5 
output[0] = [0, 1, 2]
output[1] = [6, 7, 8]
output[2] = [2147483648, 2147483648, 2147483648]
output[3] = [2147483648, 2147483648, 2147483648]
output[4] = [2147483648, 2147483648, 2147483648]

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: float32, float16, int32.
Format is ND. Rank of shape must greater zero.
- segment_ids: A 1D Tensor of type int32, whose shape is a prefix of "x.shape".
Rank of shape is small than x rank, or equal of x shape rank

## Outputs

y: type and format is the same as x type.

## Attributes

num_segments: int, specifying the number of distinct segment IDs.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- input1 segment_ids: int32
- output0 y: float16,float32,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator UnsortedSegmentMin.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
