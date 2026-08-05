# ScatterNdMax

```c
REG_OP(ScatterNdMax)
    .INPUT(var, TensorType::BasicType())
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType::BasicType())
    .OUTPUT(var,  TensorType::BasicType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ScatterNdMax)
```

## Brief

Applies sparse "updates" to individual values or slices in a variable reference using the "max" operation.

## Inputs

- var: The rewritten tensor. An ND tensor of type BasicType. Support 1D ~ 8D.
- indices: The index tensor. An ND tensor of type int32 or int64. Support 1D ~ 8D. The last dimension of "indices"
represents that the first few dimensions of "var" are the batch dimensions.
- updates: The source tensor. A tensor with the same dtype as 'var'. Support 1D ~ 8D. Shape should be equal to the
shape of "indices" except for the last dimension concats the shape of "var" except for the batch dimensions.

## Outputs

var: A Tensor. Support 1D ~ 8D. Must have the same type, shape and format as input "var".

## Attributes

- use_locking: An optional bool. Defaults to "False". If "True", the operation will be protected by a lock.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 var: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 updates: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 var: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator ScatterNdMax.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
