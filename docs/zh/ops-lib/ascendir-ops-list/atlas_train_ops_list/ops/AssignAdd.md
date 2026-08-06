# AssignAdd

```c
REG_OP(AssignAdd)
    .INPUT(ref, TensorType::BasicType())
    .INPUT(value,TensorType::BasicType())
    .OUTPUT(ref, TensorType::BasicType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(AssignAdd)
```

## Brief

Updates "ref" by adding "value" to it. Donot support broadcasting operations.

## Inputs

- ref: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bfloat16, float16, float32, int8,
int16, int32, int64, uint8, uint16, uint32, uint64.
- value: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bfloat16, float16, float32, int8,
int16, int32, int64, uint8, uint16, uint32, uint64.

## Outputs

ref: A ND Tensor that holds the new value of ref after the value has been added.

## Attributes

use_locking: An optional bool. Defaults to "False".
If "True", the addition will be protected by a lock;
otherwise the behavior is undefined, but may exhibit less contention.
            This attribute is reserved.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 ref: float16,float32,int32,int64
- input1 value: float16,float32,int32,int64
- output0 ref: float16,float32,int32,int64
### AI CPU
- input0 ref: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 ref: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

An input tensor of type int64 must have a shape with size 1.

## Third-party framework compatibility

Compatible with the TensorFlow operator AssignAdd.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
