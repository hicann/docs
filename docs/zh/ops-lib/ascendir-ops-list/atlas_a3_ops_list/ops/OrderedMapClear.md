# OrderedMapClear

```c
REG_OP(OrderedMapClear)
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(dtypes, ListType, {})
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(OrderedMapClear)
```

## Brief

Removes all elements in the underlying container. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to "0".
- memory_limit: An optional int that is >= 0. Defaults to "0".
- dtypes: An optional attribute. A list of DTypes.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".

## Attention Constraints

OrderedMapClear runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator OrderedMapClear.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
