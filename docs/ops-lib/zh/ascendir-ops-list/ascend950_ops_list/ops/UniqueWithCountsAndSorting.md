# UniqueWithCountsAndSorting

```c
REG_OP(UniqueWithCountsAndSorting)
    .INPUT(x, TensorType({BasicType(), DT_BF16}))
    .OUTPUT(y, TensorType({BasicType(), DT_BF16}))
    .OUTPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(counts, TensorType({DT_INT32, DT_INT64}))
    .ATTR(return_inverse, Bool, false)
    .ATTR(return_counts, Bool, false)
    .ATTR(sorted, Bool, true)
    .ATTR(out_idx, Type, DT_INT64)
    .OP_END_FACTORY_REG(UniqueWithCountsAndSorting)
```

## Brief

Return the unique elements of the input tensor with counts and sorted elements. 

## Inputs

x: A tensor. Input "x" is a k-dimensional tensor. 

## Outputs

- y: A Tensor. The output list of unique scalar elements. Has the same type as "x".
- indices: A tensor of type DT_INT32, DT_INT64.
             Representing the indices for where elements in the original input map to in the output.
- counts: A tensor of type DT_INT32, DT_INT64.
Representing the number of occurrences for each unique value or tensor. 

## Attributes

- return_inverse: An optional DType from: "bool". Defaults to False.
- return_counts: An optional DType from: "bool". Defaults to False.
- sorted: An optional DType from "bool". Defaults to True.
- out_idx: Output index/count's datatype. Defaults to DT_INT64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 indices: int32,int64
- output2 counts: int32,int64

## Third-party framework compatibility

Compatible with Pytorch operator _unique2.


---

[Back to Operator Specifications (Ascend950)](../README.md)
