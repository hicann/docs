# UniqueWithCounts

```c
REG_OP(UniqueWithCounts)
    .INPUT(x, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
           DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_STRING,
           DT_BF16, DT_UINT32, DT_UINT64 }))
    .OUTPUT(y, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
           DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_STRING,
           DT_BF16, DT_UINT32, DT_UINT64 }))
    .OUTPUT(idx, TensorType({ DT_INT32, DT_INT64 }))
    .OUTPUT(count, TensorType({ DT_INT32, DT_INT64 }))
    .REQUIRED_ATTR(out_idx, Type)
    .OP_END_FACTORY_REG(UniqueWithCounts)
```

## Brief

Finds unique elements in a 1D tensor. 

## Inputs

x: 1D tensor. Support all types mentioned in TensorType.
Input "x" is a k-dimensional tensor. 

## Outputs

- y: A Tensor. Has the same type as "x".
- idx: A Tensor of type "out_idx".
- count: A Tensor of type "out_idx".

## Attributes

out_idx: A required DType from: "int32, int64". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- output1 idx: int32,int64
- output2 count: int32,int64

## Attention Constraints

- UniqueWithCounts runs on the Ascend AI CPU, which delivers poor performance.
- Dtype bfloat16, uint32, uint64 only support Ascend 950 AI Processor.

## Third-party framework compatibility

Compatible with the TensorFlow operator UniqueWithCounts.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
