# Concat

```c
REG_OP(Concat)
    .INPUT(concat_dim, TensorType::IndexNumberType())
    .DYNAMIC_INPUT(x, TensorType({BasicType(), DT_BOOL, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2, DT_HIFLOAT8, DT_FLOAT8_E8M0}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2, DT_HIFLOAT8, DT_FLOAT8_E8M0}))
    .ATTR(N, Int, 1)
    .OP_END_FACTORY_REG(Concat)
```

## Brief

Concatenates tensors along one dimension .

## Inputs

Two inputs, including:
- concat_dim: Must be one of the IndexNumberType: int32, int64.
Specifies the dimension along which to concatenate .
- x: Dynamic input.A ND Tensor.
Must be one of the BasicType:
complex128, complex64, double, float32, float16, int16, int32, int64, int8,
qint16, qint32, qint8, quint16, quint8, uint16, uint32, uint64, uint8,
bfloat16, complex32, bool, HIFLOAT8、FLOAT8_E5M2、FLOAT8_E4M3FN、FLOAT8_E8M0.. 

## Outputs

y: A Tensor. Has the same type and format as "x" . 

## Attributes

N: An optional int8, int16, int32, or int64. Specifies the number of elements in "x" .
Defaults to "1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 concat_dim: int32,int64
- input1 x: bfloat16,bool,complex64,double,float8_e4m3fn,float8_e5m2,float8_e8m0,float16,float32,hifloat8,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,double,float8_e4m3fn,float8_e5m2,float8_e8m0,float16,float32,hifloat8,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 concat_dim: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- "x" is a list of at least 2 "tensor" objects of the same type.
- "concat_dim" is in the range [-len(x.shape), len(x.shape)] .

## Third-party framework compatibility

Compatible with the TensorFlow operator Concat. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
