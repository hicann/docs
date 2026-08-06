# GroupNormV2

```c
REG_OP(GroupNormV2)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mean, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(rstd, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(data_format, String, "NHWC")
    .ATTR(eps, Float, 0.00001f)
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(GroupNormV2)
```

## Brief

Performs group normalization . 

## Inputs

Three inputs
- x: A ND tensor of type bfloat16, float16, float32. The input feature map will be processed by group normalization.
"x" supports 2-8 dimensions (N, C, *), the calculation logic only cares about the first two dimensions (N and C),
and the rest can all be combined into one dimension.
The data type and shape of x must meet the following conditions:
- When the data type of x is float32, C/num_groups must be a multiple of 8.
- When the data type of x is float16 or bfloat16, C/num_groups must be a multiple of 16.
- gamma: A ND tensor of type bfloat16, float16, float32. Must be 1D. Specifies the scaling factor.
The value of "gamma" needs to be consistent with the C-axis value of "x". Has the same dype as "x".
- beta: A ND tensor of type bfloat16, float16, float32. Must be 1D. Specifies the offset.
The value of "beta" needs to be consistent with the C-axis value of "x". Has the same dype as "x". 

## Outputs

Three outputs
- y: A ND tensor of type bfloat16, float16, float32 for the normalized "x". Has the same type, format and shape as "x".
- mean: A ND tensor of type bfloat16, float16, float32. Must be 2D (N, num_groups). Specifies the mean of "x".
Has the same dype as "x".
- rstd: A ND tensor of type bfloat16, float16, float32. Must be 2D (N, num_groups). Specifies the rstd of "x".
Has the same dype as "x". 

## Attributes

- num_groups: An required int32, specifying the number of group.
- eps: An optional float32, specifying the small value added to variance to avoid dividing by zero. Defaults to "0.00001".
- data_format: An optional string, specifying the format of "x". Defaults to "NHWC". This parameter is reserved and does not take effect.
- is_training: An optional bool, specifying if the operation is used for training or inference. Defaults to "True".
- When set to true, it indicates training mode and uses the mean and variance of the current batch.
- When set to false, it indicates inference mode and uses the mean and variance saved during training. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 gamma: float16,float32
- input2 beta: float16,float32
- output0 y: float16,float32
- output1 mean: float16,float32

## Third-party framework compatibility

- Compatible with the PyTorch operator GroupNorm.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
