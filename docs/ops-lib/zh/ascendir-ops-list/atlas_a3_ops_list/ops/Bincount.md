# Bincount

```c
REG_OP(Bincount)
    .INPUT(array, TensorType(DT_INT32))
    .INPUT(size, TensorType(DT_INT32))
    .INPUT(weights, TensorType({ DT_FLOAT, DT_INT32, DT_INT64, DT_DOUBLE }))
    .OUTPUT(bins, TensorType({ DT_FLOAT, DT_INT32, DT_INT64, DT_DOUBLE }))
    .OP_END_FACTORY_REG(Bincount)
```

## Brief

Counts the number of occurrences of each value in an integer array.
Outputs a vector with length size and the same dtype as weights. If weights
are empty, then index i stores the number of times the value i is counted in
arr. If weights are non-empty, then index i stores the sum of the value in
weights at each index.

## Inputs

The input size must be a non-negative int32 scalar Tensor. Inputs include:
- array:int32 Tensor.
- size:non-negative int32 scalar Tensor.
- weights: is an int32, int64, float32, or double Tensor with the same
shape as arr, or a length-0 Tensor, in which case it acts as all weights
equal to 1. 

## Outputs

bins:1D Tensor with length equal to size. The counts or summed weights for
each value in the range [0, size). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 array: int32
- input1 size: int32
- input2 weights: double,float32,int32,int64
- output0 bins: double,float32,int32,int64

## Third-party framework compatibility

Compatible with tensorflow Bincount operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
