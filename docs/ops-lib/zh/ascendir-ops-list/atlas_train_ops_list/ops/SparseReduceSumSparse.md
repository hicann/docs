# SparseReduceSumSparse

```c
REG_OP(SparseReduceSumSparse)
    .INPUT(x_indices, TensorType({DT_INT64}))
    .INPUT(x_values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x_shape, TensorType({DT_INT64}))
    .INPUT(reduction_axes, TensorType({DT_INT32}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y_shape, TensorType({DT_INT64}))
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(SparseReduceSumSparse)
```

## Brief

Computes the sum of elements across dimensions of a SparseTensor. 

## Inputs

4 inputs, including:
- x_indices: A 2D tensor of type int64.
"N x R" matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
- x_values: A 1D tensor. The values of the SparseTensor.
"N" non-empty values corresponding to "x_indices".
- x_shape: A 1D tensor of type int64. Shape of the input SparseTensor.
- reduction_axes: A 1D tensor of type int32.
A length-"K" vector containing the reduction axes. 

## Outputs

- y_indices: A tensor of type int64.
- y_values: A tensor. Has the same type as "x_values".
- y_shape: A tensor of type int64.

## Attributes

keep_dims: An optional bool. Defaults to "False".
If true, retains reduced dimensions with length 1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x_indices: int64
- input1 x_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 x_shape: int64
- input3 reduction_axes: int32
- output0 y_indices: int64
- output1 y_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output2 y_shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseReduceSumSparse.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
