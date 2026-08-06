# BatchNormExt2

```c
REG_OP(BatchNormExt2)
    .INPUT(input_x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(input_scale, TensorType({DT_FLOAT}))
    .INPUT(input_offset, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(input_mean, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(input_variance, TensorType({DT_FLOAT}))
    .OUTPUT(output_y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(output_mean, TensorType({DT_FLOAT}))
    .OUTPUT(output_variance, TensorType({DT_FLOAT}))
    .OUTPUT(output_reserve_space_1, TensorType({DT_FLOAT}))
    .OUTPUT(output_reserve_space_2, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.0001f)
    .ATTR(data_format, String, "NHWC")
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(BatchNormExt2)
```

## Brief

Performs batch normalization .

## Inputs

Five inputs, including: (NHWC or NCHW supported)
- input_x: A 4D Tensor of type float16 or float32.
- input_scale: A 1D Tensor of type float32, for the scaling factor.
- input_offset: A 1D Tensor of type float32, for the scaling offset.
- input_mean: A 1D Tensor of type float32, for the mean used for inference.
This cannot be used if the operation is used for training.
- input_variance: A 1D Tensor of type float32, for the variance used for inference.
This cannot be used if the operation is used for training . 

## Outputs

Five outputs, including: (NHWC or NCHW supported)
- output_y: A 4D Tensor of type float16 or float32, for the normalized "x".
- output_mean: A 1D Tensor of type float32, for the mean of "x".
- output_variance: A 1D Tensor of type float32, for the variance of "x".
- output_reserve_space_1: A 1D Tensor of type float32, for the mean of "x" for gradient computation.
- output_reserve_space_2: A 1D Tensor of type float32, for the variance of "x" for gradient computation .

## Attributes

- epsilon: An optional float32, specifying the small value
added to variance to avoid dividing by zero. Defaults to "0.0001".
- data_format: An optional string, specifying the format of "x". Defaults to "NHWC".
- is_training: An optional bool, specifying if the operation
is used for training or inference. Defaults to "True" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: float16,float32
- input1 input_scale: float32
- input2 input_offset: float32
- input3 input_mean: float32
- input4 input_variance: float32
- output0 output_y: float16,float32
- output1 output_mean: float32
- output2 output_variance: float32
- output3 output_reserve_space_1: float32
- output4 output_reserve_space_2: float32

## Attention Constraints

- If the operation is used for inference, then output "reserve_space_1"
has the same value as "mean" and output "reserve_space_2" has the same value as "variance".
- For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 1‰ due to the square root instruction .

## Third-party framework compatibility

Compatible with the TensorFlow operator fused_batch_norm_v2.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
