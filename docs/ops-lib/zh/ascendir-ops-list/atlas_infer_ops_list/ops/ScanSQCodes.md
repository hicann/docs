# ScanSQCodes

```c
REG_OP(ScanSQCodes)
    .INPUT(ivf, TensorType({DT_UINT8}))
    .INPUT(query, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(bucket_list, TensorType({DT_INT32, DT_INT64}))
    .INPUT(bucket_limits, TensorType({DT_INT32, DT_INT64}))
    .INPUT(bucket_offsets, TensorType({DT_INT32, DT_INT64}))
    .INPUT(vmin, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(vdiff, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(actual_count, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(sq_distance, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(grouped_extreme_distance, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(sq_ivf, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(sq_index, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(total_limit, Int)
    .ATTR(group_size, Int, 64)
    .ATTR(extreme_mode, Int, 0)
    .OP_END_FACTORY_REG(ScanSQCodes)
```

## Brief

Calculate SQ distance.

## Inputs

- ivf: A Tensor, dtype is uint8.
- query: A Tensor, dtype is float16 or float32.
- bucket_list: A Tensor, dtype is int32 or int64.
- bucket_limits: A Tensor, dtype is int32 or int64.
- bucket_offsets: A Tensor, dtype is int32 or int64.
- vmin: A Tensor, dtype is float16 or float32.
- vdiff: A Tensor, dtype is float16 or float32.

## Outputs

- actual_count: A Tensor, dtype is int32 or int64, the actual number of
sq_distance.
- sq_distance: A Tensor, dtype is float16 or float32.
- grouped_extreme_distance: A Tensor, dtype is float16 or float32, the
extremum in each group of sq_distance.
- sq_ivf: A Tensor, dtype is int32 or int64.
- sq_index: A Tensor, dtype is int32 or int64.

## Attributes

- total_limit: A required int, indicates the max length of the output
sq_distance.
- group_size: An optional int, indicates the group size of the extremum.
Defaults to 64.
- extreme_mode: A optional int, indicates the type of extremum, 0 means
minimum, and 1 means maximum. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 ivf: uint8
- input1 query: float16
- input2 bucket_list: int32
- input3 bucket_limits: int32
- input4 bucket_offsets: int64
- input5 vmin: float16
- input6 vdiff: float16
- output0 actual_count: int32
- output1 sq_distance: float16
- output2 grouped_extreme_distance: float16
- output3 sq_ivf: int32
- output4 sq_index: int32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
