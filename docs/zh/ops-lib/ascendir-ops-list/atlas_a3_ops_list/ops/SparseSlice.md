# SparseSlice

```c
REG_OP(SparseSlice)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT,
                               DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE, DT_BF16}))
    .INPUT(shape, TensorType({DT_INT64}))
    .INPUT(start, TensorType({DT_INT64}))
    .INPUT(size, TensorType({DT_INT64}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT,
                                  DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE, DT_BF16}))
    .OUTPUT(y_shape, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(SparseSlice)
```

## Brief

Slices a SparseTensor based on the "start" and "size". 

## Inputs

- indices: A 2D tensor of type int64. The indices of the SparseTensor.
It has shape [n, rank], where n is the number of input values, and rank is the dimension of value index.
The second dimension 'rank' supports 1 to 24(included).
- values: A 1D tensor. The values of the SparseTensor.
It has shape [n] which is the number all values. The supported datatypes are:
[DT_INT64, DT_INT32, DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
DT_COMPLEX64, DT_COMPLEX128, DT_BOOL, DT_STRING, DT_RESOURCE, DT_BF16].
- shape: A 1D tensor of type int64. It has shape [rank]. It is the shape of the SparseTensor.
- start: A 1D tensor of type int64. It has shape [rank]. It is the  start of the slice.
- size: A 1D tensor of type int64. It has shape [rank]. It is the size of the slice.

## Outputs

- y_indices: A tensor of type int64. The output indices of the SparseTensor after slicing.
It has shape [m, rank] where m is unknown, it depends on compute result.
- y_values: A tensor. Has the same type as "values". The values of the output SparseTensor after slicing.
It has shape [m] where m is unknown, it depends on compute result.
- y_shape: A tensor of type int64. It has shape [rank]. It is the shape of the output SparseTensor.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input2 shape: int64
- input3 start: int64
- input4 size: int64
- output0 y_indices: int64
- output1 y_values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- output2 y_shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseSlice.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
