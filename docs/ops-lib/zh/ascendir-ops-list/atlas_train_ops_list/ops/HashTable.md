# HashTable

```c
REG_OP(HashTable)
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .ATTR(use_node_name_sharing, Bool, false)
    .REQUIRED_ATTR(key_dtype, Type)
    .REQUIRED_ATTR(value_dtype, Type)
    .OP_END_FACTORY_REG(HashTable)
```

## Brief

Creates a non-initialized hash table . 

## Outputs

handle: A Tensor of type resource. Handle to the table . 

## Attributes

- container: An optional string. Defaults to "". If non-empty, this table
is placed in the given container. Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "". If non-empty, this
table is shared under the given name across multiple sessions.
- use_node_name_sharing: An optional bool. Defaults to False. If true and
shared_name is empty, the table is shared using the node name.
- key_dtype: A DType. Type of the table keys.
- value_dtype: A DType. Type of the table values .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource

## Attention Constraints

The implementation for HashTable on Ascend uses ai cpu, with bad performance.

## Third-party framework compatibility.

Compatible with tensorflow HashTable operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
