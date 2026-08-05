# BatchNormGradExt2

```c
REG_OP(BatchNormGradExt2)
    .INPUT(y_backprop, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(reserve_space_1, TensorType({DT_FLOAT}))
    .INPUT(reserve_space_2, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.0001f)
    .ATTR(data_format, String, "NHWC")
    .ATTR(is_training, Bool, true)
    .OUTPUT(x_backprop, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(scale_backprop, TensorType({DT_FLOAT}))
    .OUTPUT(offset_backprop, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_3, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_4, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BatchNormGradExt2)
```

## Brief

Performs the backpropagation of BatchNorm .

## Inputs

Five inputs, including:
- y_backprop: A 4D Tensor of type float16 or float32, with format NHWC or NCHW, for the gradient.
- x: A 4D Tensor of type float16 or float32, with format NHWC or NCHW, the shape is same as input y_backprop.
- scale: A 4D Tensor of type float32, with format NHWC or NCHW, the shape is same as input y_backprop.
- reserve_space_1: A 4D Tensor of type float32, with format NHWC or NCHW, the shape is same as input y_backprop,
it is an output of BatchNormExt2.
- reserve_space_2: A 4D Tensor of type float32, with format NHWC or NCHW, the shape is same as input y_backprop,
it is an output of BatchNormExt2 . 

## Outputs

- x_backprop: A Tensor of type float16 or float32, with format NHWC or NCHW, for the offset of "x".
- scale_backprop: A Tensor of type float32, with format NHWC or NCHW, for the offset of "scale".
- offset_backprop: A Tensor of type float32, with format NHWC or NCHW, for the offset of "offset".
- reserve_space_3: A Tensor of type float32, with format NHWC or NCHW.
- reserve_space_4: A Tensor of type float32, with format NHWC or NCHW .

## Attributes

- epsilon: A required float32. A small float number added to the variance of "x".
- data_format: A required string for the format.
- is_training: A required bool for specifying the operation is for training (true) or inference (false) .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_backprop: float16,float32
- input1 x: float16,float32
- input2 scale: float32
- input3 reserve_space_1: float32
- input4 reserve_space_2: float32
- output0 x_backprop: float16,float32
- output1 scale_backprop: float32
- output2 offset_backprop: float32
- output3 reserve_space_3: float32
- output4 reserve_space_4: float32

## Attention Constraints

The preceding layer of this operator must be BatchNormExt2 . 
@see BatchNormExt2

## Third-party framework compatibility

Compatible with the TensorFlow operator FusedBatchNormGradV2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
