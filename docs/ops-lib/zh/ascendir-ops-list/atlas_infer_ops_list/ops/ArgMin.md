# ArgMin

```c
REG_OP(ArgMin)
    .INPUT(x, TensorType::NumberType())
    .INPUT(dimension, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(dtype, Type, DT_INT64)
    .OP_END_FACTORY_REG(ArgMin)
```

## Brief

Returns the index with the smallest value across dimensions of a tensor.

## Inputs

Two inputs, including:
- x: A ND Tensor. Must be one of the following types: float32, float64, int32, uint8, int16, int8, complex64, int64, qint8, quint8, qint32, bfloat16, uint16, complex128, float16, uint32, uint64.
format is ND.
- dimension: A 1D ND tensor or scalar, data type is int32 or int64 and value range is [-rank(input x), rank(input x)].
Describes which dimension of the input tensor to reduce across.

## Outputs

y: A ND Tensor of type "dtype".

## Attributes

dtype: The output type, either "int32" or "int64". Defaults to "int64".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 dimension: int32,int64
- output0 y: int32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 dimension: int32,int64
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with TensorFlow operator ArgMin.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
