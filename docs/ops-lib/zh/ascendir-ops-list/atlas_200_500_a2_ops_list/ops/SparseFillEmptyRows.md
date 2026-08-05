# SparseFillEmptyRows

```c
REG_OP(SparseFillEmptyRows)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_BOOL, DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16,
                               DT_INT32, DT_INT64, DT_INT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8}))
    .INPUT(dense_shape, TensorType({DT_INT64}))
    .INPUT(default_value, TensorType({DT_BOOL, DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16,
                                      DT_INT32, DT_INT64, DT_INT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values, TensorType({DT_BOOL, DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16,
                                  DT_INT32, DT_INT64, DT_INT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8}))
    .OUTPUT(empty_row_indicator, TensorType({DT_BOOL}))
    .OUTPUT(reverse_index_map, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(SparseFillEmptyRows)
```

## Brief

Fills empty rows in a sparse tensor.

## Inputs

- indices: A 2D tensor of type int64. Each row stores one sparse element
index.
- values: A 1D tensor. The value of each sparse element.
- dense_shape: A 1D tensor of type int64. The dense shape of the sparse
tensor.
- default_value: A scalar tensor. The value used to fill empty rows.

## Outputs

- y_indices: A 2D tensor of type int64. The output sparse indices.
- y_values: A 1D tensor. Has the same type as values.
- empty_row_indicator: A 1D tensor of type bool. True indicates the
corresponding row was empty.
- reverse_index_map: A 1D tensor of type int64. Maps original input values
to output positions.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input2 dense_shape: int64
- input3 default_value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y_indices: int64
- output1 y_values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output2 empty_row_indicator: bool
- output3 reverse_index_map: int64


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
