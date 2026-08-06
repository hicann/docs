# SyncBatchNormGatherStats

```c
REG_OP(SyncBatchNormGatherStats)
    .INPUT(total_sum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(total_square_sum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(sample_count, TensorType({DT_INT32}))
    .INPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(variance, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(batch_mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(batch_invstd, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(variance, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(momentum, Float, 0.1f)
    .ATTR(eps, Float, 0.00001f)
    .OP_END_FACTORY_REG(SyncBatchNormGatherStats)
```

## Brief

After the sum(total_sum) and the square sum(total_square_sum) are separately calculated on each device,
a total mean(batch_mean) and reciprocal of standard deviation(batch_invstd) are returned,
running_mean and running_var are updated.

## Inputs

include:
- total_sum: A 2-D tensor, that is, [N, C]. The sum of each device. The format must be ND.
Must be one of the following types: bfloat16, float16, float32.
- total_square_sum: A 2-D tensor, that is, [N, C]. The format must be ND. The square sum of each device.
Must be one of the following types: bfloat16, float16, float32. Has the same type, shape and format as "total_sum".
- sample_count: A 1-D tensor. Number of data for each device. The format must be ND.
Must be one of the following types: int32. The value of "sample_count" needs to be consistent with the N-axis value of "total_sum".
- mean: A 1-D tensor. Runtime mean. The format must be ND.
Must be one of the following types: bfloat16, float16, float32. The value of "mean" needs to be consistent with the C-axis value of "total_sum".
- variance: A 1-D tensor. Runtime variance. The format must be ND.
Must be one of the following types: bfloat16, float16, float32. Has the same type, shape and format as input "mean".
The value of "variance" needs to be consistent with the C-axis value of "total_sum". 

## Outputs

include:
- batch_mean: A 1-D tensor. Total mean of this batch.
Must be one of the following types: bfloat16, float16, float32. Has the same type, shape and format as input "mean".
- batch_invstd: A 1-D tensor. General statistics.
Must be one of the following types: bfloat16, float16, float32. Has the same type, shape and format as input "mean".
- mean: A 1-D tensor. Updated Runtime mean.
Must be one of the following types: bfloat16, float16, float32. Has the same type, shape and format as input "mean".
- variance: A 1-D tensor. Updated Runtime variance.
Must be one of the following types: bfloat16, float16, float32. Has the same type, shape and format as input "mean". 

## Attributes

Two Attributes, including:
- momentum: An optional float. Control the update speed of the moving average. Defaults to 0.1.
- eps: An optional float. A very small value to prevent division by zero. Defaults to 0.00001.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 total_sum: bfloat16,float16,float32
- input1 total_square_sum: bfloat16,float16,float32
- input2 sample_count: int32
- input3 mean: bfloat16,float16,float32
- input4 variance: bfloat16,float16,float32
- output0 batch_mean: bfloat16,float16,float32
- output1 batch_invstd: bfloat16,float16,float32
- output2 mean: bfloat16,float16,float32
- output3 variance: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
