# SigmoidCrossEntropyWithLogitsV2

```c
REG_OP(SigmoidCrossEntropyWithLogitsV2)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(target, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(pos_weight, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(loss, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(SigmoidCrossEntropyWithLogitsV2)
```

## Brief

Computes the sigmoid cross entropy loss of "predict" and "target".  Broadcasting is supported.

## Inputs

four inputs, including:
- predict: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the predictive value.
- target: A multi-dimensional Tensor, has the same dtype as "predict", specifying the target value.
- weight: An optional multi-dimensional Tensor, has the same dtype as "predict", specifying the weight value.
- pos_weight: An optional multi-dimensional Tensor, has the same dtype as "predict", specifying the pos weight value.

## Outputs

loss: An ND Tensor, Sigmoid cross entropy between the predictive value and target value. Has the same dimensions as "predict". 

## Attributes

reduction: A optional string attr from ["none", "mean", "sum"],
 specifying the reduction type to be applied to the output. Defaults to "mean". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: float16,float32
- input1 target: float16,float32
- input2 weight: float16,float32
- input3 pos_weight: float16,float32
- output0 loss: float32

## Third-party framework compatibility

Compatible with PyTorch operator BCEWithLogitsLoss.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
