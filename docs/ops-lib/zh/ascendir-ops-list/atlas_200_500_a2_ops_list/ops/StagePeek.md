# StagePeek

```c
REG_OP(StagePeek)
    .INPUT(index, TensorType({DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT16, \
                    DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, \
                    DT_DOUBLE, DT_UINT32, DT_UINT64}))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .ATTR(dtypes, ListType, {})
    .OP_END_FACTORY_REG(StagePeek)
```

## Brief

Op peeks at the values at the specified index. If the underlying
container does not contain sufficient elements this op will block until it does. 

## Inputs

The input values must be type int32. Inputs include:
index: A Tensor of type int32. 

## Outputs

y: A list of Tensor objects. Must be one of the following types:
float16, float, int8, int16, uint16, uint8, int32, int64, bool, double, uint32, uint64. 
It's a dynamic output. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to 0.
- memory_limit: An optional int that is >= 0. Defaults to 0.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".
- dtypes: An optional attribute. A list of DTypes that has length >= 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 index: int32

## Third-party framework compatibility

Compatible with tensorflow StagePeek operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
