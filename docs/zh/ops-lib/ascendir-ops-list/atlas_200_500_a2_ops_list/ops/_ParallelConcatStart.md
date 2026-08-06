# _ParallelConcatStart

```c
REG_OP(_ParallelConcatStart)
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, DT_UINT8,
                          DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE}))
    .ATTR(dtype, Type, DT_INT32)
    .ATTR(shape, ListInt, {})
    .OP_END_FACTORY_REG(_ParallelConcatStart)
```

## Brief

Create an empty tensor, using the shape and dtype specified in attributes. 

## Outputs

y: The empty constant tensor. 

## Attributes

- dtype: Specify the data type of the empty tensor.
- shape: Specify the shape of the empty tensor.

## Third-party framework compatibility

Compatible with the TensorFlow operator _ParallelConcatStart.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
