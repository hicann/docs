# BNTrainingReduceGrad

```c
REG_OP(BNTrainingReduceGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(diff_scale, TensorType({DT_FLOAT}))
    .INPUT(diff_offset, TensorType({DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(batch_mean, TensorType({DT_FLOAT}))
    .INPUT(batch_variance, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(epsilon, Float, 0.0001)
    .OP_END_FACTORY_REG(BNTrainingReduceGrad)
```

## Brief

Performs the backpropagation of BatchNorm .

## Inputs

Seven inputs, including:
- grads: A 4D tensor of type float16 or float32 or bfloat16, for the gradient, with format NHWC or NCHW.
The gradient of the loss function with respect to the output of the batch normalization layer.
- x: A 4D tensor of type float16 or float32 or bfloat16, with format NHWC or NCHW.
It represents the data input to the batch normalization layer during the forward pass.
Has the same type, format and shape as "grads".
- diff_scale: A 1D tensor of type float32, the shape is same as dim C of input grads.
Indicates the gradient of the loss function to the scaling parameter "scale".
Has the same format as "grads".
- diff_offset: A 1D tensor of type float32, the shape is same as dim C of input grads.
Represents the gradient of the loss function to the offset parameter.
Has the same format as "grads".
- scale: A 1D tensor of type float32, the shape is same as dim C of input grads.
The scaling parameter in batch normalization, used to adjust the normalized output.
Has the same format as "grads".
- batch_mean: A 1D tensor of type float32, the shape is same as dim C of input grads, for the mean of "x".
Has the same format as "grads".
- batch_variance: A 1D tensor of type float32, the shape is same as dim C of input grads, for the variance of
"x".
Has the same format as "grads". 

## Outputs

y: A Tensor of type float16, float32 or bfloat16, with format NHWC or NCHW.
It represents the gradient of the loss function with respect to the input data x.
Has the same type, format and shape as "grads". 

## Attributes

epsilon: An optional float32. Defaults to "0.0001".
Represents a small positive number added to the variance of "x" to prevent division by zero. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 diff_scale: float32
- input3 diff_offset: float32
- input4 scale: float32
- input5 batch_mean: float32
- input6 batch_variance: float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

The preceding layer of this operator must be BNTrainingUpdateGrad . 
@see BNTrainingUpdateGrad


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
