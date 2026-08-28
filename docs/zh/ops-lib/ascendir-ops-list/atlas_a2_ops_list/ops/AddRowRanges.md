# AddRowRanges

```c
REG_OP(AddRowRanges)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(src, TensorType({DT_FLOAT}))
    .INPUT(indices, TensorType({DT_INT32}))
    .OUTPUT(x, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(AddRowRanges)
```

## Brief

For each row r of this and for each column c, do (* this)(r, c) += src(j, c), 
  where j ranges from indexes[r].first through indexes[r].second - 1. 
  In general indexes must be >= 0 and < src.NumRows(); 
  but to represent an empty range you may use the pair (-1, -1) or any pair of numbers (i, j) such that i >= j. 

## Inputs

Three inputs, including:
- x: A Tensor, type should be float32.
- indices: A Tensor of the indices, type should be int32.
- src: A Tensor of the same type as "x".

## Outputs

x: A Tensor with the same type and shape of input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 src: float32
- input2 indices: int32
- output0 x: float32

## Third-party framework compatibility

Compatible with the kaldi operator AddRowRanges.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
