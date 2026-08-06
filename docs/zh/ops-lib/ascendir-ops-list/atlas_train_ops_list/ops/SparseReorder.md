# SparseReorder

```c
REG_OP(SparseReorder)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .INPUT(shape, TensorType({DT_INT64}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .OP_END_FACTORY_REG(SparseReorder)
```

## Brief

Reorders a SparseTensor into the canonical, row-major ordering. 

## Inputs

- indices: A matrix tensor of type int64. 2D. The indices of the SparseTensor.
- values: Values of the SparseTensor. A vector tensor. 1D.
- shape: A vector tensor of type int64. 1D. The shape of the SparseTensor.

## Outputs

- y_indices: The indices of the SparseTensor. Has the same type as "indices".
- y_values: The values of the SparseTensorr. Has the same type as "values".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input2 shape: int64
- output0 y_indices: int64
- output1 y_values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseReorder.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
