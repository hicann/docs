# OrderedMapUnstage

```c
REG_OP(OrderedMapUnstage)
    .INPUT(key, TensorType({DT_INT64}))
    .INPUT(indices, TensorType({DT_INT32}))
    .DYNAMIC_OUTPUT(values, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
                                        DT_INT32, DT_INT64, DT_FLOAT, DT_FLOAT16,
                                        DT_DOUBLE, DT_BOOL, DT_UINT32, DT_UINT64}))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(dtypes, ListType, {})
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(OrderedMapUnstage)
```

## Brief

Removes and returns the values associated with the key. 

## Inputs

Including:
- key: A Tensor of type DT_INT64.
- indices: A Tensor of type DT_INT32.

## Outputs

values: A list of Tensor objects. Must be one of the following types:
DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT,
DT_FLOAT16, DT_DOUBLE, DT_BOOL, DT_UINT32, DT_UINT64. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to "0".
- memory_limit: An optional int that is >= 0. Defaults to "0".
- dtypes: An optional attribute. A list of tf.DTypes that has length >= 1.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 key: int64
- input1 indices: int32

## Attention Constraints

OrderedMapUnstage runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator OrderedMapUnstage.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
