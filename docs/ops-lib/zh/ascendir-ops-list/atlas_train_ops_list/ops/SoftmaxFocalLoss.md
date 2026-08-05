# SoftmaxFocalLoss

```c
REG_OP(SoftmaxFocalLoss)
    .INPUT(pred, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(target, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .ATTR(gamma, Float, 2.0)
    .ATTR(alpha, Float, 0.25)
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(SoftmaxFocalLoss)
```

## Brief

Computes the softmax focal loss of "pred" and "target".

## Inputs

Three inputs, including:
- pred: A 2-dimensional Tensor of type float16 or float32, specifying the predicted value.
- target: A 1-dimensional Tensor of type int32, specifying the target value.
- weight: A 1-dimensional Tensor, specifying the weight value on class_wise.

## Outputs

y: Softmax focal loss between the predicted value and target value. Has the same dimensions as "pred". 

## Attributes

- gamma: An optional float, specifying the exponent of the modulating factor (1 - pt)
to balance easy/hard examples. Defaults to 2.0.
- alpha: An optional float, specifying the weighting factor in range (1, 0) to balance
the importance of positive/negative examples or less than 0 for ignore. Defaults to 0.25.
- reduction: A optional character string from "none", "mean", and "sum", specifying the
reduction type to be applied to the output. Defaults to "mean".  reduction only support
"none" currently for matching mmcv.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 pred: float16,float32
- input1 target: int32
- input2 weight: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with mmcv operator SoftmaxFocalLoss.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
