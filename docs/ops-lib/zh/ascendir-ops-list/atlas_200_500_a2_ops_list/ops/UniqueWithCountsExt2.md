# UniqueWithCountsExt2

```c
REG_OP(UniqueWithCountsExt2)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16, DT_INT8,
    DT_COMPLEX64, DT_INT64, DT_QINT8, DT_QUINT8, DT_QINT32, DT_QINT16, DT_QUINT16,
    DT_UINT16, DT_COMPLEX128, DT_FLOAT16, DT_UINT32, DT_UINT64, DT_BOOL, DT_BF16}))
    .INPUT(axis, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16, DT_INT8,
    DT_COMPLEX64, DT_INT64, DT_QINT8, DT_QUINT8, DT_QINT32, DT_QINT16, DT_QUINT16,
    DT_UINT16, DT_COMPLEX128, DT_FLOAT16, DT_UINT32, DT_UINT64, DT_BOOL, DT_BF16}))
    .OUTPUT(idx, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(count, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(inverse_idx, TensorType({DT_INT32, DT_INT64}))
    .ATTR(out_idx, Type, DT_INT64)
    .ATTR(sorted, Bool, false)
    .ATTR(return_inverse, Bool, false)
    .OP_END_FACTORY_REG(UniqueWithCountsExt2)
```

## Brief

Finds unique elements in a 1D tensor. 

## Inputs

Inputs "x" and "axis" are 1D vectors.
- x: A 1D tensor.
- axis: A 1D tensor.

## Outputs

- y: "x" in the unique output "y".
- idx: Contains the index of the "y" element that first appears in "x".
- count: Contains the count of each element of the "y" in the input "x".
- inverse_idx: For an element of "x", contain its corresponding index in "y".

## Attributes

- out_idx: An optional DType from: "int32, int64". Defaults to "int64".
- sorted: An optional DType from "bool". Defaults to False.
- return_inverse: An optional DType from: "bool". Defaults to False.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 axis: int32,int64
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 idx: int32,int64
- output2 count: int32,int64
- output3 inverse_idx: int32,int64

## Attention Constraints

UniqueWithCountsExt2 runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator UniqueWithCountsExt2.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
