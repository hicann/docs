# SegmentMax

```c
REG_OP(SegmentMax)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(segment_ids, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(SegmentMax)
```

## Brief

Computes the maximum along segments of a tensor.
Computes a tensor such that output[i]=(data[i]) where max is over j such that segment_ids[j] == i.
If the max is empty for a given segment ID i, output[i] = 0.

## Inputs

Two inputs, include:
- x:A Tensor of type, must be one of the following types: double, float32, float16, bfloat16,
int8, uint8, int16, uint16, int32, uint32, int64, uint64.
- segment_ids:should be the size of the first dimension
must sorted and need not cover all values in the full range of valid values
must be positive integer.

## Outputs

y:A Tensor with same type as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 segment_ids: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator SegmentMax.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
