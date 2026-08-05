# MatrixSetDiag

```c
REG_OP(MatrixSetDiag)
    .INPUT(x, TensorType::BasicType())
    .INPUT(diagonal, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(MatrixSetDiag)
```

## Brief

Returns a batched matrix tensor with new batched diagonal values . 

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types:
   float16, float32, double, int32, uint8, int16, int8, complex64, int64,
   qint8, quint8, qint32, uint16, complex128, uint32, uint64.
- diagonal: A Tensor of the same type as "x" .

## Outputs

y: A Tensor. Has the same type as "x" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 diagonal: bfloat16,bool,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator MatrixSetDiag.


---

[Back to Operator Specifications (Ascend950)](../README.md)
