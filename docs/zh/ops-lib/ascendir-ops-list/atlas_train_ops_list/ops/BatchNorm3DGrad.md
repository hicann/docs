# BatchNorm3DGrad

```c
REG_OP(BatchNorm3DGrad)
    .INPUT(y_backprop, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(reserve_space_1, TensorType({DT_FLOAT}))
    .INPUT(reserve_space_2, TensorType({DT_FLOAT}))
    .OUTPUT(x_backprop, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(scale_backprop, TensorType({DT_FLOAT}))
    .OUTPUT(offset_backprop, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_4, TensorType({DT_FLOAT}))
    .OUTPUT(reserve_space_5, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.0001f)
    .ATTR(data_format, String, "NCDHW")
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(BatchNorm3DGrad)
```

## Brief

Performs the backpropagation of BatchNorm .

## Inputs

Five inputs, including:
- y_backprop: A 5D Tensor of type float16 or float32, with format NDHWC, NCDHW, for the gradient.
- x: A 5D Tensor of type float16 or float32, with format NDHWC, NCDHW.
- scale: A 5D Tensor of type float32, with format NDHWC, NCDHW.
- reserve_space_1: A 5D Tensor of type float32, with format NDHWC, NCDHW. It is an output of BatchNorm.
- reserve_space_2: A 5D Tensor of type float32, with format NDHWC, NCDHW. It is an output of BatchNorm .

## Outputs

- x_backprop: A Tensor of type float16 or float32, with format NDHWC, NCDHW, for the offset of "x".
- scale_backprop: A Tensor of type float32, with format NDHWC, NCDHW, for the offset of "scale".
- *offset_backprop: A Tensor of type float32, with format NDHWC, NCDHW, for the offset of "offset".
- *reserve_space_4: A Tensor of type float32, with shape NDHWC, NCDHW. Pass "None" to skip this output.
- *reserve_space_5: A Tensor of type float32, with shape NDHWC, NCDHW. Pass "None" to skip this output .

## Attributes

- epsilon: An optional float32. Defaults to "0.0001". A small float number added to the variance of "x".
- data_format: An optional string. Defaults to "NCDHW".
- is_training: An optional bool. Defaults to "true". Specifies the operation is for training (default) or inference .

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
- output3 reserve_space_4: float32
- output4 reserve_space_5: float32

## Attention Constraints

The preceding layer of this operator must be operator BatchNorm . 
@see BatchNorm

## Third-party framework compatibility

Compatible with the TensorFlow operators FusedBatchNormGradV2 and FusedBatchNorm3DGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
