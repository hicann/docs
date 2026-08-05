# BatchNorm3D

```c
REG_OP(BatchNorm3D)
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
    .ATTR(data_format, String, "NCDHW")
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(BatchNorm3D)
```

## Brief

Performs batch normalization .

## Inputs

Five inputs, including: (NDHWC, NCDHW)
- x: A 5D Tensor of type float16 or float32, with format NDHWC or NCDHW.
- scale: A Tensor of type float32. Must be 1D if input "x" is with format NDHWC or NCDHW.
Specifies the scaling factor.
- offset: A Tensor of type float32. Must be 3D if input "x" is with format NDHWC or NCDHW.
Specifies the offset.
- mean: A Tensor of type float32. Must be 3D if input "x" is with format NDHWC or NCDHW.
Specifies the mean used for inference. Must be "None" if the
operation is used for training.
- variance: A Tensor of type float32. Must be 3D if input "x" is with format NHWC or NCHW.
Specifies the variance used for inference. Must be "None"
if the operation is used for training . 

## Outputs

Five outputs, including: (NDHWC, NCDHW)
- y: A 5D Tensor of type float16 or float32 for the normalized "x", with format NDHWC or NCDHW.
- batch_mean: A Tensor of type float32. Must be 3D if input "x" is with format NDHWC or NCDHW.
Specifies the mean of "x".
- batch_variance: A Tensor of type float32. Must be 1D if input "x" is with format NDHWC or NCDHW.
Specifies the variance of "x".
- reserve_space_1: An optional Tensor of type float32. Must be 1D if input "x" is with format NDHWC or NCDHW.
Specifies the mean of "x" for gradient computation. Pass "None" to skip this output.
- reserve_space_2: An optional Tensor of type float32. Must be 1D if input "x" is with format NHWC or NCHW.
Specifies the variance of "x" for gradient computation. Pass "None" to skip this output . 

## Attributes

- epsilon: An optional float32, specifying the small value added to variance to avoid dividing by zero. Defaults to "0.0001".
- data_format: An optional string, specifying the format of "x". Defaults to "NCDHW".
- is_training: An optional bool, specifying if the operation is used for training or inference. Defaults to "True" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 scale: float32
- input2 offset: float32
- input3 mean: float32
- input4 variance: float32
- output0 y: float16,float32
- output1 batch_mean: float32
- output2 batch_variance: float32
- output3 reserve_space_1: float32
- output4 reserve_space_2: float32

## Attention Constraints

- If the operation is used for inference and outputs "reserve_space_1" and "reserve_space_2" are available,
then "reserve_space_1" has the same value as "mean" and "reserve_space_2" has the same value as "variance".
- For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 1‰ due to the square root instruction .

## Third-party framework compatibility

- Compatible with the TensorFlow operator fused_batch_norm.
- Compatible with the TensorFlow operator fused_batch_norm_v2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
