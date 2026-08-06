# MapStage

```c
REG_OP(MapStage)
    .INPUT(key, TensorType({DT_INT64}))
    .INPUT(indices, TensorType({DT_INT32}))
    .DYNAMIC_INPUT(values,
        TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
        DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, DT_UINT32, \
        DT_UINT64, DT_RESOURCE, DT_STRING, DT_COMPLEX64, DT_COMPLEX128, \
        DT_QINT8, DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32 }))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(dtypes, ListType, {})
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(MapStage)
```

## Brief

Stage (key, values) in the underlying container which behaves like a hashtable. 

## Inputs

Including:
- key: A Tensor of type DT_INT64.
- indices: A Tensor of type DT_INT32.
- values: A list of Tensor objects for tensor dtypes.
A list of data types that inserted values should adhere to of.
Must be one of the following types: DT_FLOAT, DT_FLOAT16,
DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, DT_INT32,
DT_INT64, DT_BOOL, DT_DOUBLE, DT_UINT32, DT_UINT64,
DT_RESOURCE, DT_STRING, DT_COMPLEX64, DT_COMPLEX128,
DT_QINT8, DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32.
It's a dynamic input. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to "0".
Maximum number of elements in the Staging Area. If > 0,
inserts on the container will block when the capacity is reached.
- memory_limit: An optional int that is >= 0. Defaults to "0".
- dtypes: An optional attribute. A list of tf.DTypes.
- container: An optional string. Defaults to "".
If non-empty, this queue is placed in the given container.
Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "".
It is necessary to match this name to the matching Unstage Op. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 key: int64
- input1 indices: int32

## Attention Constraints

MapStage runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator MapStage.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
