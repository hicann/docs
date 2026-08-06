# Cumprod

```c
REG_OP(Cumprod)
    .INPUT(x, TensorType::NumberType())
    .INPUT(axis, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::NumberType())
    .ATTR(exclusive, Bool, false)
    .ATTR(reverse, Bool, false)
    .OP_END_FACTORY_REG(Cumprod)
```

## Brief

Computes the cumulative product of the tensor "x" along "axis" .

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types:
double, float32, float16, bfloat16, complex32, complex64, complex128,
int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint32.
- axis: A Tensor of type int32 or int64. Range is [-rank(x),rank(x)). Defaults to "0".

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- exclusive: If "False", performs inclusive cumprod, which means that the first element of the input
is identical to the first element of the output. If "True", performs exclusive cumprod.
- reverse: A bool. Defaults to "False".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 axis: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Cumprod.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
