# StageSize

```c
REG_OP(StageSize)
    .OUTPUT(size, TensorType({DT_INT32}))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .ATTR(dtypes, ListType, {})
    .OP_END_FACTORY_REG(StageSize)
```

## Brief

Op returns the number of elements in the underlying container. 

## Outputs

size:A Tensor of type int32. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to 0.
- memory_limit: An optional int that is >= 0. Defaults to 0.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".
- dtypes: An optional attribute. A list of DTypes that has length >= 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 size: int32

## Third-party framework compatibility

Compatible with tensorflow StageSize operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
