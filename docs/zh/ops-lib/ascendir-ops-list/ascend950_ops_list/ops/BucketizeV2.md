# BucketizeV2

```c
REG_OP(BucketizeV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8}))
    .INPUT(boundaries, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(out_int32, Bool, false)
    .ATTR(right, Bool, false)
    .OP_END_FACTORY_REG(BucketizeV2)
```

## Brief

Bucketize 'x' based on 'boundaries'. For example, if the inputs
are boundaries = [0, 10, 100] x = [[-5, 10000] [150, 10] [5, 100]] then
the output will be [[0, 3] [3, 2] [1, 3]].

## Inputs

Two inputs, including:
- x: A tensor. Must be one of the following types:
    float16, float32, bfloat16, int8, int16, int32, int64, uint8. 
- boundaries: A sorted 1-dim tensor with same type as x. It gives the boundary of the buckets. Must be one of the
following types:
    float16, float32, bfloat16, int8, int16, int32, int64, uint8. 

## Outputs

y: A tensor with the same shape as 'x', each value of input replaced with bucket index.
Must be one of the following types: int32, int64. 

## Attributes

- out_int32: An optional true or false. If true, the dtype of y is int32. Otherwise, it is int64. Defaults to false.
- right: An optional true or false. If true, return upperbound index. If false return lowerbound index.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int16,int32,int64,uint8
- input1 boundaries: bfloat16,float16,float32,int8,int16,int32,int64,uint8
- output0 y: int32,int64

## Attention Constraints

- The output has the same shape as the input.
- ‌The boundaries must be in ascending order and non-repeating.

## Third-party framework compatibility

Compatible with the Pytorch operator bucketize. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
