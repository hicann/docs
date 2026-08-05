# ClipByValueV2

```c
REG_OP(ClipByValueV2)
    .INPUT(x, TensorType::NumberType())
    .INPUT(clip_value_min, TensorType::NumberType())
    .INPUT(clip_value_max, TensorType::NumberType())
    .OUTPUT(y, TensorType::NumberType())
    .OP_END_FACTORY_REG(ClipByValueV2)
```

## Brief

Clips tensor values to a specified min and max.
When the input is bfloat16, float16, float32, int32 or int64, broadcasting operations are supported.  

## Inputs

Three inputs, including:
- x: A ND tensor with TensorType::NumberType().
- clip_value_min: A ND tensor of the same dtype as "x".
- clip_value_max: A ND tensor of the same dtype as "x".

## Outputs

y: A ND tensor. Has the same dtype as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32,int64
- input1 clip_value_min: bfloat16,float16,float32,int32,int64
- input2 clip_value_max: bfloat16,float16,float32,int32,int64
- output0 y: bfloat16,float16,float32,int32,int64
### AI CPU
- input0 x: bfloat16,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 clip_value_min: bfloat16,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input2 clip_value_max: bfloat16,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 y: bfloat16,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the PyTorch operator clip.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
