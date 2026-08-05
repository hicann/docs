# Sort

```c
REG_OP(Sort)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT16, DT_INT8,
                          DT_UINT8, DT_INT32, DT_INT64, DT_BF16,
                          DT_UINT32, DT_UINT16, DT_UINT64}))
    .OUTPUT(y1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT16, DT_INT8,
                            DT_UINT8, DT_INT32, DT_INT64, DT_BF16,
                            DT_UINT32, DT_UINT16, DT_UINT64}))
    .OUTPUT(y2, TensorType({DT_INT32, DT_INT64}))
    .ATTR(axis, Int, -1)
    .ATTR(descending, Bool, false)
    .ATTR(stable, Bool, false)
    .ATTR(y2_dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(Sort)
```

## Brief

sort the input tensor and return the value of index.

## Inputs

Inputs include:
x: A Tensor. Supported type: float16, float32, int16, int8, uint8, int32, int64, bfloat16, uint32, uint16, uint64.
Supported format: ND . 

## Outputs

- y1: A Tensor. Must have the same dtype shape and format as x.
- y2: A Tensor. Indices of y1 in x. Dtype must be int32 or int64. Must have the same shape and format as x.

## Attributes

- axis: An optional attribute indicates the sorting axis. Defaults to "-1".Only supports sorting along the
last dimension.
- descending: An optional attribute indicates desending sort or not. Defaults to "false".
- stable: An optional attribute indicates the sort result of y2 is stable or not. Defaults to "false" .
Setting it to false is also a stable sort.
- y2_dtype: An optional attribute indicates the sort result of y2's dtype, int32 or int64, defaults to "int32" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y1: bfloat16,float16,float32
- output1 y2: int32
### AI CPU
- input0 x: float16,float32,int8,int16,int32,int64,uint8
- output0 y1: float16,float32,int8,int16,int32,int64,uint8
- output1 y2: int32

## Attention Constraints

The operator depends on the unstable sorting algorithm.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
