# FusedBatchNormV2

```c
REG_OP(FusedBatchNormV2)
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(offset, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(mean, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(variance, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(batch_mean, TensorType({DT_FLOAT}))
    .OUTPUT(batch_variance, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_1, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_2, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.0001f)
    .ATTR(data_format, String, "NHWC")
    .ATTR(is_training, Bool, true)
    .ATTR(exponential_avg_factor, Float, 1.0)
    .OP_END_FACTORY_REG(FusedBatchNormV2)
```

## Brief

Performs batch normalization . 

## Inputs

Five inputs, including: (NHWC, NCHW supported)
- x: A 4D or 5D Tensor of type float16 or float32, with format NHWC or NCHW for 4D.
- scale: A Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the scaling factor.
- offset: A Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the offset.
- mean: A Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the mean used for inference. Must be "None" if the
operation is used for training.
- variance: A Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the variance used for inference. Must be "None"
if the operation is used for training . 

## Outputs

Five outputs, including: (NHWC, NCHW supported)
- y: A 4D or 5D Tensor of type float16 or float32 for the normalized "x", with format NHWC or NCHW for 4D.
- batch_mean: A Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the mean of "x".
- batch_variance: A Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
pecifies the variance of "x".
- reserve_space_1: An optional Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the mean of "x" for gradient computation. Pass "None" to skip this output.
- reserve_space_2: An optional Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the variance of "x" for gradient computation. Pass "None" to skip this output . 

## Attributes

- epsilon: An optional float32, specifying the small value added to variance to avoid dividing by zero. Defaults to "0.0001".
- data_format: An optional string, specifying the format of "x". Defaults to "NHWC".
- is_training: An optional bool, specifying if the operation is used for training or inference. Defaults to "True".
- exponential_avg_factor: An optional float, default is 1.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float32
- input1 scale: float32
- input3 mean: float32
- input4 variance: float32
- output0 y: float32

## Attention Constraints

- If the operation is used for inference and outputs "reserve_space_1" and "reserve_space_2" are available,
then "reserve_space_1" has the same value as "mean" and "reserve_space_2" has the same value as "variance".
- For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 1‰ due to the square root instruction .


---

[Back to Operator Specifications (Ascend950)](../README.md)
