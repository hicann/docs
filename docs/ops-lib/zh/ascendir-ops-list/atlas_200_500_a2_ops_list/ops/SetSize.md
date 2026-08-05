# SetSize

```c
REG_OP(SetSize)
    .INPUT(set_indices, TensorType({DT_INT64}))
    .INPUT(set_values, TensorType({DT_INT8, DT_INT16, \
        DT_UINT8, DT_UINT16, DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(set_shape, TensorType({DT_INT64}))
    .OUTPUT(size, TensorType({DT_INT32}))
    .ATTR(validate_indices, Bool, true)
    .OP_END_FACTORY_REG(SetSize)
```

## Brief

Number of unique elements along last dimension of input set. 

## Inputs

Inputs include:
- set_indices: A Tensor of type int64. 2D Tensor, indices of a SparseTensor.
- set_values: A Tensor. Must be one of the following types: int8, int16, int32, int64, uint8, uint16, string.
- set_shape: A Tensor of type int64. 1D Tensor, shape of a SparseTensor.

## Outputs

size: A Tensor of type int32. 

## Attributes

validate_indices: An optional bool. Defaults to True. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 set_indices: int64
- input1 set_values: int8,int16,int32,int64,string,uint8,uint16
- input2 set_shape: int64
- output0 size: int32

## Attention Constraints

The implementation for SetSize on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow SetSize operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
