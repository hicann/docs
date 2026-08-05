# BatchNorm

```c
REG_OP(BatchNorm)
    .INPUT(x, "T1")
    .INPUT(scale, "T2")
    .INPUT(offset, "T2")
    .OPTIONAL_INPUT(mean, "T2")
    .OPTIONAL_INPUT(variance, "T2")
    .OUTPUT(y, "T1")
    .OUTPUT(batch_mean, "T2")
    .OUTPUT(batch_variance, "T2")
    .OUTPUT(reserve_space_1, "T2")
    .OUTPUT(reserve_space_2, "T2")
    .OUTPUT(reserve_space_3, "T2")
    .ATTR(epsilon, Float, 1e-4f)
    .ATTR(data_format, String, "NHWC")
    .ATTR(is_training, Bool, true)
    .ATTR(exponential_avg_factor, Float, 1.0f)
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BatchNorm)
```

## Brief

Performs batch normalization with support for 4D/5D tensors and training/inference modes.

## Inputs

Five inputs, with format constraints as follows:
- x: A 4D or 5D tensor of type float16, bfloat16, or float32.
       Supported data formats:
       - 4D: NHWC (batch, height, width, channels) or NCHW (batch, channels, height, width).
       - 5D: NDHWC (batch, depth, height, width, channels) or NCDHW (batch, channels, depth, height, width).
- scale: A 1D tensor of type float32, with length equal to the number of channels in "x".
       Specifies the scaling factor (gamma) applied after normalization.
- offset: A 1D tensor of type float32, with length equal to the number of channels in "x".
       Specifies the offset (beta) applied after scaling.
- mean: A 1D tensor of type float32, with length equal to the number of channels in "x".
       - Inference mode (is_training=false): Must be provided as input, representing the
         moving mean computed during training.
       - Training mode (is_training=true): Optional input. When provided, will be used to
         initialize the moving mean for updates; when None, moving mean starts from zeros.
- variance: A 1D tensor of type float32, with length equal to the number of channels in "x".
       - Inference mode (is_training=false): Must be provided as input, representing the
         moving variance computed during training.
       - Training mode (is_training=true): Optional input. When provided, will be used to
         initialize the moving variance for updates; when None, moving variance starts from ones.

## Outputs

Up to six outputs, with shape and format matching "x" unless specified:
- y: A tensor with the same rank (4D/5D), type, and format as "x", containing normalized values.
       (Required output)
- batch_mean: A 1D tensor of type float32 (channel dimension).
       - Training mode: Mean of the current batch (computed over spatial dimensions).
       - Inference mode: Equal to input "mean" (for compatibility).
       (Required output)
- batch_variance: A 1D tensor of type float32 (channel dimension).
       - Training mode: Variance of the current batch (computed over spatial dimensions, with Bessel's correction).
       - Inference mode: Equal to input "variance" (for compatibility).
       (Required output)
- reserve_space_1: Optional 1D tensor of type float32 (channel dimension).
       Reserved for gradient computation.
       - Training mode: Same as batch_mean.
       - Inference mode: Same as input "mean".
- reserve_space_2: Optional 1D tensor of type float32 (channel dimension).
       Reserved for gradient computation.
       - Training mode: saved inv_var (1/sqrt(epsilon + variance), to be reused in the backward gradient computation.
       - Inference mode: Same as input "variance".
- reserve_space_3: A 1D tensor of type float32 with exactly one element.
       Exists solely for TensorFlow compatibility and contains no meaningful data.

## Attributes

- epsilon: Optional float32. Small value added to variance to avoid division by zero.
       Defaults to 0.0001f.
- data_format: Optional string. Specifies the data format of "x".
       Allowed values: "NHWC" (4D default), "NCHW" (4D), "NDHWC" (5D), "NCDHW" (5D).
- is_training: Optional bool. Specifies operation mode:
       - true: Training mode (computes batch mean/variance and updates moving stats).
       - false: Inference mode (uses provided mean/variance for normalization).
       Defaults to true.
- exponential_avg_factor: Optional float32. Factor for updating moving averages during training.
       Formula: new_mean = (1 - factor) * old_mean + factor * batch_mean.
       Defaults to 1.0f.

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
- output5 reserve_space_3: float32
### AI CPU
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


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
