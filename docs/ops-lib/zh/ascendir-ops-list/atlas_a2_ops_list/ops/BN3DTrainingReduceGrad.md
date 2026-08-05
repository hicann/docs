# BN3DTrainingReduceGrad

```c
REG_OP(BN3DTrainingReduceGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(diff_scale, TensorType({DT_FLOAT}))
    .INPUT(diff_offset, TensorType({DT_FLOAT}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(batch_mean, TensorType({DT_FLOAT}))
    .INPUT(batch_variance, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(epsilon, Float, 0.0001)
    .OP_END_FACTORY_REG(BN3DTrainingReduceGrad)
```

## Brief

Performs the backpropagation of BatchNorm .

## Inputs

Seven inputs, including:
- grads: A 5Dtensor of type float16 or float32 or bfloat16, for the gradient, with format NDHWC or NCDHW.
- x: A 5D tensor of type float16 or float32 or bfloat16, with format NDHWC or NCDHW.
- diff_scale: A 1D tensor of type float32,
for the mean of "x". shape must be C channel.
- diff_offset: A 1D tensor of type float32,
for the variance of "x". shape must be C channel.
- scale: A 1D tensor of type float32.
- batch_mean: A 1D tensor of type float32,
for the mean of "x". shape must be C channel.
- batch_variance: A 1D tensor of type float32,
for the variance of "x" . shape must be C channel. 

## Outputs

y: A 5D Tensor of type float16 or float32 or bfloat16, with format NDHWC or NCDHW. 

## Attributes

epsilon: An optional float32. Defaults to "0.0001". A small float number
added to the variance of "x" . 

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

The preceding layer of this operator must be BN3DTrainingReduceGrad . 
@see BN3DTrainingReduceGrad


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
