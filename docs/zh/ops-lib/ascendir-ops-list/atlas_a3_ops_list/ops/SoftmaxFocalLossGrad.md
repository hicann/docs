# SoftmaxFocalLossGrad

```c
REG_OP(SoftmaxFocalLossGrad)
    .INPUT(pred, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(target, TensorType({DT_INT32}))
    .INPUT(dout, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(alpha, Float, 0.25)
    .ATTR(gamma, Float, 2.0)
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(SoftmaxFocalLossGrad)
```

## Brief

MMCV Function: softmax_focal_loss_grad.

## Inputs

Three inputs, including:
- pred: the predicted tensor. The type support float16 and float32.
- target: the target label Tensor. The type support Int32.
- dout: the grad of previous op grad, which has the sampe shape wth pred. The type support float16 and float32.
- weight: A optional input Tensor, default is None, which helps to calculate the loss by supplying sample weights.
The type support float16 and float32.
    shape of pred should be (B, D), B means batch size, D means the number of labels.
    shape of target should be (B, D).
    shape of weight should be (D, ) 

## Outputs

grad: A mutable Tensor. Has the same type and shape as "pred". 

## Attributes

- alpha: A attribute is used to reweight the sample. The type is float . Default is 0.25
- gamma: A attribute is used to calculate the power of the probability.
    The type is float . Default is 2.0
- reduction: a type of the reduce method. default is 'mean', which means computing the average loss.
'sum' means computing the sum of the loss, 'none' means no reducing. Default is 'mean' 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 pred: float16,float32
- input1 target: int32
- input2 dout: float16,float32
- input3 weight: float16,float32
- output0 grad: float16,float32

## Third-party framework compatibility

Compatible with the MMCV operator SoftmaxFocalLossGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
