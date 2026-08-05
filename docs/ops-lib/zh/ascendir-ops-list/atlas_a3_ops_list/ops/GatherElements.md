# GatherElements

```c
REG_OP(GatherElements)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16,
                          DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_FLOAT8_E5M2, DT_FLOAT8_E8M0, DT_FLOAT8_E4M3FN}))
    .INPUT(index, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16,
                           DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_FLOAT8_E5M2, DT_FLOAT8_E8M0, DT_FLOAT8_E4M3FN}))
    .ATTR(dim, Int, 0)
    .OP_END_FACTORY_REG(GatherElements)
```

## Brief

Gather slices from "x" according to "index" by corresponding dim, produces a output tensor
with shape(index.shape).

## Inputs

- x: A Tensor. Must be one of the following types: float16, bfloat16, float32, uint32, int32, uint64,
int64, uint8, int8, uint16, int16, bool, double, DT_FLOAT8_E5M2, DT_FLOAT8_E8M0, DT_FLOAT8_E4M3FN.
- index: The index tensor used for collecting values. A Tensor. Must be one of the following types: int32, int64.The
number of dimensions
of index needs to be consistent with that of x, and its shape needs to be consistent with that of y.
Except for the dimension specified by dim, the size of other dimensions should be less than or equal
to the size of the corresponding dimension of x.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

dim: the axis along which to index, int32 or int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 index: int32,int64
- output0 y: bfloat16,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 index: int32,int64
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the PyTorch operator Gather.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
