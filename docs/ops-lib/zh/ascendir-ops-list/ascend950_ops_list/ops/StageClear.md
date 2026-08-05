# StageClear

```c
REG_OP(StageClear)
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .ATTR(dtypes, ListType, {})
    .OP_END_FACTORY_REG(StageClear)
```

## Brief

Op removes all elements in the underlying container. 

## Attributes

- capacity: An optional int. A list of DTypes
- memory_limit: An optional int that is >= 0. Defaults to 0.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".
- dtypes: An optional attribute. A list of DTypes.
@see Stage

## Third-party framework compatibility

Compatible with tensorflow StageClear operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
