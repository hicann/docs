# Coordinates1DTo2D

```c
REG_OP(Coordinates1DTo2D)
    .INPUT(x, TensorType({DT_INT32, DT_INT64, DT_UINT64}))
    .INPUT(shape, TensorType({DT_INT32, DT_INT64, DT_UINT64}))
    .OUTPUT(row, TensorType({DT_INT32, DT_INT64, DT_UINT64}))
    .OUTPUT(col, TensorType({DT_INT32, DT_INT64, DT_UINT64}))
    .OUTPUT(n, TensorType({DT_INT32, DT_INT64, DT_UINT64}))
    .OP_END_FACTORY_REG(Coordinates1DTo2D)
```

## Brief

Converts 1D coordinate to 2D coordinate based on shape information.

## Inputs

Two inputs:
- x: 1D coordinate index value.
  Must be one of the following types: int32, int64, uint64. 
- shape: Shape information with 4 elements (N, D, H, W).
  Must be one of the following types: int32, int64, uint64. 

## Outputs

Three outputs:
- row: Row index result.
- col: Column index result.
- n: Column count (W dimension value).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: int32,int64,uint64
- input1 shape: int32,int64,uint64
- output0 row: int32,int64,uint64
- output1 col: int32,int64,uint64
- output2 n: int32,int64,uint64

## Attention Constraints

- input[shape] element count must be 4.
- input[x] and input[shape] data type must be the same.
- shape[3] (W dimension) cannot be 0.

## Third-party framework compatibility

Compatible with internal Huawei operator. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
