# SparseSplit

```c
REG_OP(SparseSplit)
    .INPUT(split_dim, TensorType({DT_INT64}))
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16, \
        DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, \
        DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE}))
    .INPUT(shape, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(y_indices, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(y_values, TensorType({DT_INT64, DT_INT32, DT_UINT16, \
        DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE}))
    .DYNAMIC_OUTPUT(y_shape, TensorType({DT_INT64}))
    .ATTR(num_split, Int, 1)
    .OP_END_FACTORY_REG(SparseSplit)
```

## Brief

Splits a SparseTensor into "num_split" tensors along one dimension. 

## Inputs

4 inputs, including:
- split_dim: A 0D tensor of type int64.
The dimension along which to split. Must be in the range "[0, rank(shape))".
- indices: A 2D tensor of type int64.
The indices of the SparseTensor.
- values: A 1D tensor. The values of the SparseTensor.
- shape: A 1D tensor of type int64. Shape of the SparseTensor.

## Outputs

- y_indices: A list of "num_split" tensor objects of type int64.
- y_values: A list of "num_split" tensor objects with the same type as "values".
- y_shape: A list of "num_split" tensor objects of type int64.

## Attributes

num_split: An int that is >= 1. The number of ways to split. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 split_dim: int64
- input1 indices: int64
- input2 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input3 shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseSplit.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
