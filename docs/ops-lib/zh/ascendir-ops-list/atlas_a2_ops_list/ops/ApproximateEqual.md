# ApproximateEqual

```c
REG_OP(ApproximateEqual)
  .INPUT(x1, TensorType::NumberType())
  .INPUT(x2, TensorType::NumberType())
  .OUTPUT(y, TensorType({DT_BOOL}))
  .ATTR(tolerance, Float, 1e-5f)
  .OP_END_FACTORY_REG(ApproximateEqual)
```

## Brief

Returns the truth value of abs(x1-x2) < tolerance element-wise. Support broadcasting operations.

## Inputs

- x1: A tensor. Must be one of the following types: float32, float64, int32, uint8, int16, int8, complex64, int64, qint8, quint8, qint32, uint16, complex128, float16, uint32, uint64
- x2: A tensor of the same dtype as "x1".

## Outputs

y: A tensor of type bool.

## Attributes

tolerance: Defaults to "1e-05". The supported type is the float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32
- input1 x2: float16,float32
- output0 y: bool
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 y: bool

## Third-party framework compatibility

Compatible with the TensorFlow operator ApproximateEqual.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
