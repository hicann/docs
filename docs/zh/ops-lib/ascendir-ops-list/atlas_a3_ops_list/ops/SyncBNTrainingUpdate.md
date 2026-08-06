# SyncBNTrainingUpdate

```c
REG_OP(SyncBNTrainingUpdate)
    .INPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(running_mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(running_mean_update, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(momentum, Float, 0.1f)
    .OP_END_FACTORY_REG(SyncBNTrainingUpdate)
```

## Brief

update running_mean.

## Inputs

include:
- mean: A Tensor. The mean of each device. Must be one of the following types: float16, float32, bfloat16.
- running_mean: A Tensor. Runtime Mean. Must be one of the following types: float16, float32, bfloat16.

## Outputs

include:
- running_mean_update: A Tensor. It's moving mean of each device after the update. Must be one of the following types: float16, float32, bfloat16.

## Attributes

One Attribute, including:
- momentum: A optional float. Defaults to 0.01.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 mean: bfloat16,float16,float32
- input1 running_mean: bfloat16,float16,float32
- output0 running_mean_update: bfloat16,float16,float32

## Third-party framework compatibility

ReduceMeanWithCount and SyncBatchNormGatherStatsWithCounts and SyncBNTrainingUpdate
compatible with the Pytorch operator BatchNormGatherStatsWithCounts.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
