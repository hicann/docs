# UnravelIndex

```c
REG_OP(UnravelIndex)
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(dims, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(UnravelIndex)
```

## Brief

Converts an array of flat indices into a tuple of coordinate arrays. 

## Inputs

Input "indices" is a 0D or 1D tensor. Input "dims" is a 1D tensor.
- indices: A 0D or 1D int Tensor whose elements are indices into
the flattened version of an array of dimensions "dims".
- dims: A 1D int Tensor of the same type as "indices".
The shape of the array to use for unraveling indices. 

## Outputs

y: A Tensor. Has the same type as "indices". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int32,int64
- input1 dims: int32,int64
- output0 y: int32,int64

## Attention Constraints

UnravelIndex runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator UnravelIndex.


---

[Back to Operator Specifications (Ascend950)](../README.md)
