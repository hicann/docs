# AssignSub

```c
REG_OP(AssignSub)
    .INPUT(var, TensorType::NumberType())
    .INPUT(value,TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(AssignSub)
```

## Brief

Updates "var" by subtracting "value" from it.
This operation outputs "var" after the update is done. 
This makes it easier to chain operations that need to use the reset value.

## Inputs

- var: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bfloat16, float32, float64, int32, uint8
int16, int8, complex64, int64, qint8, quint8, qint32, uint16, complex128, uint32, uint64
- value: A tensor of the same dtype as "var".

## Outputs

y: A tensor. Has the same dtype as "var".

## Attributes

use_locking: An optional bool. Defaults to "False". If "True", the subtraction will be protected 
by a lock; otherwise the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32,int8,int32,int64,uint8
- input1 value: bfloat16,float16,float32,int8,int32,int64,uint8
- output0 var: bfloat16,float16,float32,int8,int32,int64,uint8
### AI CPU
- input1 value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator AssignSub.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
