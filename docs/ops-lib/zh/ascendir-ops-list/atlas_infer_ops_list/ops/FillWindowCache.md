# FillWindowCache

```c
REG_OP(FillWindowCache)
    .INPUT(x, TensorType::BasicType())
    .INPUT(clean_cache, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(axis, Int)
    .REQUIRED_ATTR(cache_depth, Int)
    .OP_END_FACTORY_REG(FillWindowCache)
```

## Brief

Step the original data block of y forward one by one,
discard the first data block, and then update x to the last data block of y. 

## Inputs

- x: A Tensor, A tensor that stores updated data.
       Must be one of the following types:
       int8, uint8, int16, uint16, int32, uint32, int64, uint64, float16, float, bfloat16
       double, complex64, complex128, qint8, qint16, qint32, quint8, quint16.
- clean_cache: A Bool, Indicates whether to reset y to zero first.

## Outputs

- y: The updated tensor. Dtype is same as x.

## Attributes

- axis: A int, dtype is int64. Specify which dimension to start updating elements from.
- cache_depth: A int, dtype is int64. Specify the depth of data caching.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
