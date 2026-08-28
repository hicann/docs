# SigmoidCrossEntropyWithLogitsGrad

```c
REG_OP(SigmoidCrossEntropyWithLogitsGrad)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(target, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(dout, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(gradient, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(SigmoidCrossEntropyWithLogitsGrad)
```

## Brief

Computes the sigmoid cross entropy loss of "predict" and "target" .

## Inputs

Three inputs, including:
- predict: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the predictive value.
- target: A multi-dimensional Tensor of type float16 or float32 or bfloat16, specifying the target value .
- dout:A multi-dimensional Tensor of float16 or float32 or bfloat16,specifying the gradient transferred from the upper layer.

## Outputs

gradient: Sigmoid cross entropy between the predictive value and target value. Has the same dimensions as "predict" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 target: bfloat16,float16,float32
- input2 dout: bfloat16,float16,float32
- output0 gradient: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the scenario where "reduction" is set to "none"of PyTorch operator SigmoidCrossEntropyWithLogitsGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
