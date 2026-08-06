# ConcatV2

```c
REG_OP(ConcatV2)
    .DYNAMIC_INPUT(x, TensorType({BasicType(), DT_BOOL, DT_STRING, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2, DT_HIFLOAT8, DT_FLOAT8_E8M0}))
    .INPUT(concat_dim, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_STRING, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2, DT_HIFLOAT8, DT_FLOAT8_E8M0}))
    .ATTR(N, Int, 1)
    .OP_END_FACTORY_REG(ConcatV2)
```

## Brief

Concatenates tensors along one dimension .

## Inputs

Two inputs, including:
- Dynamic input "x" is A ND Tensor.
Must be one of the following types: bfloat16, float16, float32, double, int32,
    uint8, int16, int8, complex64, int64, qint8, quint8, qint32, uint16,
    complex128, uint32, uint64, qint16, quint16, bool, string, HIFLOAT8, FLOAT8_E5M2, FLOAT8_E4M3FN, FLOAT8_E8M0.
- concat_dim: A 0D Tensor (scalar) with dtype int32, or int64. Specifies the dimension along which to concatenate .

## Outputs

y: A Tensor. Has the same type and format as "x" . 

## Attributes

N: An optional int includes all types of int.
Specifies the number of elements in "x". Defaults to "1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 concat_dim: int32
### AI CPU
- input1 concat_dim: int32,int64
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

"x" is a list of at least 2 "tensor" objects of the same type . 

## Third-party framework compatibility

Compatible with the TensorFlow operator ConcatV2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
