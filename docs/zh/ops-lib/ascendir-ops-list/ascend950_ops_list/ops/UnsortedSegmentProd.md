# UnsortedSegmentProd

```c
REG_OP(UnsortedSegmentProd)
    .INPUT(x, TensorType::NumberType())
    .INPUT(segment_ids, TensorType::IndexNumberType())
    .INPUT(num_segments, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .OP_END_FACTORY_REG(UnsortedSegmentProd)
```

## Brief

Computes the product along segments of a tensor.
Computes a tensor such that output[i] = prod_{j...} data[j...]
where the product is over tuples j... such that segment_ids[j...] == i.
If the product for a given segment ID i is empty, output[i] = 1.
Negative segment IDs are ignored.

## Inputs

Three inputs, including:
- x: A Tensor of type float16, float32, bfloat16, int32, int64, uint32, uint64, format is ND.
- segment_ids: A Tensor of type int32, int64, whose shape is a prefix of "x", format is ND.
- num_segments: A 1D Tensor contains a single element of type int32, int64, format is ND.

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
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 segment_ids: int32,int64
- input2 num_segments: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator UnsortedSegmentProd.


---

[Back to Operator Specifications (Ascend950)](../README.md)
