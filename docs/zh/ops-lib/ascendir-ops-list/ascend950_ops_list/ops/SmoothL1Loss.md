# SmoothL1Loss

```c
REG_OP(SmoothL1Loss)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(loss, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(sigma, Float, 1.0)
    .OP_END_FACTORY_REG(SmoothL1Loss)
```

## Brief

Computes the regression box of the RPN. It is a FasterRCNN operator.

## Inputs

Two inputs, including:
- predict: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the predictive value.
The maximum dimension is 8.
- label: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the target value.
The maximum dimension is 8, predict and label can be broadcast.

## Outputs

loss: Indicates the loss between the predictive value and target value.
Has the same dtype and dimensions as "predict".

## Attributes

sigma: Must be a floating point number. Defaults to "1.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 label: bfloat16,float16,float32
- output0 loss: bfloat16,float16,float32

## Attention Constraints

This operator does not perform the "reduce" operation on the loss value.
Call other reduce operators to perform "reduce" operation on the loss if required.

## Third-party framework compatibility

Compatible with the scenario where "reduction" is set to "none"of PyTorch operator SmoothL1Loss.


---

[Back to Operator Specifications (Ascend950)](../README.md)
