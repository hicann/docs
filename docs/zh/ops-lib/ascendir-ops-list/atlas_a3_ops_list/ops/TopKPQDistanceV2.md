# TopKPQDistanceV2

```c
REG_OP(TopKPQDistanceV2)
    .INPUT(pq_distance, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(grouped_extreme_distance, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OUTPUT(topk_distance, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OUTPUT(topk_index, TensorType({DT_INT32}))
    .ATTR(order, String, "ASC")
    .REQUIRED_ATTR(k, Int)
    .REQUIRED_ATTR(group_size, Int)
    .OP_END_FACTORY_REG(TopKPQDistanceV2)
```

## Brief

Finds values and indices of the "k" largest or least elements for the last dimension. 

## Inputs

Two inputs, including:
- pq_distance: A Tensor, Will be updated after calculation. Must be one of the following types: float32, float16,
int32.
- grouped_extreme_distance: A Tensor, the extremum in each group. Must be one of the following types: float32,
float16, int32.

## Outputs

Two outputs, including:
- topk_distance: A Tensor, values of the "k" largest or least elements for the last dimension. Must be one of the
following types: float32, float16, int32.
- topk_index: A Tensor, indices of the "k" largest or least elements for the last dimension. dtype is int32.

## Attributes

- order: A string, indicates the sorting method, Must be one of the following string: "ASC" or "DES". default
is "ASC".
- k: Int, k maximum or minimum values, required.
- group_size: Int, the group size of the extremum, required.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 pq_distance: float16,float32,int32
- input1 grouped_extreme_distance: float16,float32,int32
- output0 topk_distance: float16,float32,int32
- output2 topk_index: int32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
