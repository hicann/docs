# MapUnstage

```c
REG_OP(MapUnstage)
    .INPUT(key, TensorType({DT_INT64}))
    .INPUT(indices, TensorType({DT_INT32}))
    .DYNAMIC_OUTPUT(values,
        TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
        DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, DT_UINT32, \
        DT_UINT64, DT_RESOURCE, DT_STRING, DT_COMPLEX64, DT_COMPLEX128, \
        DT_QINT8, DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32 }))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(dtypes, ListType, {})
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(MapUnstage)
```

## Brief

Removes and returns the values associated with the key. 

## Inputs

Including:
- key: A Tensor of type DT_INT64.
- indices: A Tensor of type DT_INT32.

## Outputs

values: A list of Tensor objects. Must be one of the following types:
DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, DT_INT32,
DT_INT64, DT_BOOL, DT_DOUBLE, DT_UINT32, DT_UINT64, DT_RESOURCE,
DT_STRING, DT_COMPLEX64, DT_COMPLEX128, DT_QINT8, DT_QUINT8,
DT_QINT16, DT_QUINT16, DT_QINT32. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to "0".
- memory_limit: An optional int that is >= 0. Defaults to "0".
- dtypes: An optional attribute. A list of DTypes that has length >= 1.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 key: int64
- input1 indices: int32

## Attention Constraints

MapUnstage runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator MapUnstage.


---

[Back to Operator Specifications (Ascend950)](../README.md)
