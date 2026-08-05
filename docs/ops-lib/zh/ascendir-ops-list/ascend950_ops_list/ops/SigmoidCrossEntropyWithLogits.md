# SigmoidCrossEntropyWithLogits

```c
REG_OP(SigmoidCrossEntropyWithLogits)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(target, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(loss, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(SigmoidCrossEntropyWithLogits)
```

## Brief

Performs the backpropagation of SigmoidCrossEntropyWithLogits for training scenarios .

## Inputs

Two inputs, including:
- predict: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the predictive value.
- target: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the target value.

## Outputs

loss: Return loss. Has the same dimensions and type as "predict" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 target: bfloat16,float16,float32
- output0 loss: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the scenario where "reduction" is set to "none"of PyTorch operator SigmoidCrossEntropyWithLogits.


---

[Back to Operator Specifications (Ascend950)](../README.md)
