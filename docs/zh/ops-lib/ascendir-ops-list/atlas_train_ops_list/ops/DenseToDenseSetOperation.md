# DenseToDenseSetOperation

```c
REG_OP(DenseToDenseSetOperation)
  .INPUT(x1, TensorType({DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, \
                         DT_INT32, DT_INT64, DT_STRING}))
  .INPUT(x2, TensorType({DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, \
                         DT_INT32, DT_INT64, DT_STRING}))
  .OUTPUT(y_indices, TensorType({DT_INT64}))
  .OUTPUT(y_values, TensorType({DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, \
                                DT_INT32, DT_INT64, DT_STRING}))
  .OUTPUT(y_shape, TensorType({DT_INT64}))
  .ATTR(set_operation, String, "")
  .ATTR(validate_indices, Bool, true)
  .OP_END_FACTORY_REG(DenseToDenseSetOperation)
```

## Brief

Applies set operation along last dimension of 2 Tensor inputs. 

## Inputs

Inputs include:
- x1: A Tensor. Must be one of the following types: int8, int16, int32, int64, uint8, uint16, string.
- x2: A Tensor. Must have the same type as x1.

## Outputs

- y_indices: A Tensor of type int64.
- y_values: A Tensor. Has the same type as x1.
- y_shape: A Tensor of type int64.

## Attributes

- set_operation: An optional string. Defaults to "".
- validate_indices: An optional bool. Defaults to True.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: int8,int16,int32,int64,string,uint8,uint16
- input1 x2: int8,int16,int32,int64,string,uint8,uint16
- output0 y_indices: int64
- output1 y_values: int8,int16,int32,int64,string,uint8,uint16
- output2 y_shape: int64

## Attention Constraints

The implementation for DenseToDenseSetOperation on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow DenseToDenseSetOperation operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
