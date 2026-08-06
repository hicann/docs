# IsClose

```c
REG_OP(IsClose)
    .INPUT(x1, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .INPUT(x2, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .ATTR(rtol, Float, 1e-05f)
    .ATTR(atol, Float, 1e-08f)
    .ATTR(equal_nan, Bool, false)
    .OP_END_FACTORY_REG(IsClose)
```

## Brief

Returns a new tensor with boolean elements representing 
if each element of input is “close” to the corresponding element of other

## Inputs

Two inputs, including:
- x1: A tensor. Must be one of the following types:
    float16, float, double, bfloat16, int8, int16, int32, int64, qint8, qint16, qint32, qint64,
    quint8, uin8, uint16, uint32, uint64, complex32, complex64, complex128, bool. 
- x2: A tensor with the same dtype and shape as 'x1'.

## Outputs

y: A tensor bool with the same shape as 'x1'. 

## Attributes

- rtol: An optional float.Defaults to 1e-05.
- atol: An optional float.Defaults to 1e-08.
- equal_nan: An optional bool.Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- output0 y: bool
### AI CPU

## Third-party framework compatibility

Compatible with the PyTorch operator isclose. 


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
