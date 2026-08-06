# BNTrainingUpdate

```c
REG_OP(BNTrainingUpdate)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(sum, TensorType({DT_FLOAT}))
    .INPUT(square_sum, TensorType({DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(offset, TensorType({DT_FLOAT}))
    .INPUT(mean, TensorType({DT_FLOAT}))
    .INPUT(variance, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(factor, Float)
    .REQUIRED_ATTR(epsilon, Float)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(mean, TensorType({DT_FLOAT}))
    .OUTPUT(variance, TensorType({DT_FLOAT}))
    .OUTPUT(batch_mean, TensorType({DT_FLOAT}))
    .OUTPUT(batch_variance, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BNTrainingUpdate)
```

## Brief

Performs reduced batch normalization .

## Inputs

Seven inputs, including:
- x: A 4D tensor of type float16 or float32 or bfloat16, with format NHWC or NCHW. Empty tensors are not
supported.
Input tensor, that is, the original data that needs to be normalized.
- sum: A 1D tensor of type float32, the shape is same as dim C of input "x", for the output of operator
BNTrainingReduce.
It represents the sum of the input tensor "x" on the C axis. Has the same format as "x".
- square_sum: A 1D tensor of type float32, the shape is same as dim C of input "x", for the output of operator
BNTrainingReduce.
It represents the sum of squares of the input tensor "x" on the C axis. Has the same format as "x".
- scale: A 1D tensor of type float32, the shape is same as dim C of input "x", for the scaling factor. Has the
same format as "x".
- offset: A 1D tensor of type float32, the shape is same as dim C of input "x", for the scaling offset. Has the
same format as "x".
- mean: A 1D tensor of type float32, the shape is same as dim C of input "x", for the updated mean. Has the same
format as "x".
- variance: A 1D tensor of type float32, the shape is same as dim C of input "x", for the updated variance. Has
the same format as "x". 

## Outputs

Five outputs, including:
- y: A 4D tensor of type float16 or float32 or bfloat16, for normalized "x". Empty tensors are not supported.
Has the same dype, format and shape as "x".
- mean: A 1D tensor of type float32, for the updated mean. shape must be C channel. Has the same format as "x".
- variance: A 1D tensor of type float32, for the updated variance. shape must be C channel. Has the same format
as "x".
- batch_mean: A 1D tensor of type float32, for the mean of "x". shape must be C channel. Has the same format as
"x".
- batch_variance: A 1D tensor of type float32, for the variance of "x" . shape must be C channel. Has the same
format as "x". 

## Attributes

- epsilon: A required float32, specifying the small value added to variance
to avoid dividing by zero.
- factor: A required float32, specifying the weight for updating the mean
and variance . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 sum: float32
- input2 square_sum: float32
- input3 scale: float32
- input4 offset: float32
- input5 mean: float32
- input6 variance: float32
- output0 y: float16,float32
- output1 mean: float32
- output2 variance: float32
- output3 batch_mean: float32
- output4 batch_variance: float32

## Attention Constraints

- This operator is a BatchNorm fusion operator for updating the moving
averages for training. This operator is used in conjunction with
BNTrainingUpdate.
- For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 1/1000 due to the
square root instruction.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
