# MutableDenseHashTable

```c
REG_OP(MutableDenseHashTable)
    .INPUT(empty_key, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(deleted_key, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .ATTR(use_node_name_sharing, Bool, false)
    .REQUIRED_ATTR(value_dtype, Type)
    .ATTR(value_shape, ListInt, {})
    .ATTR(initial_num_buckets, Int, 131072)
    .ATTR(max_load_factor, Float, static_cast<float>(0.8))
    .OP_END_FACTORY_REG(MutableDenseHashTable)
```

## Brief

Creates an empty hash table that uses tensors as the backing store. 

## Inputs

The input deleted_key must have the same type as empty_key. Inputs include:
- empty_key: A Tensor. The key used to represent empty key buckets
internally. Must not be used in insert or lookup operations.
- deleted_key: A Tensor. Must have the same type as empty_key.

## Outputs

handle: A Tensor of type resource. Handle to the table. 

## Attributes

- container: An optional string. Defaults to "". If non-empty, this table
is placed in the given container. Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "". If non-empty, this
table is shared under the given name across multiple sessions.
- use_node_name_sharing: An optional bool. Defaults to False. If true and
shared_name is empty, the table is shared using the node name.
- value_dtype: A DType. Type of the table values.
- value_shape: An optional TensorShape or list of ints. Defaults to [].
The shape of each value.
- initial_num_buckets: An optional int. Defaults to 131072. The initial
number of hash table buckets. Must be a power to 2.
- max_load_factor: An optional float. Defaults to 0.8. The maximum ratio
between number of entries and number of buckets before growing the table.
Must be between 0 and 1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 empty_key: int32,int64,string
- input1 deleted_key: int32,int64,string
- output0 handle: resource

## Third-party framework compatibility.

Compatible with tensorflow MutableDenseHashTable operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
