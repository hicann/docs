# Unique

```c
REG_OP(Unique)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
           DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE,
           DT_BF16, DT_UINT32, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
           DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE,
           DT_BF16, DT_UINT32, DT_UINT64}))
    .OUTPUT(idx, TensorType({DT_INT32, DT_INT64}))
    .ATTR(out_idx, Type, DT_INT32)
    .OP_END_FACTORY_REG(Unique)
```

## Brief

Finds unique elements in a 1D tensor. 

## Inputs

x: 1D tensor. Support all types mentioned in TensorType.
Input "x" is a 1D tensor. 

## Outputs

- y: "x" in the unique output "y".
- idx: A tensor the same size as "x". The index of each value of "x".

## Attributes

out_idx: An optional DType from: "int32, int64". Defaults to "int32". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output1 idx: int32,int64

## Attention Constraints

- Unique runs on the Ascend AI CPU, which delivers poor performance.
- Dtype bfloat16, uint32, uint64 only support Ascend 950 AI Processor.

## Third-party framework compatibility

Compatible with the TensorFlow operator Unique.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
