# CastLike

```c
REG_OP(CastLike)
    .INPUT(x, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .INPUT(target, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_STRING}))
    .OP_END_FACTORY_REG(CastLike)
```

## Brief

The operator casts the elements of a given input tensor (the first input)
to the same data type as the elements of the second input tensor.

## Inputs

Two inputs, including:
- x:A ND Tensor. Must be one of the following types:
float16, float, int8, int32, uint32, uint8, int64, uint64, int16, uint16, double,
complex64, complex128, qint8, quint8, qint16, quint16, qint32, bfloat16, bool, string.  
- target:A ND Tensor. Must be one of the following types:
float16, float, int8, int32, uint32, uint8, int64, uint64, int16, uint16, double,
complex64, complex128, qint8, quint8, qint16, quint16, qint32, bfloat16, bool, string.  

## Outputs

y:A ND Tensor with same shape as x, and data type is specified by target.

## Third-party framework compatibility

Compatible with the onnx operator CastLike.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
