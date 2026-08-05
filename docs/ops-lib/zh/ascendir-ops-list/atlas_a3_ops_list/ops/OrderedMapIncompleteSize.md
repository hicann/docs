# OrderedMapIncompleteSize

```c
REG_OP(OrderedMapIncompleteSize)
    .OUTPUT(size, TensorType({DT_INT32}))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(dtypes, ListType, {})
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(OrderedMapIncompleteSize)
```

## Brief

Returns the number of incomplete elements in the underlying container. 

## Outputs

size: A Tensor of type DT_INT32. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to "0".
- memory_limit: An optional int that is >= 0. Defaults to "0".
- dtypes: An optional attribute. A list of DTypes.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 size: int32

## Attention Constraints

OrderedMapIncompleteSize runs on the Ascend AI CPU,
which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator OrderedMapIncompleteSize.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
