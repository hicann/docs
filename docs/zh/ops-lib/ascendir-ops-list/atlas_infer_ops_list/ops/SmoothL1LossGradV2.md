# SmoothL1LossGradV2

```c
REG_OP(SmoothL1LossGradV2)
    .INPUT(predict, TensorType({DT_FLOAT, DT_FLOAT16,DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(dout, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(gradient, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(sigma, Float, 1.0)
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(SmoothL1LossGradV2)
```

## Brief

Calculates the reversed outputs of the function "smooth_l1_loss_v2". Broadcasting is supported.

## Inputs

Three Inputs, including:
- predict: A ND multi-dimensional tensor of type float16, bfloat16 or float32, specifying the predictive value.
- label: A ND multi-dimensional tensor, has same type and shape as "predict", specifying the target value.
- dout: A tensor. Has the same type as "predict".

## Outputs

 gradient: A tensor. Has the same type as "predict". 

## Attributes

Two Attributes, including:
- sigma: An optional float. Specifies the threshold of loss. The value must be non-negative. Defaults to 1.0.
- reduction: An optional string. Specifies the reduction to apply to
the output: 'none' | 'mean' | 'sum'. 'none': no reduction will be applied;
'mean': the sum of the output will be divided by the number of elements in
the output;'sum': the output will be summed. Default: 'mean'. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: float16,float32
- input1 label: float16,float32
- input2 dout: float16,float32
- output0 gradient: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator SmoothL1LossBackward.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
