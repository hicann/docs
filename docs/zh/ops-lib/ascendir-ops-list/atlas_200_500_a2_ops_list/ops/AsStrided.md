# AsStrided

```c
REG_OP(AsStrided)
    .INPUT(x, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_BOOL}))
    .INPUT(size, TensorType::IndexNumberType())
    .INPUT(stride, TensorType::IndexNumberType())
    .INPUT(storage_offset, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_BOOL}))
    .OP_END_FACTORY_REG(AsStrided)
```

## Brief

Make memory of a view be contiguous.

## Inputs

Four inputs, including:
- x: The input tensor. Must be the type of hifloat8, float8_e5m2,
float8_e4m3fn, bool and BasicType. Support format "ND".
- size: The shape of output tensor. Must be the type of
IndexNumberType(IndexNumberType includes: int32, int64).
All elements in the size must be non-negative integers.
Support format "ND".
- stride: The stride of output tensor. Must be the type of IndexNumberType.
All elements in the stride must be non-negative integers.
Support format "ND".
- storage_offset: The offset in the underlying storage of the output tensor.
Must be a non-negative interger.
Must be the type of IndexNumberType. Support format "ND".

## Outputs

y: A Tensor. Has the same type as "x". Support format "ND".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float8_e4m3fn,float8_e5m2,hifloat8
- input1 size: int32,int64
- input2 stride: int32,int64
- input3 storage_offset: int32,int64
- output0 y: bool,float8_e4m3fn,float8_e5m2,hifloat8

## Third-party framework compatibility

Compatible with the PyTorch operator as_strided.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
