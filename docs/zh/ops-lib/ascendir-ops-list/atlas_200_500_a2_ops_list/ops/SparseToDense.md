# SparseToDense

```c
REG_OP(SparseToDense)
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(output_shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_INT8,
                               DT_UINT8, DT_BOOL, DT_DOUBLE}))
    .INPUT(default_value, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_INT8,
                                      DT_UINT8, DT_BOOL, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_INT8, DT_UINT8,
                           DT_BOOL, DT_DOUBLE}))
    .ATTR(validate_indices, Bool, true)
    .OP_END_FACTORY_REG(SparseToDense)
```

## Brief

Converts a sparse representation into a dense tensor. 

## Inputs

Four inputs, including:
- indices: An ND Tensor of type int32 or int64. Dimension must be 0D, 1D or 2D.
Data between different rows(Corresponding index of output) cannot be duplicated, and should be sorted by ascending.
Index cannot exceed the size of each dimension of output.
- output_shape: A 1D Tensor has the same dtype of indices.
- values: A 1D Tensor, Values corresponding to each row of indices, or a scalar value to be used for all sparse
indices. 
Must be one of the following types: float32, float16, bfloat16, int16, uint16, int32, int64, int8, uint8, bool,
double.
- default_value: An ND Tensor of the same dtype as values .
Size must be 1.  

## Outputs

y: A Tensor. Has the same type and format as input "values" . 

## Attributes

- validate_indices: An optional bool.
If true, indices are checked to make sure they are sorted by ascending, no repeats, and cannot exceed the size of each
dimension.
This param is currently not effective in Ascend950PR/Ascend950DT. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int32,int64
- input1 output_shape: int32,int64
- input2 values: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input3 default_value: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
