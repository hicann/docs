# ConjugateTranspose

```c
REG_OP(ConjugateTranspose)
    .INPUT(x, TensorType::BasicType())
    .INPUT(perm, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(ConjugateTranspose)
```

## Brief

Returns the complex conjugatetranspose.

## Inputs

- x: A Tensor. Must be one of the following types: double, float32, float16, bfloat16, complex32, complex64, complex128,
int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint16, quint16, qint32.
- perm: A Index. Must be one of the following types: int32, int64

## Outputs

- y: A Tensor. Has the same type as "x" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 perm: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility.

Compatible with tensorflow ConjugateTranspose operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
