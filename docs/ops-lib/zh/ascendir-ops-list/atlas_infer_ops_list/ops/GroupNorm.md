# GroupNorm

```c
REG_OP(GroupNorm)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(variance, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(data_format, String, "NHWC")
    .ATTR(eps, Float, 0.0001f)
    .ATTR(is_training, Bool, true)
    .OP_END_FACTORY_REG(GroupNorm)
```

## Brief

Performs group normalization . 

## Inputs

Three inputs
- x: A ND Tensor of type float16 or float32, with format NCHW for 4D.
- gamma: A Tensor of type float16 or float32. Must be 1D. Specifies the scaling factor.
- beta: A Tensor of type float16 or float32. Must be 1D. Specifies the offset.

## Outputs

Three outputs
- y: A ND Tensor of type float16 or float32 for the normalized "x",
with format NCHW for 4D.
- mean: A Tensor of type float16 or float32. Must be 1D. Specifies the mean of "x".
- variance: A Tensor of type float16 or float32. Must be 1D. Specifies the variance of "x".

## Attributes

- num_groups: An required int32, specifying the number of group.
- eps: An optional float32, specifying the small value added to
variance to avoid dividing by zero. Defaults to "0.0001".
- data_format: An optional string, specifying the format of "x".
Defaults to "NHWC".
- is_training: An optional bool, specifying if the operation is used for
training or inference. Defaults to "True" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 gamma: float16,float32
- input2 beta: float16,float32
- output0 y: float16,float32
- output1 mean: float16,float32
- output2 variance: float16,float32

## Attention Constraints

- For Atlas 200/300/500 Inference Product, only support NCHW which can be trans to 5HD.
- the value range of the inputs should be constrained between -10000 and 10000.

## Third-party framework compatibility

- Compatible with the PyTorch operator GroupNorm.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
