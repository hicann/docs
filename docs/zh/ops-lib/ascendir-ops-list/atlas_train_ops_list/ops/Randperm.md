# Randperm

```c
REG_OP(Randperm)
    .OUTPUT(out, TensorType({DT_INT64, DT_INT32, DT_INT16,
        DT_UINT8, DT_INT8, DT_FLOAT16, DT_FLOAT32, DT_DOUBLE}))
    .REQUIRED_ATTR(n, Int)
    .ATTR(layout, Int, 0)
    .ATTR(dtype, Type, DT_INT64)
    .OP_END_FACTORY_REG(Randperm)
```

## Brief

Returns the random permutation of integers from 0 to n-1. 

## Outputs

out: A required Tensor. Must be one of the following types:
float16, float32, float32, int8, uint8, int16, int32, int64. 

## Attributes

- n: An required int.
- dtype: An optional str. Defaults to int64 .
- layout: An optional int. Defaults to 0 .

## Attention Constraints

The implementation for Randperm on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with Pytorch Randperm operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
