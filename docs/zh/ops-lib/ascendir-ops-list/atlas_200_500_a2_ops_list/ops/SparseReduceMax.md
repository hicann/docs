# SparseReduceMax

```c
REG_OP(SparseReduceMax)
    .INPUT(x_indices, TensorType({DT_INT64}))
    .INPUT(x_values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .INPUT(x_shape, TensorType({DT_INT64}))
    .INPUT(reduction_axes, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
                           DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_DOUBLE}))
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(SparseReduceMax)
```

## Brief

Computes the max of elements across dimensions of a SparseTensor. 

## Inputs

4 inputs,contains:
- x_indices:A `tensor` of type `int64`.2-D.
`N x R` matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
- x_values:A `tensor`. 1-D. the values of the sparse tensor.
`N` non-empty values corresponding to `x_indices`.
- x_shape:A `tensor` of type `int64`.1-D.  Shape of the input SparseTensor.
- reduction_axes:A `tensor` of type `int32`.1-D.
Length-`K` vector containing the reduction axes. 

## Outputs

y:A `tensor`. Has the same type as `x_values`. 

## Attributes

keep_dims:An optional `bool`. Defaults to `False`.
If true, retain reduced dimensions with length 1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x_indices: int64
- input1 x_values: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 x_shape: int64
- input3 reduction_axes: int32
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible SparseReduceMax operator in Tensorflow.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
