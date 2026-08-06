# SpaceToBatchND

```c
REG_OP(SpaceToBatchND)
    .INPUT(x, TensorType::BasicType())
    .INPUT(block_shape, TensorType::IndexNumberType())
    .INPUT(paddings, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(SpaceToBatchND)
```

## Brief

Zeros-pads and then permutes blocks of spatial data into batch.
The values from the height and width dimensions are moved in spatial blocks to the batch dimension.
After zeros-pads the height and width dimensions. 

## Inputs

- x: A ND tensor. Format is ND. Must be one of the following types:
float16, float32, double, int64, int32, uint8, uint16, uint32, uint64, int8,
int16, complex64, complex128, qint8, quint8, qint16, quint16, qint32, bfloat16.
- block_shape: A 1D tensor with shape [M]. Format is ND. Support int32 or int64.
- paddings: A 2D tensor with shape [M, 2]. Format is ND. Support int32 or int64.

## Outputs

y: A tensor, the same type and format as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 block_shape: int32,int64
- input2 paddings: int32,int64
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- input1 block_shape: int32,int64
- input2 paddings: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator SpaceToBatchND.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
