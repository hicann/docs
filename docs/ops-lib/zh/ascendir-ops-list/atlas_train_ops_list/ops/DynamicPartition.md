# DynamicPartition

```c
REG_OP(DynamicPartition)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL, DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE,\
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(partitions, TensorType({DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL, DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE,\
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .ATTR(num_partitions, Int, 1)
    .OP_END_FACTORY_REG(DynamicPartition)
```

## Brief

Partitions "x" into "num_partitions" tensors using indices from "partitions".

## Inputs

Including:
- x: The tensor to be sliced. Must be one of the following types:
DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL, DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE,
DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN.
- partitions: A tensor of type DT_INT32, with any shape.

## Outputs

y: A list of tensors with same data type of x.

## Attributes

num_partitions: An optional attribute of type int, specifying the count of output, which must meet >= 1. Defaults to "1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input1 partitions: int32

## Third-party framework compatibility

Compatible with the TensorFlow operator DynamicPartition.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
