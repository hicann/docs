# ArgMaxV2

```c
REG_OP(ArgMaxV2)
    .INPUT(x, TensorType::NumberType())
    .INPUT(dimension, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(dtype, Type, DT_INT64)
    .OP_END_FACTORY_REG(ArgMaxV2)
```

## Brief

Returns the index with the largest value across axes of a tensor.

## Inputs

Two inputs, including:
- x: A ND and multi-dimensional tensor of type float16, float32, int32, or int16.
- dimension: A Scalar of type int32, specifying the index with the largest value.

## Outputs

y: A ND tensor of type int32 or int64, specifying the index with the largest value. The dimension is one less than that of "x".

## Attributes

dtype: The output type, either "int32" or "int64". Defaults to "int64".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32,int64
- input1 dimension: int32,int64
- output0 y: int32,int64
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 dimension: int32,int64
- output0 y: int32,int64

## Attention Constraints

- x: If there are multiple maximum values, the index of the first maximum value is used.
- The value range of "dimension" is [-dims, dims - 1]. "dims" is the dimension length of "x".

## Third-party framework compatibility

Compatible with TensorFlow operator ArgMax.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
