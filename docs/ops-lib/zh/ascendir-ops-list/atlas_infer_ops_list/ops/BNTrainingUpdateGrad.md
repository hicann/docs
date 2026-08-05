# BNTrainingUpdateGrad

```c
REG_OP(BNTrainingUpdateGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(batch_mean, TensorType({DT_FLOAT}))
    .INPUT(batch_variance, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.0001)
    .OUTPUT(diff_scale, TensorType({DT_FLOAT}))
    .OUTPUT(diff_offset, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BNTrainingUpdateGrad)
```

## Brief

Performs the backpropagation of BatchNorm .

## Inputs

Four inputs, including:
- grads: A 4D tensor of type float16 or float32 or bfloat16,
for the gradient, with format NHWC or NCHW.
Indicates the gradient of the loss function with respect to the output of the batch normalization layer.
- x: A 4D tensor of type float16 or float32 or bfloat16, with format NHWC or NCHW.
Indicates the data input to the batch normalization layer during the forward propagation process.
Has the same type, format and shape as "grads".
- batch_mean: A 1D tensor of type float32,
for the mean of "x". Shape must be C channel.
Has the same format as "grads".
- batch_variance: A 1D tensor of type float32,
for the variance of "x" . Shape must be C channel.
Has the same format as "grads". 

## Outputs

- diff_scale: A 1D Tensor of type float32,
for the offset of "scale". Shape must be C channel.
Has the same format as "grads".
- diff_offset: A 1D Tensor of type float32,
for the offset of "offset". Shape must be C channel.
Has the same format as "grads". 

## Attributes

epsilon: An optional float32. Defaults to "0.0001".
Represents a very small positive number that is added to the variance of "x" to prevent division by zero. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32
- input1 x: float16,float32
- input2 batch_mean: float32
- input3 batch_variance: float32
- output0 diff_scale: float32
- output1 diff_offset: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
