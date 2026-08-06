# UniqueConsecutive

```c
REG_OP(UniqueConsecutive)
    .INPUT(x, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .OUTPUT(idx, TensorType::IndexNumberType())
    .OUTPUT(count, TensorType::IndexNumberType())
    .ATTR(return_idx, Bool, false)
    .ATTR(return_counts, Bool, false)
    .ATTR(axis, Int, 1000)
    .ATTR(out_idx, Type, DT_INT64)
    .OP_END_FACTORY_REG(UniqueConsecutive)
```

## Brief

Finds the first unique element from every consecutive group of equivalent elements.

## Inputs

x: A ND tensor of BasicType, bool or bfloat16. 

## Outputs

- y: "x" in the unique output "y".Has the same type as "x" .
- idx: The index of each value of "x".
- count: The counts of each value of "y".

## Attributes

- return_idx: An optional bool. Whether to also return the indices. The default value is False. Currently only False is supported.
- return_count: An optional bool. Whether to also return the counts for each element. The default is False.
- axis: An optional int. Which one axis to apply unique. The default is 1000, which means None. Currently only 1000 is supported.
- out_idx: Output index/count's datatype. The default is DT_INT64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 idx: int32,int64
- output2 count: int32,int64

## Attention Constraints

UniqueConsecutive runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the PyTorch operator UniqueConsecutive.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
