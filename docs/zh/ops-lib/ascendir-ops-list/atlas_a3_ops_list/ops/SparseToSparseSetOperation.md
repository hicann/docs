# SparseToSparseSetOperation

```c
REG_OP(SparseToSparseSetOperation)
    .INPUT(x1_indices, TensorType({DT_INT64}))
    .INPUT(x1_values, TensorType({DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, \
                                  DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(x1_shape, TensorType({DT_INT64}))
    .INPUT(x2_indices, TensorType({DT_INT64}))
    .INPUT(x2_values, TensorType({DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, \
                                  DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(x2_shape, TensorType({DT_INT64}))
    .OUTPUT(y_indices, TensorType({DT_INT64}))
    .OUTPUT(y_values, TensorType({DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, \
                                  DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(y_shape, TensorType({DT_INT64}))
    .ATTR(set_operation, String, "")
    .ATTR(validate_indices, Bool, true)
    .OP_END_FACTORY_REG(SparseToSparseSetOperation)
```

## Brief

Applies set operation along last dimension of 2 SparseTensor inputs. 

## Inputs

Inputs include:
- x1_indices: A Tensor of type int64. 2D Tensor, indices of a SparseTensor.
- x1_values: A Tensor. Must be one of the following types: int8, int16,
int32, int64, uint8, uint16, string. 1D Tensor, values of a SparseTensor.
- x1_shape: A Tensor of type int64. 1D Tensor, shape of a SparseTensor.
- x2_indices: A Tensor of type int64. 2D Tensor, indices of a SparseTensor.
- x2_values: A Tensor. Must have the same type as x1_values. 1D Tensor, values of a SparseTensor.
- x2_shape: A Tensor of type int64. 1D Tensor, shape of a SparseTensor.

## Outputs

- y_indices: A Tensor of type int64.
- y_values: A Tensor. Has the same type as x1_values.
- y_shape: A Tensor of type int64.

## Attributes

- set_operation: An optional string. Defaults to "".
- validate_indices: An optional bool. Defaults to True.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1_indices: int64
- input1 x1_values: int8,int16,int32,int64,string,uint8,uint16
- input2 x1_shape: int64
- input3 x2_indices: int64
- input4 x2_values: int8,int16,int32,int64,string,uint8,uint16
- input5 x2_shape: int64
- output0 y_indices: int64
- output1 y_values: int8,int16,int32,int64,string,uint8,uint16
- output2 y_shape: int64

## Attention Constraints

The implementation for SparseToSparseSetOperation on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow SparseToSparseSetOperation operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
