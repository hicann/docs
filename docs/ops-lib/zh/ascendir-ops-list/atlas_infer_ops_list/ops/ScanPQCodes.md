# ScanPQCodes

```c
REG_OP(ScanPQCodes)
    .INPUT(ivf, TensorType({DT_UINT8}))
    .INPUT(bucket_list, TensorType({DT_INT32, DT_INT64}))
    .INPUT(bucket_base_distance, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(bucket_limits, TensorType({DT_INT32}))
    .INPUT(bucket_offsets, TensorType({DT_INT64}))
    .INPUT(adc_tables, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(actual_count, TensorType({DT_INT32}))
    .OUTPUT(pq_distance, TensorType({DT_FLOAT16}))
    .OUTPUT(grouped_extreme_distance, TensorType({DT_FLOAT16}))
    .OUTPUT(pq_ivf, TensorType({DT_INT32}))
    .OUTPUT(pq_index, TensorType({DT_INT32}))
    .REQUIRED_ATTR(total_limit, Int)
    .ATTR(group_size, Int, 64)
    .ATTR(extreme_mode, Int, 0)
    .ATTR(split_count, Int, 1)
    .ATTR(split_index, Int, 0)
    .OP_END_FACTORY_REG(ScanPQCodes)
```

## Brief

Calculate PQ distance. 

## Inputs

Six inputs, including:
- ivf: A Tensor, dtype is uint8.
- bucket_list: A Tensor, dtype is int32, int64.
- bucket_base_distance: A Tensor, dtype is float16, float32.
- bucket_limits: A Tensor, dtype is int32.
- bucket_offsets: A Tensor, dtype is int64.
- adc_tables: A Tensor. dtype is float16, float32.

## Outputs

Five outputs, including:
- actual_count: A Tensor, dtype is int32, the first element means the length of processed ivf.
- pq_distance: A Tensor, dtype is float16.
- grouped_extreme_distance: A Tensor, dtype is float16.
- pq_ivf: A Tensor, dtype is int32.
- pq_index: A Tensor, dtype is int32.

## Attributes

Five attributes, including:
- group_size: A Scalar, indicates the group size when compute grouped_extreme_distance.
- total_limit: A Scalar, indicates the total length of the outputs.
- extreme_mode: A Scalar, indicates the type of extremum, 0 means minimum, and 1 means maximum.
- split_count: A Scalar.
- split_index: A Scalar.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 ivf: uint8
- input1 bucket_list: int32,int64
- input2 bucket_base_distance: float16
- input3 bucket_limits: int32
- input4 bucket_offsets: int64
- input5 adc_tables: float16
- output0 actual_count: int32
- output1 pq_distance: float16
- output2 grouped_extreme_distance: float16
- output3 pq_ivf: int32
- output4 pq_index: int32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
