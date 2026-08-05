# SparseAdd

```c
REG_OP(SparseAdd)
    .INPUT(x1_indices, TensorType({DT_INT64}))
    .INPUT(x1_values, TensorType({DT_FLOAT, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x1_shape, TensorType({DT_INT64}))
    .INPUT(x2_indices, TensorType({DT_INT64}))
    .INPUT(x2_values, TensorType({DT_FLOAT, DT_INT8, DT_INT16, DT_INT32, \
        DT_INT64, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x2_shape, TensorType({DT_INT64}))
    .INPUT(thresh, TensorType({DT_FLOAT, DT_INT8, DT_INT16, DT_INT32, \
        DT_INT64, DT_DOUBLE}))
    .OUTPUT(sum_indices, TensorType({DT_INT64}))
    .OUTPUT(sum_values, TensorType({DT_FLOAT, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(sum_shape, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(SparseAdd)
```

## Brief

Adds two `SparseTensor` objects to produce another `SparseTensor`. 

## Inputs

7 inputs, contains:
- x1_indices:A `tensor` of type `int64`.2-D.
The `indices` of the first `SparseTensor`, size `[nnz, ndims]` Matrix.
- x1_values:A `tensor`. Must be one of the following types:float,int8,int16,int32,int64, float64, complex64, complex128.
- x1_shape:A `tensor` of type `int64`.1-D. The `shape` of the first `SparseTensor`,
size `[ndims]` Vector.
- x2_indices:A `tensor` of type `int64`.2-D.The `indices` of the second `SparseTensor`,
size `[nnz, ndims]` Matrix.
- x2_values:A `tensor`. Must have the same type as `x1_values`.1-D.
The `values` of the second `SparseTensor`, size `[nnz]` Vector.
- x2_shape:A `tensor` of type `int64`.1-D.
The `shape` of the second `SparseTensor`, size `[ndims]` Vector.
- thresh:A `tensor` 0-D.The magnitude threshold that determines if an output value/index pair takes space .

## Outputs

- sum_indices:A `tensor` of type `int64`.
- sum_values:A `tensor`. Has the same type as `x1_values`.
- sum_shape:A `tensor` of type `int64` .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1_indices: int64
- input1 x1_values: complex64,complex128,double,float32,int8,int16,int32,int64
- input2 x1_shape: int64
- input3 x2_indices: int64
- input4 x2_values: complex64,complex128,double,float32,int8,int16,int32,int64
- input5 x2_shape: int64
- input6 thresh: double,float32,int8,int16,int32,int64
- output0 sum_indices: int64
- output1 sum_values: complex64,complex128,double,float32,int8,int16,int32,int64
- output2 sum_shape: int64

## Third-party framework compatibility

Compatible SparseAdd operator in Tensorflow.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
