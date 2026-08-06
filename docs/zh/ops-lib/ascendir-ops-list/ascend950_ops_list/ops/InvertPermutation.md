# InvertPermutation

```c
REG_OP(InvertPermutation)
    .INPUT(x, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(InvertPermutation)
```

## Brief

Computes the inverse permutation of a tensor. 

## Inputs

x: A k-dimensional tensor. 

## Outputs

y: A 1D tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: int32,int64
- output0 y: int32,int64

## Attention Constraints

InvertPermutation runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator InvertPermutation.


---

[Back to Operator Specifications (Ascend950)](../README.md)
