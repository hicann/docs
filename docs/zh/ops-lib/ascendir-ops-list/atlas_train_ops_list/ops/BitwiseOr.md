# BitwiseOr

```c
REG_OP(BitwiseOr)
    .INPUT(x1, TensorType::IntegerDataType())
    .INPUT(x2, TensorType::IntegerDataType())
    .OUTPUT(y, TensorType::IntegerDataType())
    .OP_END_FACTORY_REG(BitwiseOr)
```

## Brief

Element-wise computes the bitwise OR of "x1" and "x2". Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types: int8, int16,
    int32, int64, uint8, uint16, uint32, uint64. Broadcasting is supported.
- x2: A ND Tensor of the same dtype and format as "x1".

## Outputs

y: A ND Tensor. Has the same dtype and format as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: int16,int32,uint16
- input1 x2: int16,int32,uint16
- output0 y: int16,int32,uint16
### AI CPU
- input0 x1: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator BitwiseOr.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
