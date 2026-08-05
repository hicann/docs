# UnsortedSegmentSum

```c
REG_OP(UnsortedSegmentSum)
    .INPUT(x, TensorType::NumberType())
    .INPUT(segment_ids, TensorType::IndexNumberType())
    .INPUT(num_segments, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(is_preprocessed, Bool, false)
    .ATTR(check_ids, Bool, false)
    .OP_END_FACTORY_REG(UnsortedSegmentSum)
```

## Brief

Computes the sum along segments of a tensor . 
Computes a tensor such that (output[i] = sum_{j...} x[j...] where
the sum is over tuples j... such that segment_ids[j...] == i.If the sum
is empty for a given segment ID i, output[i] = 0 
for example:x = [[0,1,2],[3,4,5],[6,7,8]] , segment_ids = [0,0,4] num_segments = 5 
output[0] = [3, 5, 7] 
output[1] = [0, 0, 0] 
output[2] = [0, 0, 0] 
output[3] = [0, 0, 0] 
output[4] = [6, 7, 8] 

## Inputs

Three inputs, including:
- x: A tensor of type float32,float16,int32,int64,uint32,uint64,bfloat16. Format is ND.
- segment_ids: The ID of the output location.
A tensor of type int32, int64, and the rank is less than or equal to x rank.
Whose shape is a prefix of "x.shape". Format is ND.
- num_segments: A tensor of type int32, int64, format is ND.
Indicates the output segment . 

## Outputs

y: Type and format is the same as x . 

## Attributes

- is_preprocessed: Deprecated attributes. Must to false.
- check_ids: Check whether the ID is verified. An optional bool. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 segment_ids: int32,int64
- input2 num_segments: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator UnsortedSegmentSum


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
