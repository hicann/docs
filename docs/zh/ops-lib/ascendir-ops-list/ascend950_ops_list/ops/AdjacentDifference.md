# AdjacentDifference

```c
REG_OP(AdjacentDifference)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8, DT_INT16, DT_INT32, DT_INT64,
                          DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(y_dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(AdjacentDifference)
```

## Brief

Compare two consecutive values in input tensor, if they are equal, return 0; otherwise, return 1. 
y[0] = 0;
y[i] = x[i] == x[i - 1] ? 0 : 1;

## Inputs

Inputs include:
x: A tensor. Dtype support: float16, float, bfloat16, int16, int8, int32, int64, uint8, uint32,
uint16, uint64, support format: [ND].

## Outputs

y: A tensor. Must have the same shpae as x, dtype support int32, int64. Support format: [ND].

## Attributes

y_dtype: The output type, either "DT_INT32(3)" or "DT_INT64(9)". Defaults to "DT_INT32(3)".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int32,int64


---

[Back to Operator Specifications (Ascend950)](../README.md)
