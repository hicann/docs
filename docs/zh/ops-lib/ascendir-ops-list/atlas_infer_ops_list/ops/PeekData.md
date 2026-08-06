# PeekData

```c
REG_OP(PeekData)
    .DYNAMIC_OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64,
                                   DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL}))
    .ATTR(output_types, ListType, {})
    .ATTR(output_shapes, ListListInt, {})
    .ATTR(channel_name, String, "")
    .OP_END_FACTORY_REG(PeekData)
```

## Brief

Get the batch of data in data processing. 

## Outputs

y: A nested structure of Tensor objects. Must be one of the types:int8, uint8, int16,
uint16, int32, int64, uint32, uint64, float16, float32, double, bool. 

## Attributes

- output_types: A nested structure of DType objects corresponding to each
component of an element of this dataset.
- output_shapes: A nested structure of TensorShape objects corresponding
to each component of an element of this dataset.
- channel_name: A string. Defaults to "".

## Third-party framework compatibility

Compatible with tensorflow GetNext operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
