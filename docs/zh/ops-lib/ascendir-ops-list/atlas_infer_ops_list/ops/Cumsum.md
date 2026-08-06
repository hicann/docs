# Cumsum

```c
REG_OP(Cumsum)
    .INPUT(x, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128, DT_BF16}))
    .INPUT(axis, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128, DT_BF16}))
    .ATTR(exclusive, Bool, false)
    .ATTR(reverse, Bool, false)
    .OP_END_FACTORY_REG(Cumsum)
```

## Brief

Computes the cumulative sum of the tensor "x" along "axis" .

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types:
int8, int16, int32, int64, uint8, uint16, uint32, uint64, float16, float32,
double, complex64, complex128, bfloat16.
- axis: A Tensor of type int32 or int64. Range is [-rank(x),rank(x)). Dim and shape must be 1.

## Outputs

y: A Tensor. Has the same type and shape as "x".

## Attributes

- exclusive: A bool. Defaults to "False". If "False", performs inclusive cumsum, which means that the first element
of the input is identical to the first element of the output. If "True", performs exclusive cumsum.
- reverse: A bool. Defaults to "False". If "True", the cumulative sum is calculated from the end of the
tensor towards the beginning. If "False", the cumulative sum is calculated from the beginning of the tensor towards
the end.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- input1 axis: int32,int64
- output0 y: float16,float32,int32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 axis: int32,int64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Cumsum.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
