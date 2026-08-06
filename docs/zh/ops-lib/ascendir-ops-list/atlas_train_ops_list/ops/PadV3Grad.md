# PadV3Grad

```c
REG_OP(PadV3Grad)
    .INPUT(x, TensorType::BasicType())
    .INPUT(paddings, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .ATTR(mode, String, "reflect")
    .ATTR(paddings_contiguous, Bool, true)
    .OP_END_FACTORY_REG(PadV3Grad)
```

## Brief

Cal the grad of Pads.

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: float16, bfloat16, float32, double, int32,
    uint8, int16, int8, complex64, int64, qint8, quint8, qint32, qint16, quint16, uint16,
    complex128, uint32, uint64.
- paddings: A Tensor of type int32 or int64.
1-D. The size is twice of the dimensionality of input x.

## Outputs

y: A Tensor of the same type and dimensionality as "x". The shape of y and input x satisfy the
mathematical relationship of the padding operation.

## Attributes

- mode: An optional string, Defaults to "reflect", indicates paddings mode,
    support "reflect", "edge", "constant", "symmetric", "circular".
- paddings_contiguous: An optional bool value, Defaults to true.
    If true, paddings is arranged as [[begin0, end0], [begin1, end1], ...]
    If false, paddings is arranged as [[begin0, begin1], ..., [end0, end1], ...]

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 paddings: int32,int64
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 paddings: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with ONNX operator PadGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
