# SyncBatchNormGatherStatsWithCounts

```c
REG_OP(SyncBatchNormGatherStatsWithCounts)
    .INPUT(mean_all, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(invert_std_all, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(count_all, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(mean_broadcast, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(count_sum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(running_var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(invert_std, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(running_var_update, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(momentum, Float, 0.1f)
    .ATTR(epsilon, Float, 0.001f)
    .OP_END_FACTORY_REG(SyncBatchNormGatherStatsWithCounts)
```

## Brief

After the mean and reciprocal of standard deviation(invert_std) are separately calculated on each device,
the mena and reciprocal of standard deviation(invert_std) data on each device are normlized,
a total mean and reciprocal of standard deviation(invert_std) are returned, and running_var are updated.

## Inputs

include:
- mean_all: A Tensor. The mean of each device. Must be one of the following types: float16, float32, bfloat16.
- invert_std_all: A Tensor. Reciprocal of the variances of each device. Must be one of the following types: float16, float32, bfloat16.
- count_all: A Tensor. Number of data for each device. Must be one of the following types: float16, float32, bfloat16.
- mean_broadcast: A Tensor. The overall average and broadcast. Must be one of the following types: float16, float32, bfloat16.
- count_sum: A Tensor. General statistics. Must be one of the following types: float16, float32, bfloat16.
- running_var: A Tensor. Runtime variance. Must be one of the following types: float16, float32, bfloat16.

## Outputs

include:
- invert_std: A Tensor. It's inverse of total variance. Must be one of the following types: float16, float32, bfloat16.
- running_var_update: A Tensor. It's moving variance of each device after the update. Must be one of the following types: float16, float32, bfloat16.

## Attributes

Two Attributes, including:
- momentum: An optional float. Defaults to 0.01.
- epsilon: An optional float. Defaults to 0.00001.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 mean_all: float16,float32
- input1 invert_std_all: float16,float32
- input2 count_all: float16,float32
- input3 mean_broadcast: float16,float32
- input4 count_sum: float16,float32
- input5 running_var: float16,float32
- output0 invert_std: float16,float32
- output1 running_var_update: float16,float32

## Third-party framework compatibility

ReduceMeanWithCount and SyncBatchNormGatherStatsWithCounts and SyncBNTrainingUpdate
compatible with the Pytorch operator BatchNormGatherStatsWithCounts.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
