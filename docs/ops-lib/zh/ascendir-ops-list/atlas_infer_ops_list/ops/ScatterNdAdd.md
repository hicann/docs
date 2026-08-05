# ScatterNdAdd

```c
REG_OP(ScatterNdAdd)
    .INPUT(var, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16,
                            DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8,
                                DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .OUTPUT(var, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16,
                             DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ScatterNdAdd)
```

## Brief

Applies sparse "updates" to individual values or slices in a variable reference using the "add" operation.

## Inputs

- var: The rewritten tensor. An ND tensor. Support 1D ~ 8D. Must be one of the following types:
complex128, complex64, double, float32, float16, int8, uint8, int16, uint16, int32, uint32, int64, uint64, bool.
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
- input0 var: bool,float16,float32,int32
- input1 indices: int32,int64
- input2 updates: bool,float16,float32,int32
- output0 var: bool,float16,float32,int32
### AI CPU
- input0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 updates: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterNdAdd.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
