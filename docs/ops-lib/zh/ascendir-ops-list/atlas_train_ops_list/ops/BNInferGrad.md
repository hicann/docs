# BNInferGrad

```c
REG_OP(BNInferGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .INPUT(batch_variance, TensorType({DT_FLOAT}))
    .OUTPUT(x_backprop, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(epsilon, Float, 0.0001)
    .OP_END_FACTORY_REG(BNInferGrad)
```

## Brief

Performs the backpropagation of BatchNorm for inference .

## Inputs

Three inputs, including:
- grads: A tensor of type float16 or float32 or bfloat16. Indicates the gradient of the BathNorm output parameter
"y".
Shape support 4D and 5D. Format support NHWC, NCHW or NC1HWC0.
- scale: A 1D tensor of type float32. Shape must be C channel.
Specifies the scaling factor. Has the same format as "grads".
- batch_variance: A 1D tensor of type float32. Calculated variance, that is, the value of BatchNorm output
parameter "batch_variance".
Shape must be C channel. Has the same format as "grads". 

## Outputs

x_backprop: A tensor of type float16 or float32 or bfloat16.
Indicates the gradient of BathNorm input data "x".
Has the same type, shape and format as "grads". 

## Attributes

epsilon: An optional float32. Defaults to "0.0001". A small float number
added to the variance of "batch_variance". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32
- input1 scale: float32
- input2 batch_variance: float32
- output0 x_backprop: float16,float32

## Attention Constraints

The preceding layer of this operator must be operator BatchNorm.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
