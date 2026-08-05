# ScatterMin

```c
REG_OP(ScatterMin)
    .INPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .OUTPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ScatterMin)
```

## Brief

Reduces sparse updates into a variable reference using the "min" operation.

## Inputs

- var: The rewritten tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types:
float16, float32, int32, int8, uint8.
- indices: The index tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types: int32, int64.
- updates: The source tensor. An ND tensor. Support 1D ~ 8D. Shape should be equal to the shape of "indices" concats
the shape of "var" except for the first dimension. Must have the same type of "var".

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
- input0 var: double,float16,float32,int32,int64
- input1 indices: int32,int64
- input2 updates: double,float16,float32,int32,int64
- output0 var: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterMin.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
