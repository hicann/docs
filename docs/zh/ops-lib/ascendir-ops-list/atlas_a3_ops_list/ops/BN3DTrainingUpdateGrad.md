# BN3DTrainingUpdateGrad

```c
REG_OP(BN3DTrainingUpdateGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(batch_mean, TensorType({DT_FLOAT}))
    .INPUT(batch_variance, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.0001)
    .OUTPUT(diff_scale, TensorType({DT_FLOAT}))
    .OUTPUT(diff_offset, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BN3DTrainingUpdateGrad)
```

## Brief

Performs the backpropagation of BatchNorm .

## Inputs

Four inputs, including:
- grads: A 5D tensor of type float16 or float32 or bfloat16,
for the gradient, with format NDHWC or NCDHW.
- x: A 5D tensor of type float16 or float32 or bfloat16, with format NDHWC or NCDHW,
the shape is same as input grads.
- batch_mean: A 1D tensor of type float32,
for the mean of "x", the shape is same as dim C of input grads.
- batch_variance: A 1D tensor of type float32,
for the variance of "x", the shape is same as dim C of input grads. 

## Outputs

- diff_scale: A 1D Tensor of type float32,
for the offset of "scale", the shape is same as dim C of input grads.
- diff_offset: A 1D Tensor of type float32,
for the offset of "offset", the shape is same as dim C of input grads. 

## Attributes

epsilon: An optional float32. Defaults to "0.0001". A small float number
added to the variance of "x" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 batch_mean: float32
- input3 batch_variance: float32
- output0 diff_scale: float32
- output1 diff_offset: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
