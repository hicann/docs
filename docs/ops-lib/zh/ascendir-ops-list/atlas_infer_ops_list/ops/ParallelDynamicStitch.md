# ParallelDynamicStitch

```c
REG_OP(ParallelDynamicStitch)
    .DYNAMIC_INPUT(indices, TensorType({DT_INT32}))
    .DYNAMIC_INPUT(x,
        TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, \
        DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_STRING, DT_COMPLEX64, DT_COMPLEX128, \
        DT_QINT8, DT_QUINT8, DT_QINT32 }))
    .OUTPUT(y,
        TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, \
        DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_STRING, DT_COMPLEX64, DT_COMPLEX128, \
        DT_QINT8, DT_QUINT8, DT_QINT32 }))
    .ATTR(N, Int, 1)
    .OP_END_FACTORY_REG(ParallelDynamicStitch)
```

## Brief

Interleaves the values from the "x" tensors into a single tensor. 

## Inputs

Including:
- indices: A list of at least 1 Tensor objects with type DT_INT32. It's a dynamic input.
- x: A list with the same length as "indices" of Tensor objects. It's a dynamic input.
Must be one of the following types: DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_STRING,
DT_COMPLEX64, DT_COMPLEX128, DT_QINT8, DT_QUINT8, DT_QINT32. 

## Outputs

y: A Tensor. Has the same type as "x". 

## Attributes

N: An int that is >= 1. Defaults to "1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,string,uint8,uint16

## Attention Constraints

ParallelDynamicStitch runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator ParallelDynamicStitch.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
