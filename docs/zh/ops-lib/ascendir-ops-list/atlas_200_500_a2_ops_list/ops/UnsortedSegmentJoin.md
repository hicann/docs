# UnsortedSegmentJoin

```c
REG_OP(UnsortedSegmentJoin)
    .INPUT(input, TensorType({DT_STRING}))
    .INPUT(segment_ids, TensorType({DT_INT32,DT_INT64}))
    .INPUT(num_segments, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(output, TensorType({DT_STRING}))
    .ATTR(separator, String, "")
    .OP_END_FACTORY_REG(UnsortedSegmentJoin)
```

## Brief

A Tensor of type string. The input to be joined. 

## Inputs

include:
- input:A Tensor of type string. The text to be processed.
- segment_ids:A Tensor. Must be one of the following types: int32, int64.
A tensor whose shape is a prefix of data.shape. Negative segment ids are not supported.
- num_segments:A Tensor. Must be one of the following types: int32, int64. A scalar.

## Outputs

output:A Tensor of type string.

## Attributes

separator:An optional string. Defaults to "". The separator to use when joining.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: string
- input1 segment_ids: int32,int64
- input2 num_segments: int32,int64
- output0 output: string


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
