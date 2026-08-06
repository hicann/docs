# Abs

```c
REG_OP(Abs)
    .INPUT(x, "T")
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_UINT8, DT_BOOL, DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT16,
                             DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(Abs)
```

## Brief

Computes the absolute value of a tensor.

## Inputs

One input, including:
x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
uint8, bool, bfloat16, float16, float32, double, int8, int16, int32, int64.

## Outputs

y: A ND Tensor. Has the same dtype as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,complex32,complex64,float16,float32,int8,int16,int32,int64
- output0 y: bfloat16,float16,float32,int8,int16,int32,int64
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator Abs.


---

[Back to Operator Specifications (Ascend950)](../README.md)
