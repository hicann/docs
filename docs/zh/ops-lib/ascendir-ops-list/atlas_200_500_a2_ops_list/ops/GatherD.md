# GatherD

```c
REG_OP(GatherD)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32
                          DT_INT64, DT_UINT64, DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(dim, TensorType({DT_INT32, DT_INT64}))
    .INPUT(index, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_FLOAT16, DT_FLOAT,
                           DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_BF16}))
    .ATTR(dim, Int, 0)
    .OP_END_FACTORY_REG(GatherD)
```

## Brief

Gather slices from "x" according to "indices" by corresponding dim, produces a output tensor
with shape(x.shape[:dim]+indices.shape[batch:]+x.shape[dim+1:]). When the impl_mode is set
as "support out of bound index", if the indices data is out of bound, the corresponding results
will be set as 0. Otherwise, an aic_error will occur.

## Inputs

- x: A ND Tensor. Support 1D ~ 8D.
Must be one of the following types: int8, uint8, int16, uint16, int32, uint32, int64,
uint64, bool, bfloat16, float16, float32, double.
- index: A ND Tensor. Support 1D ~ 8D. Must be one of the following types: int32, int64.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

dim: An optional int. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 dim: int32,int64
- input2 index: int32,int64
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the PyTorch operator Gather.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
