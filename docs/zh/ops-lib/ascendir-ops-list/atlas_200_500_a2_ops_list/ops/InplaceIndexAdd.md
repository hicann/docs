# InplaceIndexAdd

```c
REG_OP(InplaceIndexAdd)
    .INPUT(var, TensorType({DT_INT16, DT_INT32, DT_INT8, DT_UINT8, DT_FLOAT32, DT_FLOAT16, DT_DOUBLE, DT_INT64, DT_BOOL,
                            DT_BF16}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(updates, TensorType({DT_INT16, DT_INT32, DT_INT8, DT_UINT8, DT_FLOAT32, DT_FLOAT16, DT_DOUBLE, DT_INT64,
                                DT_BOOL, DT_BF16}))
    .OPTIONAL_INPUT(alpha, TensorType({DT_INT16, DT_INT32, DT_INT8, DT_UINT8, DT_FLOAT32, DT_FLOAT16, DT_DOUBLE,
                                       DT_INT64, DT_BOOL, DT_BF16}))
    .OUTPUT(var, TensorType({DT_INT16, DT_INT32, DT_INT8, DT_UINT8, DT_FLOAT32, DT_FLOAT16, DT_DOUBLE, DT_INT64,
                             DT_BOOL, DT_BF16}))
    .REQUIRED_ATTR(axis, Int)
    .OP_END_FACTORY_REG(InplaceIndexAdd)
```

## Brief

Add updates to var according to axis and indices.

## Inputs

Three inputs, including:
- var: A Tensor. Must be one of the following types:
    double, float16, float32, int16, int32, int8, uint8, int64, bool, bfloat16.
- indices: A Tensor. The indices of updates to select from. Its type should be int32 or int64.
The indices should be 1-dimensional.
- updates: A Tensor of the same type as "var".
- alpha: An optional Tensor of the same type as "var". A scaling factor to updates.

## Outputs

var: A Tensor. Same as input "var".

## Attributes

axis: An required int to specify the axis to perform indices add. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32,int8,int16,int32,uint8
- input1 indices: int32,int64
- input2 updates: float16,float32,int8,int16,int32,uint8
- input3 alpha: float16,float32,int8,int16,int32,uint8
- output0 var: float16,float32,int8,int16,int32,uint8
### AI CPU
- input0 var: bool,double,float16,float32,int8,int16,int32,int64,uint8
- input1 indices: int32,int64
- input2 updates: bool,double,float16,float32,int8,int16,int32,int64,uint8
- input3 alpha: bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 var: bool,double,float16,float32,int8,int16,int32,int64,uint8

## Attention Constraints

- The shape values of var and updates should be the same in other dimensions except the axis dimension.
- The shape size of indices should be the same as updates in the axis dimension.
- The indices cannot contain negative values, and its value range cannot exceed the shape value range of var in the
axis dimension.

## Third-party framework compatibility

Compatible with the Pytorch operator index_add_.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
