# UnsortedSegmentMax

```c
REG_OP(UnsortedSegmentMax)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(segment_ids, TensorType::IndexNumberType())
    .INPUT(num_segments, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(UnsortedSegmentMax)
```

## Brief

Computes the maximum along segments of a tensor.
Computes a tensor such that (output[i] = max_{j...} x[j...].
the value of segment_ids must be in [0, num_segments - 1].
for example:x = [[0,1,2],[3,4,5],[6,7,8]], segment_ids = [0,0,1] num_segments = 5
output[0] = [3, 4, 5]
output[1] = [6, 7, 8]
output[2] = [-2147483648, -2147483648, -2147483648]
output[3] = [-2147483648, -2147483648, -2147483648]
output[4] = [-2147483648, -2147483648, -2147483648]

## Inputs

Three inputs, including:
- x: A Tensor of type double, float32, float16, bfloat16, int8, int16, int32, int64, uint8, uint16, uint32, uint64,
format is ND.
- segment_ids: A Tensor of type int32, int64, whose shape is a prefix of "x", format is ND.
- num_segments: A 1D Tensor contains a single element of type int32, int64, format is ND.
Indicates the output segment.

## Outputs

y: Have the same type and format of "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32,int64,uint32,uint64
- input1 segment_ids: int32,int64
- input2 num_segments: int32,int64
- output0 y: bfloat16,float16,float32,int32,int64,uint32,uint64
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 segment_ids: int32,int64
- input2 num_segments: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator UnsortedSegmentMax.


---

[Back to Operator Specifications (Ascend950)](../README.md)
