# RaggedTensorToTensor

```c
REG_OP(RaggedTensorToTensor)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(values, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
                          DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .INPUT(default_value, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16,
              DT_UINT16, DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .DYNAMIC_INPUT(row_partition_tensors, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(result, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
                          DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(num_row_partition_tensors, Int)
    .REQUIRED_ATTR(row_partition_types, ListString)
    .OP_END_FACTORY_REG(RaggedTensorToTensor)
```

## Brief

Create a dense tensor from a ragged tensor, possibly altering its shape. 

## Inputs

- shape:A `Tensor`. Must be one of the following types: `int64`, `int32`.
- values:A 1D tensor representing the values of the ragged tensor.
- default_value:A `Tensor`. Must have the same type as `values`.
- row_partition_tensors:A list of at least 1 `Tensor` objects with the same
type in: `int64`, `int32` . It's a dynamic input.

## Outputs

result: A `Tensor`. Has the same type as `values`.

## Attributes

- num_row_partition_tensors: An optional int that indicates the numbers of row partition tensors.
- row_partition_types: A list of `strings`.
The types of the row partition tensors. At present, these can be:
"ROW_SPLITS": the row_splits tensor from the ragged tensor.
"VALUE_ROWIDS": the value_rowids tensor from the ragged tensor.
"FIRST_DIM_SIZE": if value_rowids is used for the first dimension, then it
is preceeded by "FIRST_DIM_SIZE". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 values: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 default_value: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 result: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
