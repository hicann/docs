# ScatterNdUpdate

```c
REG_OP(ScatterNdUpdate)
    .INPUT(var, TensorType({BasicType(), DT_BOOL, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({BasicType(), DT_BOOL, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0}))
    .OUTPUT(var,  TensorType({BasicType(), DT_BOOL, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ScatterNdUpdate)
```

## Brief

Applies sparse "updates" to individual values or slices in a variable reference.

## Inputs

- var: The rewritten tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types:
complex128, complex64, double, float32, float16, int16, int32, int64, int8, qint16, qint32, qint8, quint16, quint8,
uint16, uint32, uint64, uint8, bfloat16, bool.
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
- input0 var: bfloat16,bool,float16,float32,int8,int16,int32,int64
- input1 indices: int32,int64
- input2 updates: bfloat16,bool,float16,float32,int8,int16,int32,int64
- output0 var: bfloat16,bool,float16,float32,int8,int16,int32,int64
### AI CPU
- input0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 updates: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterNdUpdate.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
