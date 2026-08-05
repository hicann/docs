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

Computes gradients of sigmoid_cross_entropy_with_logits.

## Inputs

- predict: An ND tensor of type float16, float32, bfloat16, specifying the predictive value.
- target: An ND tensor of type float16, float32, bfloat16, specifying the target value.
    Shape must be the same as predict.
- dout: An ND tensor of type float16, float32, bfloat16, specifying the dout value.
    Shape needs to satisfy the broadcast relationship with predict. 

## Outputs

gradient: An ND tensor with the same shape and type as "predict". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 target: bfloat16,float16,float32
- input2 dout: bfloat16,float16,float32
- output0 gradient: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator SigmoidCrossEntropyWithLogitsGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
