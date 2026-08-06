# ScatterAdd

```c
REG_OP(ScatterAdd)
    .INPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .OUTPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ScatterAdd)
```

## Brief

Adds sparse "updates" to a variable reference.

## Inputs

- var: The rewritten tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types:
float16, float32, int32, int8, uint8.
- indices: The index tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types: int32, int64.
- updates: The source tensor. An ND tensor. Support 1D ~ 8D. Shape should be equal to the shape of "indices" concats
the shape of "var" except for the first dimension. Must have the same type of "var".

## Outputs

var: An ND tensor. Support 1D ~ 8D. Must have the same type, shape and format as input "var".

## Attributes

use_locking: Ignore this attribute. This attribute does not take effect even if it is set. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: bfloat16,float16,float32,int8,int32,uint8
- output0 var: bfloat16,float16,float32,int8,int32,uint8
### AI CPU
- input0 var: float16,float32,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: float16,float32,int8,int32,uint8
- output0 var: float16,float32,int8,int32,uint8

## Attention Constraints

updates.shape = indices.shape + var.shape[1:] or updates.shape = []. 

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterAdd.


---

[Back to Operator Specifications (Ascend950)](../README.md)
