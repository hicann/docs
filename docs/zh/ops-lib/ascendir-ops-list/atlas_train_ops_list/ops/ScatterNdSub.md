# ScatterNdSub

```c
REG_OP(ScatterNdSub)
    .INPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .OUTPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ScatterNdSub)
```

## Brief

Applies sparse "updates" to individual values or slices in a variable reference using the "sub" operation.

## Inputs

- var: The rewritten tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types:
float16, float32, int32, int8, uint8.
- indices: The index tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types: int32, int64. The
last dimension of "indices" represents that the first few dimensions of "var" are the batch dimensions.
- updates: The source tensor. An ND tensor. Support 1D ~ 8D. Shape should be equal to the shape of "indices" except
for the last dimension concats the shape of "var" except for the batch dimensions. Must have the same type of "var".

## Outputs

var: An ND tensor. Support 1D ~ 8D. Must have the same type, shape and format as input "var".

## Attributes

use_locking: An optional bool. Defaults to "False". If "True", the operation will be protected by a lock.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32,int32
- input1 indices: int32,int64
- input2 updates: float16,float32,int32
- output0 var: float16,float32,int32
### AI CPU
- input0 var: float16,float32,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: float16,float32,int8,int32,uint8
- output0 var: float16,float32,int8,int32,uint8

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterNdSub.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
