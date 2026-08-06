# ParseExample

```c
REG_OP(ParseExample)
    .INPUT(serialized, TensorType({DT_STRING}))
    .INPUT(name, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(sparse_keys, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(dense_keys, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(dense_defaults, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .DYNAMIC_OUTPUT(sparse_indices, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(sparse_values, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .DYNAMIC_OUTPUT(sparse_shapes, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(dense_values, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .ATTR(Nsparse, Int, 0)
    .ATTR(Ndense, Int, 0)
    .ATTR(sparse_types, ListType, {})
    .ATTR(Tdense, ListType, {})
    .ATTR(dense_shapes, ListListInt, {})
    .OP_END_FACTORY_REG(ParseExample)
```

## Brief

Convert serialized tensorflow.TensorProto prototype to Tensor.
@brief Parse an Example prototype.

## Inputs

- serialized: A Tensor of type string.
- name:A Tensor of type string.
- sparse_keys: Dynamic input tensor of string.
- dense_keys: Dynamic input tensor of string
- dense_defaults:  Dynamic input tensor type as string, float, int64.

## Outputs

- sparse_indices: A Tensor of type int64.
- sparse_values:  Has the same type as sparse_types.
- sparse_shapes: A Tensor of type int64
- dense_values:  Has the same type as dense_defaults.

## Attributes

- Nsparse: An optional int. Defaults to 0. Number of sparse_keys, sparse_indices and sparse_shapes.
- Ndense: An optional int. Defaults to 0. Number of dense_keys.
- sparse_types: An optional attribute, types of sparse_values.
- Tdense: An optional attribute. Type of dense_defaults dense_defaults and dense_values.
- dense_shapes: An optional attribute that indicates output of dense_defaults shape.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 serialized: string
- input2 sparse_keys: string
- input3 dense_keys: string
- input4 dense_defaults: float32,int64,string

## Third-party framework compatibility 

- compatible with tensorflow StringToNumber operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
