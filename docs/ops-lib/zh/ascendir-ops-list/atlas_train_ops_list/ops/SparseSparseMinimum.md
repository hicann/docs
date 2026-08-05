# SparseSparseMinimum

```c
REG_OP(SparseSparseMinimum)
    .INPUT(x1_indices, TensorType({DT_INT64}))
    .INPUT(x1_values, TensorType({DT_INT64, DT_INT32, \
        DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, \
        DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x1_shape, TensorType({DT_INT64}))
    .INPUT(x2_indices, TensorType({DT_INT64}))
    .INPUT(x2_values, TensorType({DT_INT64, DT_INT32, \
        DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, \
        DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x2_shape, TensorType({DT_INT64}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values, TensorType({DT_INT64, DT_INT32, \
        DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, \
        DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(SparseSparseMinimum)
```

## Brief

Returns the element-wise min of two SparseTensors. 

## Inputs

6 inputs,contains:
- x1_indices:A `tensor` of type `int64`.2-D.
`N x R` matrix with the indices of non-empty values in a SparseTensor,
in the canonical lexicographic ordering.
- x1_values:A `tensor`. 1-D. the values of the sparse tensor.
- x1_shape:A `tensor` of type `int64`.1-D. the shape of the sparse tensor.
- x2_indices:A `tensor` of type `int64`.2-D. the indices of the sparse tensor.
- x2_values:A `tensor`. 1-D. Must have the same type as `x1_values`.
- x2_shape:A `tensor` of type `int64`.1-D.
counterpart to `a_shape` for the other operand; the two shapes must be equal. 

## Outputs

- y_indices:A `tensor` of type `int64`.
- y_values:A `tensor`. Has the same type as `x1_values`.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1_indices: int64
- input1 x1_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 x1_shape: int64
- input3 x2_indices: int64
- input4 x2_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input5 x2_shape: int64
- output0 y_indices: int64
- output1 y_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible SparseSparseMinimum operator in Tensorflow.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
