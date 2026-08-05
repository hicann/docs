# ParseSingleSequenceExample

```c
REG_OP(ParseSingleSequenceExample)
    .INPUT(serialized, TensorType({DT_STRING}))
    .INPUT(feature_list_dense_missing_assumed_empty, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(context_sparse_keys, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(context_dense_keys, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(feature_list_sparse_keys, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(feature_list_dense_keys, TensorType({DT_STRING}))
    .DYNAMIC_INPUT(context_dense_defaults, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .INPUT(debug_name, TensorType({DT_STRING}))
    .DYNAMIC_OUTPUT(context_sparse_indices, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(context_sparse_values, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .DYNAMIC_OUTPUT(context_sparse_shapes, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(context_dense_values, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .DYNAMIC_OUTPUT(feature_list_sparse_indices, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(feature_list_sparse_values, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .DYNAMIC_OUTPUT(feature_list_sparse_shapes, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(feature_list_dense_values, TensorType({DT_FLOAT, DT_INT64, DT_STRING}))
    .ATTR(Ncontext_sparse, Int, 0)
    .ATTR(Ncontext_dense, Int, 0)
    .ATTR(Nfeature_list_sparse, Int, 0)
    .ATTR(Nfeature_list_dense, Int, 0)
    .ATTR(context_sparse_types, ListType, {})
    .ATTR(Tcontext_dense, ListType, {})
    .ATTR(feature_list_dense_types, ListType, {})
    .ATTR(context_dense_shapes, ListListInt, {})
    .ATTR(feature_list_sparse_types, ListType, {})
    .ATTR(feature_list_dense_shapes, ListListInt, {})
    .OP_END_FACTORY_REG(ParseSingleSequenceExample)
```

## Brief

Transforms a scalar brain.SequenceExample proto (as strings) into typed
tensors.

## Inputs

- serialized: A Tensor of type string.
- feature_list_dense_missing_assumed_empty:A Tensor of type string.
- context_sparse_keys: Dynamic input tensor of string.
- context_dense_keys: Dynamic input tensor of string.
- feature_list_sparse_keys:  Dynamic input tensor of string.
- feature_list_dense_keys:  Dynamic input tensor of string.
- context_dense_defaults:  Dynamic input tensor of string, float, int64.
- debug_name: A Tensor of type string.

## Outputs

- context_sparse_indices: Dynamic output tensor of type int64.
- context_sparse_values:  Dynamic output tensor of type string, float, int64.
- context_sparse_shapes: Dynamic output tensor of type int64.
- context_dense_values:  Dynamic output tensor of type string, float, int64.
- feature_list_sparse_indices: Dynamic output tensor of type int64.
- feature_list_sparse_values:  Dynamic output tensor of type string, float, int64.
- feature_list_sparse_shapes: Dynamic output tensor of type int64.
- feature_list_dense_values:  Dynamic output tensor of type string, float, int64.

## Attributes

- Ncontext_sparse: An optional int, default is 0. Number of context_sparse_keys, context_sparse_indices and context_sparse_shapes.
- Ncontext_dense: An optional int, default is 0. Number of context_dense_keys.
- Nfeature_list_sparse: An optional int, default is 0. Number of feature_list_sparse_keys.
- Nfeature_list_dense: An optional int, default is 0. Number of feature_list_dense_keys.
- context_sparse_types: An optional attribute. Types of context_sparse_values.
- Tcontext_dense: An optional attribute. Number of dense_keys.
- feature_list_dense_types: An optional attribute. Types of feature_list_dense_values.
- context_dense_shapes: An optional attribute. Shape of context_dense.
- feature_list_sparse_types: An optional attribute. Type of feature_list_sparse_values.
- feature_list_dense_shapes: An optional attribute. Shape of feature_list_dense.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 serialized: string
- input1 feature_list_dense_missing_assumed_empty: string
- input2 context_sparse_keys: string
- input3 context_dense_keys: string
- input4 feature_list_sparse_keys: string
- input5 feature_list_dense_keys: string
- input6 context_dense_defaults: float32,int64,string
- input7 debug_name: string
- output0 context_sparse_indices: int64
- output1 context_sparse_values: float32,int64,string
- output2 context_sparse_shapes: int64
- output3 context_dense_values: float32,int64,string
- output4 feature_list_sparse_indices: int64
- output5 feature_list_sparse_values: float32,int64,string
- output6 feature_list_sparse_shapes: int64
- output7 feature_list_dense_values: float32,int64,string

## Third-party framework compatibility 

- compatible with tensorflow StringToNumber operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
