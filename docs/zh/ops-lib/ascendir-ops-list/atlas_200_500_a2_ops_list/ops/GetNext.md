# GetNext

```c
REG_OP(GetNext)
    .DYNAMIC_OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64,
                                   DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL}))
    .ATTR(output_types, ListType, {})
    .ATTR(output_shapes, ListListInt, {})
    .ATTR(output_num, Int, 1)
    .ATTR(channel_name, String, "")
    .OP_END_FACTORY_REG(GetNext)
```

## Brief

Get the next batch of data in data processing.

## Outputs

y:A nested structure of Tensor objects.
Must be one of the following types: int8, uint8, int16, uint16, int32, int64, uint32, uint64, float16, float, double, bool. 

## Attributes

- output_types: An optional list. A nested structure of DType objects corresponding to each
component of an element of this dataset.
- output_shapes: An optional list list of int. A nested structure of TensorShape objects corresponding
to each component of an element of this dataset.
- output_num: An optional int that indicates the number of output. Defaults to 1.
- channel_name: An optional string. Defaults to "".

## Third-party framework compatibility

Compatible with tensorflow GetNext operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
