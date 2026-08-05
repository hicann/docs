# Assign

```c
REG_OP(Assign)
    .INPUT(ref, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .INPUT(value, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .OUTPUT(ref, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .ATTR(validate_shape, Bool, true)
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(Assign)
```

## Brief

Updates "ref" by assigning "value" to it. Donot support broadcasting operations.

## Inputs

- ref: A ND Tensor. Support 1D ~ 8D. Must be one of the following types: bfloat16, float16, float32,
   double, int8, int16, int32, int64, uint8, uint16, uint32, uint64, complex32,
   complex64, complex128, qint8, quint8, qint16, qint32, quint16, bool, string.
   Support format list: ["NC1HWC0", "ND", "C1HWNCoC0", "FRACTAL_Z", "FRACTAL_Z_3D",
   "NDC1HWC0", "FRACTAL_NZ"].
- value: A ND Tensor of the same shape and dtype and format as "ref".

## Outputs

ref: A ND Tensor that holds the new value of ref after the value has been assigned.
Has the same shape and dtype and format as the input "ref". 

## Attributes

- validate_shape: An optional bool. Defaults to "true".
If "true", the operation will validate that the shape of "value" matches the shape of the Tensor being assigned to.
                   If "false", "ref" will take on the shape of "value".
                   This attribute is reserved.
- use_locking: An optional bool. Defaults to false.
If True, the assignment will be protected by a lock;
otherwise the behavior is undefined, but may exhibit less contention.
                This attribute is reserved. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 ref: bfloat16,bool,complex32,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 value: bfloat16,bool,complex32,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 ref: bfloat16,bool,complex32,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 ref: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 value: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 ref: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Assign.


---

[Back to Operator Specifications (Ascend950)](../README.md)
