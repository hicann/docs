# SparseConcat

```c
REG_OP(SparseConcat)
    .DYNAMIC_INPUT(indices, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(values,
        TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
                    DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, \
                    DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .DYNAMIC_INPUT(shapes, TensorType({DT_INT64}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values,
        TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
                    DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, \
                    DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .OUTPUT(y_shape, TensorType({DT_INT64}))
    .ATTR(concat_dim, Int, 0)
    .ATTR(N, Int, 1)
    .OP_END_FACTORY_REG(SparseConcat)
```

## Brief

Concatenates a list of `SparseTensor` along the specified dimension.
Concatenation is with respect to the dense versions of these sparse tensors. 

## Inputs

- indices:A list of at least 2 `tensor` objects with type `int64`.2-D.
Indices of each input `SparseTensor`.It's a dynamic input.
- values:A list with the same length as `indices` of `tensor` objects with the same type.
It's a dynamic input.
- shapes:A list with the same length as `indices` of `tensor` objects with type `int64`.1-D.
Shapes of each `SparseTensor`. It's a dynamic input. 

## Outputs

- y_indices:A `tensor` of type `int64`.
- y_values:A `tensor`. Has the same type as `values`.
- y_shape:A `tensor` of type `int64`.

## Attributes

- concat_dim: An optional int. Dimension to concatenate along. Default is 0.
- N: An optional int. Number of sparse. Default is 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 y_indices: int64
- output1 y_values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- output2 y_shape: int64

## Third-party framework compatibility

Compatible SparseConcat operator in Tensorflow.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
