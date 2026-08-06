# CrossEntropyLossGrad

```c
REG_OP(CrossEntropyLossGrad)
    .INPUT(grad_loss, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(log_prob, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(target, TensorType({DT_INT64, DT_INT32}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(grad_zloss, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(lse_gor_zloss, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(x_grad, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(reduction, String, "mean")
    .ATTR(ignore_index, Int, -100)
    .ATTR(label_smoothing, Float, 0.0)
    .ATTR(lse_square_scale_for_zloss, Float, 0.0)
    .OP_END_FACTORY_REG(CrossEntropyLossGrad)
```

## Brief

Performs the backpropagation of CrossEntropyLoss for training scenarios .

## Inputs

Six inputs, including:
- grad_loss: A 1D tensor or scalar of type float16 or float32 or bfloat16, specifying the backpropagation gradient. When reduction is "none", the shape is [N], when reduction is "sum" or "mean", it is scalar. N is batch size.
- log_prob: A 2D tensor of type float16 or float32 or bfloat16. Has the same dtype as grad_loss, specifying the logarithmized probabilities of the outputs. Shape only support [N, C], where N is batch size, C is class.
- target: A 1D tensor of type int32 or int64, specifying the target value. It represent the target squences. Shape is [N]. The range of values is [0, C).
- weight: An optional 1D tensor of type float32, specifying the weight value. Shape is [C].
- grad_zloss: An optional ND tensor of type float16 or float32 or bfloat16. Has the same dtype as grad_loss. Reserved.
- lse_gor_zloss: An optional ND tensor of type float16 or float32 or bfloat16. Has the same dtype as grad_loss. Reserved.

## Outputs

x_grad: A 2D tensor. Has the same dtype and shape as log_prob.

## Attributes

- reduction: A character string from "none", "mean", and "sum", specifying the gradient output mode. Defaults to "mean" .
- ignore_index: An optional int. Specifies a target value that is ignored and does not contribute to the input gradient. Defaults to -100.
- label_smoothing: An optional float attr in [0.0, 1.0]. Specifies the amount of smoothing when computing the loss. Defaults to 0.0.
- lse_square_scale_for_zloss: An optional float attr, Default: 0.0. Reserved.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_loss: bfloat16,float16,float32
- input1 log_prob: bfloat16,float16,float32
- input2 target: int64
- input3 weight: float32
- input4 grad_zloss: bfloat16,float16,float32
- output0 x_grad: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
