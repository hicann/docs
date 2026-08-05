# Stage

```c
REG_OP(Stage)
    .DYNAMIC_INPUT(values, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, \
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, \
        DT_DOUBLE, DT_UINT32, DT_UINT64}))
    .ATTR(capacity, Int, 0)
    .ATTR(memory_limit, Int, 0)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(Stage)
```

## Brief

Stage values similar to a lightweight Enqueue. 

## Inputs

The input values must be a list of Tensor objects. Inputs include: 
values: A list of Tensor objects. Must be one of the following types:
float16, float, int8, int16, uint16, uint8, int32, int64, bool, double, uint32, uint64. 
A list of data types that inserted values should adhere to. It's a dynamic input. 

## Attributes

- capacity: An optional int that is >= 0. Defaults to 0. Maximum number of
elements in the Staging Area. If > 0, inserts on the container will block
when the capacity is reached.
- memory_limit: An optional int that is >= 0. Defaults to 0. The maximum
number of bytes allowed for Tensors in the Staging Area. If > 0, inserts will
block until sufficient space is available.
- container: An optional string. Defaults to "". If non-empty, this queue
is placed in the given container. Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "". It is necessary to
match this name to the matching Unstage Op. 
@see Unstage

## Third-party framework compatibility

Compatible with tensorflow Stage operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
