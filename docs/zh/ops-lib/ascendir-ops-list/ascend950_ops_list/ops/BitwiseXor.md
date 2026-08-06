# BitwiseXor

```c
REG_OP(BitwiseXor)
    .INPUT(x1, TensorType::IntegerDataType())
    .INPUT(x2, TensorType::IntegerDataType())
    .OUTPUT(y, TensorType::IntegerDataType())
    .OP_END_FACTORY_REG(BitwiseXor)
```

## Brief

Elementwise computes the bitwise XOR of "x1" and "x2". Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types: int8, int16, int32, int64, uint8, uint16, uint32, uint64.
      The format is ND. Broadcasting is supported.
- x2: A ND Tensor. Has the same dtype and format as "x1".

## Outputs

y: Output result. A ND Tensor. Has the same dtype and format as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 x1: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with TensorFlow operator BitwiseXor.


---

[Back to Operator Specifications (Ascend950)](../README.md)
