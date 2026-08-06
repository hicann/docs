# DataFormatVecPermute

```c
REG_OP(DataFormatVecPermute)
    .INPUT(x, TensorType({ DT_INT32, DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_INT32, DT_INT64 }))
    .ATTR(src_format, String, "NHWC")
    .ATTR(dst_format, String, "NCHW")
    .OP_END_FACTORY_REG(DataFormatVecPermute)
```

## Brief

Returns the permuted vector/tensor in the destination data format given the .

## Inputs

Inputs include:
x: A Tensor. Must be one of the following types: int32, int64. Vector of size 4
or Tensor of shape (4, 2) in source data format . 

## Outputs

y: A Tensor. Has the same type as x . 

## Attributes

- src_format: An optional string. Defaults to "NHWC". source data format.
- dst_format: An optional string. Defaults to "NCHW". destination data format .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: int32,int64
- output0 y: int32,int64

## Attention Constraints

The implementation for DataFormatVecPermute on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow DataFormatVecPermute operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
