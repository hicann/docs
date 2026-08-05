# BatchNormGrad

```c
REG_OP(BatchNormGrad)
    .INPUT(y_backprop, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(reserve_space_1, TensorType({DT_FLOAT}))
    .INPUT(reserve_space_2, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(reserve_space_3, TensorType({DT_FLOAT}))
    .OUTPUT(x_backprop, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(scale_backprop, TensorType({DT_FLOAT}))
    .OUTPUT(offset_backprop, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_4, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_5, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-4)
    .ATTR(data_format, String, "NHWC")
    .ATTR(is_training, Bool, true)
    .ATTR(output_mask, ListBool, {true, false, false})
    .OP_END_FACTORY_REG(BatchNormGrad)
```

## Brief

Performs the backpropagation of BatchNorm.

## Inputs

Six inputs, including:
- y_backprop: A 4D or 5D Tensor of type bfloat16, float16 or float32, with format NCHW, NHWC, NDHWC or NCDHW, for the gradient.
- x: A 4D or 5D Tensor of type bfloat16, float16 or float32, with format NCHW, NHWC, NDHWC or NCDHW, the same shape with "y_backprop".
- scale: A 1D Tensor of type float32, with format ND, shape must be C channel.
- reserve_space_1: A 1D Tensor of type float32, with format ND, shape must be C channel. It is an output of BatchNorm.
When in training mode, it represents the saved mean of "x". And in inference mode, it represents the running mean of "x".
- reserve_space_2: A 1D Tensor of type float32, with format ND, shape must be C channel. It is an output of BatchNorm.
- reserve_space_3: A 1D optional Tensor of type float32, with format ND. Not used and not involved in calculations. When in training mode,
it represents the saved inverse standard deviation of "x" And in inference mode, it represents the running variance of "x".  

## Outputs

- x_backprop: A 4D or 5D Tensor of type bfloat16, float16 or float32, with format NCHW, NHWC, NDHWC or NCDHW. For the offset of "x".
the same shape with "x".
- scale_backprop: A Tensor of type float32, with format ND, for the offset of "scale", the same shape format with scale.
- offset_backprop: A Tensor of type float32, with format ND, for the offset of "offset", the same shape format with scale.
- reserve_space_4: A Tensor of type float32, with shape ND. The same shape format with scale.
- reserve_space_5: A Tensor of type float32, with shape ND. The same shape format with scale.

## Attributes

- epsilon: An optional float32. Defaults to "1e-4". A small float number used to add with running variance of "x" in inference mode.
- data_format: An optional string. Defaults to "NHWC". Should be same as y_backprop/x/x_backprop's dtype.
- is_training: An optional bool. Defaults to "true". Specifies the operation is for training (default) or inference.
- output_mask: An optional ListBool. Defaults to [true, false, false]. Valid only in inference mode, it determines whether
the outputs "x_backprop", "scale_backprop" and "offset_backprop" contain actual reseluts. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_backprop: float16,float32
- input1 x: float16,float32
- input2 scale: float32
- input3 reserve_space_1: float32
- input4 reserve_space_2: float32
- input5 reserve_space_3: float32
- output0 x_backprop: float16,float32
- output1 scale_backprop: float32
- output2 offset_backprop: float32
- output3 reserve_space_4: float32
- output4 reserve_space_5: float32
### AI CPU
- input0 y_backprop: float16,float32
- input1 x: float16,float32
- input2 scale: float32
- input3 reserve_space_1: float32
- input4 reserve_space_2: float32
- output0 x_backprop: float16,float32
- output1 scale_backprop: float32
- output2 offset_backprop: float32
- output3 reserve_space_4: float32
- output4 reserve_space_5: float32

## Attention Constraints

The preceding layer of this operator must be operator BatchNorm . 
@see BatchNorm

## Third-party framework compatibility

Compatible with the TensorFlow operators FusedBatchNormGrad, FusedBatchNormGradV2 and FusedBatchNormGradV3.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
