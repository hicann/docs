# SmoothL1LossV2

```c
REG_OP(SmoothL1LossV2)
    .INPUT(predict, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(label, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(loss, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(sigma, Float, 1.0)
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(SmoothL1LossV2)
```

## Brief

Creates a criterion that uses a squared term if the absolute
element-wise error falls below sigma and an L1 term otherwise. It is
less sensitive to outliers than the MSELoss and in some cases prevents
exploding gradients.

## Inputs

- predict: A ND multi-dimensional tensor of type float16, bfloat16 or float32,
specifying the predictive value. 
- label: A ND multi-dimensional tensor, has same type and shape as "predict",
specifying the target value. 

## Outputs

loss: A multi-dimensional Tensor of type float16, bfloat16 or float32. Indicates the loss between the predictive value and target value.
Has the same dimensions as "predict". 

## Attributes

- sigma: An optional float. Specifies the threshold of loss. The value must be positive number. Defaults
to "1.0". 
- reduction: An optional string. Specifies the reduction to apply to
the output: 'none' | 'mean' | 'sum'. 'none': no reduction will be applied;
'mean': the sum of the output will be divided by the number of elements in
the output;'sum': the output will be summed. Default: 'mean'. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 label: bfloat16,float16,float32
- output0 loss: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator smooth_l1_loss. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
