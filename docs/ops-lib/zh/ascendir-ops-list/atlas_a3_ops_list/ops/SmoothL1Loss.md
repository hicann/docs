# SmoothL1Loss

```c
REG_OP(SmoothL1Loss)
    .INPUT(predict, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(loss, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(sigma, Float, 1.0)
    .OP_END_FACTORY_REG(SmoothL1Loss)
```

## Brief

Creates a criterion that uses a squared term if the absolute
element-wise error falls below sigma and an L1 term otherwise.

## Inputs

- predict: A ND multi-dimensional tensor of type float16, bfloat16 or float32,
specifying the predictive value. 
- label: A ND multi-dimensional tensor, has same type and shape as "predict",
specifying the target value. 

## Outputs

loss: A multi-dimensional Tensor of type float16, bfloat16 or float32. Indicates
the loss between the predictive value and target value.
Has the same dimensions as "predict". 

## Attributes

- sigma: An optional float. Specifies the threshold of loss. The value must be
non-negative. Defaults to "1.0". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 label: bfloat16,float16,float32
- output0 loss: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator smooth_l1_loss (reduction='none'). 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
